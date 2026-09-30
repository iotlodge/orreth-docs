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
				'Documentation for Orreth — a kernel for fleets of agents: identity, memory, rails, meter, gate, watches and levers held in one place under one law.',
			social: [
				{ icon: 'rocket', label: 'Live demo', href: 'https://demo.orreth.ai' },
				{ icon: 'github', label: 'GitHub', href: 'https://github.com/iotlodge/orreth' },
			],
			customCss: ['./src/styles/orreth.css'],
			// mermaid rides in only on pages that carry a diagram; theme follows the book's light
			head: [
				{
					tag: 'script',
					attrs: { type: 'module' },
					content:
						"if (document.querySelector('pre.mermaid')) { const { default: mermaid } = await import('https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs'); const dark = document.documentElement.dataset.theme !== 'light'; mermaid.initialize({ startOnLoad: false, theme: dark ? 'dark' : 'neutral' }); await mermaid.run({ querySelector: 'pre.mermaid' }); }",
				},
			],
			sidebar: [
				{
					label: 'Learn',
					items: [
						{ label: 'What is Orreth', link: '/' },
						{ label: 'One law at every layer', slug: 'learn/one-law' },
						{ label: 'The anatomy of a running world', slug: 'learn/anatomy' },
						{ label: 'How the kernel works', slug: 'learn/how-the-kernel-works' },
						{ label: 'What works today', slug: 'learn/what-works-today' },
						{ label: 'Glossary', slug: 'learn/glossary' },
					],
				},
				{
					label: 'Build',
					items: [
						{ label: 'Quickstart', slug: 'build/quickstart' },
						{ label: 'Your first world', slug: 'build/first-world' },
						{ label: 'Seat your own body', slug: 'build/your-own-body' },
						{ label: 'Run it from the repository', slug: 'build/from-the-repository' },
					],
				},
				{
					label: 'Watch',
					items: [
						{ label: 'The panel', slug: 'watch/the-panel' },
						{ label: 'The tour', slug: 'watch/the-tour' },
						{ label: 'The one chat', slug: 'watch/the-one-chat' },
						{ label: 'The monitor and its levers', slug: 'watch/the-monitor' },
						{ label: 'The crew and the Analyzer', slug: 'watch/the-crew-and-the-analyzer' },
					],
				},
				{
					label: 'Reference',
					items: [
						{ label: 'The HTTP doors', slug: 'reference/http-api' },
						{ label: 'Configuration — the dials', slug: 'reference/configuration' },
						{ label: 'The crew — templates and bindings', slug: 'reference/the-crew' },
						{ label: 'Tools and levers', slug: 'reference/tools-and-levers' },
						{ label: 'Facts, watches and health checks', slug: 'reference/facts-watches-checks' },
						{ label: 'The contracts', slug: 'reference/contracts' },
					],
				},
				// The sidebar only ever lists pages that exist.
			],
		}),
	],
});
