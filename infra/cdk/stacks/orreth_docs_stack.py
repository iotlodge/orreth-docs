# PROVENANCE: Fable 5 (claude-fable-5) — 0064 The Open Book, the docs site · 2026-08-31
"""docs.orreth.ai — the Orreth documentation, served static.

Mirrors the demo site's stack (the smallest possible surface): S3 (private,
OAC) + CloudFront + DNS-validated ACM. No compute, no login, no origin to
probe. The Starlight build in ../../dist is the only content.

Custom domain is optional: pass -c docs_domain=docs.orreth.ai
-c orreth_zone_id=ZXXXX -c orreth_zone_name=orreth.ai to alias it; without
them the CloudFront URL serves.
"""
from aws_cdk import (
    CfnOutput,
    RemovalPolicy,
    Stack,
    Tags,
    aws_certificatemanager as acm,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_route53 as route53,
    aws_route53_targets as targets,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
)
from constructs import Construct


class OrrethDocsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, *,
                 site_dir: str, docs_domain: str | None = None,
                 zone_id: str | None = None, zone_name: str | None = None,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        Tags.of(self).add("Project", "orreth.ai")
        Tags.of(self).add("ManagedBy", "CDK")

        bucket = s3.Bucket(
            self,
            "SiteBucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        cert = None
        hosted_zone = None
        if docs_domain and zone_id and zone_name:
            hosted_zone = route53.HostedZone.from_hosted_zone_attributes(
                self, "Zone", zone_name=zone_name, hosted_zone_id=zone_id)
            cert = acm.Certificate(
                self,
                "SiteCert",
                domain_name=docs_domain,
                validation=acm.CertificateValidation.from_dns(hosted_zone),
            )

        # Starlight emits pretty URLs (/learn/anatomy/ → .../index.html);
        # default_root_object only covers the root, so a tiny edge function
        # appends index.html to directory and extensionless requests.
        rewrite_fn = cloudfront.Function(
            self,
            "IndexRewrite",
            code=cloudfront.FunctionCode.from_inline(
                "function handler(event){var r=event.request;var u=r.uri;"
                "if(u.endsWith('/')){r.uri=u+'index.html';}"
                "else if(!u.split('/').pop().includes('.')){r.uri=u+'/index.html';}"
                "return r;}"
            ),
        )

        distribution = cloudfront.Distribution(
            self,
            "CDN",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3BucketOrigin.with_origin_access_control(bucket),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                cache_policy=cloudfront.CachePolicy.CACHING_OPTIMIZED,
                function_associations=[
                    cloudfront.FunctionAssociation(
                        function=rewrite_fn,
                        event_type=cloudfront.FunctionEventType.VIEWER_REQUEST,
                    ),
                ],
            ),
            default_root_object="index.html",
            domain_names=[docs_domain] if cert else None,
            certificate=cert,
            price_class=cloudfront.PriceClass.PRICE_CLASS_100,
            http_version=cloudfront.HttpVersion.HTTP2_AND_3,
            # Starlight is a multi-page static site: directory URLs resolve to
            # index.html via the sub-path, and a miss should show the site's
            # own 404 page, not an S3 XML error.
            error_responses=[
                cloudfront.ErrorResponse(
                    http_status=403,
                    response_http_status=404,
                    response_page_path="/404.html",
                ),
            ],
        )

        if hosted_zone and docs_domain:
            route53.ARecord(
                self,
                "DocsAlias",
                zone=hosted_zone,
                record_name=docs_domain,
                target=route53.RecordTarget.from_alias(
                    targets.CloudFrontTarget(distribution)),
            )

        # every deploy ships the fresh build and invalidates the edge cache.
        s3deploy.BucketDeployment(
            self,
            "DeploySite",
            sources=[s3deploy.Source.asset(site_dir)],
            destination_bucket=bucket,
            distribution=distribution,
            distribution_paths=["/*"],
        )

        # 0064 — the apex (JB's lock, 2026-08-31): orreth.ai itself, blank
        # until today, 301-redirects to the book. The viewer-request function
        # answers before any origin is consulted; the bucket origin is never
        # reached and never listed.
        if hosted_zone and zone_name and docs_domain:
            apex_cert = acm.Certificate(
                self,
                "ApexCert",
                domain_name=zone_name,
                subject_alternative_names=[f"www.{zone_name}"],
                validation=acm.CertificateValidation.from_dns(hosted_zone),
            )
            apex_fn = cloudfront.Function(
                self,
                "ApexRedirect",
                code=cloudfront.FunctionCode.from_inline(
                    "function handler(event){return {statusCode:301,"
                    "statusDescription:'Moved Permanently',headers:{location:"
                    f"{{value:'https://{docs_domain}'+event.request.uri}}}}}};}}"
                ),
            )
            apex_dist = cloudfront.Distribution(
                self,
                "ApexCDN",
                default_behavior=cloudfront.BehaviorOptions(
                    origin=origins.S3BucketOrigin.with_origin_access_control(bucket),
                    viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                    cache_policy=cloudfront.CachePolicy.CACHING_DISABLED,
                    function_associations=[
                        cloudfront.FunctionAssociation(
                            function=apex_fn,
                            event_type=cloudfront.FunctionEventType.VIEWER_REQUEST,
                        ),
                    ],
                ),
                domain_names=[zone_name, f"www.{zone_name}"],
                certificate=apex_cert,
                price_class=cloudfront.PriceClass.PRICE_CLASS_100,
            )
            for rec_id, rec_name in (("ApexAlias", zone_name),
                                     ("WwwAlias", f"www.{zone_name}")):
                route53.ARecord(
                    self,
                    rec_id,
                    zone=hosted_zone,
                    record_name=rec_name,
                    target=route53.RecordTarget.from_alias(
                        targets.CloudFrontTarget(apex_dist)),
                )
            CfnOutput(self, "ApexRedirectTo", value=f"https://{docs_domain}")

        CfnOutput(self, "CloudFrontDomain", value=distribution.distribution_domain_name)
        CfnOutput(self, "CloudFrontDistId", value=distribution.distribution_id)
        if docs_domain:
            CfnOutput(self, "DocsUrl", value=f"https://{docs_domain}")
