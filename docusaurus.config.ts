import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'OSE SRD',
  tagline: 'Tradução do Old-School Essentials SRD',
  favicon: 'img/ose_logo_white.png',

  url: 'https://ose-srd.netlify.app',
  baseUrl: '/',

  onBrokenLinks: 'throw',

  // Portuguese-only site: sets <html lang>, date formats, theme translations.
  i18n: {
    defaultLocale: 'pt-BR',
    locales: ['pt-BR'],
  },

  // Markdown hooks: new home in 3.9+ for what used to live at top level
  // (onBrokenMarkdownLinks). The top-level option is deprecated and removed
  // in v4, so we use the hooks object up front.
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'throw',
    },
  },

  // Docusaurus Faster + v4 future flags.
  // `faster: true` enables Rspack + SWC + Lightning CSS + persistent cache
  // + SSG worker threads + MDX cross-compiler cache. Renamed from
  // `experimental_faster` in Docusaurus 3.10 now that the feature graduated.
  // `v4: true` enables all v4 future flags (removeLegacyPostBuildHeadAttribute,
  // useCssCascadeLayers), which is required by ssgWorkerThreads and also
  // front-loads the v4 migration so we don't get surprised later.
  future: {
    v4: true,
    faster: true,
  },

  presets: [
    [
      'classic',
      {
        docs: {
          path: 'content',
          routeBasePath: '/',
          sidebarPath: './sidebars.ts',
          // Keeps URLs like /classes/1-anao instead of stripping the "1-"
          // prefix. Sidebar ordering is handled by _category_.json + the
          // numeric prefix on filenames via the parser below, which still
          // extracts the prefix as a sidebar sort weight.
          numberPrefixParser: (filename: string) => {
            const match = filename.match(/^(\d+)-/);
            return {
              filename,
              numberPrefix: match ? Number(match[1]) : undefined,
            };
          },
          include: ['**/*.md', '**/*.mdx'],
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'OSE SRD',
      logo: {
        alt: 'OSE SRD',
        src: 'img/ose_logo_white.png',
      },
    },
    colorMode: {
      defaultMode: 'light',
      respectPrefersColorScheme: true,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
