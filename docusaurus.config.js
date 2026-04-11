// @ts-check

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'OSE SRD',
  tagline: 'Tradução do Old-School Essentials SRD',
  favicon: 'img/ose_logo_white.png',

  url: 'https://ose-srd.netlify.app',
  baseUrl: '/',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'throw',

  // Portuguese-only site: sets <html lang>, date formats, theme translations.
  i18n: {
    defaultLocale: 'pt-BR',
    locales: ['pt-BR'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          path: 'content',
          routeBasePath: '/',
          sidebarPath: './sidebars.js',
          // numberPrefixParser: false keeps URLs like /classes/1-anao instead
          // of stripping the "1-" prefix. Sidebar ordering is handled by
          // _category_.json + the numeric prefix on filenames via the default
          // parser replaced here — we fall back to an identity parser that
          // still extracts the prefix as a sidebar sort weight.
          numberPrefixParser: (filename) => {
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
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
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
    }),
};

module.exports = config;
