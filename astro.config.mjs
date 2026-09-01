// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://docs.orreth.ai',
	integrations: [
		starlight({
			title: 'Orreth',
			description:
				'Documentation for Orreth — a governed runtime for agentic systems: a small kernel your agents join, and capabilities you build on top.',
			social: [
				{ icon: 'github', label: 'GitHub', href: 'https://github.com/iotlodge/orreth' },
			],
			customCss: ['./src/styles/orreth.css'],
			sidebar: [
				{
					label: 'Learn',
					items: [
						{ label: 'What is Orreth', link: '/' },
						{ label: 'The anatomy of a running world', slug: 'learn/anatomy' },
						{ label: 'What works today', slug: 'learn/what-works-today' },
						{ label: 'Glossary', slug: 'learn/glossary' },
					],
				},
				{
					label: 'Build',
					items: [
						{ label: 'Quickstart', slug: 'build/quickstart' },
						{ label: 'Build your first world', slug: 'build/first-world' },
						{ label: 'Build your first capability', slug: 'build/first-capability' },
						{ label: 'Bring your own agent', slug: 'build/bring-your-own-agent' },
					],
				},
				{
					label: 'Reference',
					items: [
						{ label: 'The HTTP API', slug: 'reference/http-api' },
						{ label: 'Configuration — the dials', slug: 'reference/configuration' },
						{ label: 'The residents', slug: 'reference/residents' },
						{ label: 'The contracts', slug: 'reference/contracts' },
						{ label: 'The capability manifest', slug: 'reference/capability-manifest' },
					],
				},
				// More pages arrive with the next spoonfuls of design dive 0064 —
				// the sidebar only ever lists pages that exist.
			],
		}),
	],
});
