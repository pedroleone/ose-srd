const config = {
  gatsby: {
    pathPrefix: '/',
    siteUrl: 'https://hasura.io',
    gaTrackingId: null,
    trailingSlash: false,
  },
  header: {
    logo: './images/ose_logo_white.png',
    logoLink: '/',
    title: 'OSE SRD',
    githubUrl: '',
    helpUrl: '',
    tweetText: '',
    social: '',
    links: [{ text: '', link: '' }],
    search: {
      enabled: false,
      indexName: '',
      algoliaAppId: process.env.GATSBY_ALGOLIA_APP_ID,
      algoliaSearchKey: process.env.GATSBY_ALGOLIA_SEARCH_KEY,
      algoliaAdminKey: process.env.ALGOLIA_ADMIN_KEY,
    },
  },
  sidebar: {
    forcedNavOrder: [
      '/personagens',
      '/classes',
      '/equipamentos',
      '/magias',
      //'/introduction', // add trailing slash if enabled above

    ],
    collapsedNav: [
      //'/personagens', // add trailing slash if enabled above
    ],
    links: [{ text: 'Old School Essentials SRD', link: 'https://oldschoolessentials.necroticgnome.com/srd/index.php/Main_Page' }],
    frontline: false,
    ignoreIndex: true,
    title:
      "",
  },
  siteMetadata: {
    title: 'OSE SRD',
    description: 'Tradução do Old School Essentials SRD ',
    ogImage: null,
    docsLocation: '',
    favicon: null,
  },
  pwa: {
    enabled: false, // disabling this will also remove the existing service worker.
    manifest: {
      name: 'Gatsby Gitbook Starter',
      short_name: 'GitbookStarter',
      start_url: '/',
      background_color: '#6b37bf',
      theme_color: '#6b37bf',
      display: 'standalone',
      crossOrigin: 'use-credentials',
      icons: [
        {
          src: 'src/pwa-512.png',
          sizes: `512x512`,
          type: `image/png`,
        },
      ],
    },
  },
};

module.exports = config;
