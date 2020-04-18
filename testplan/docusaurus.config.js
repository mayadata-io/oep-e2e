module.exports = {
  title: 'OEP E2E',
  tagline: 'E2E testing for OEP',
  url: 'https://ci.mayadata.io',
  baseUrl: '/',
  favicon: 'img/favicon.ico',
  organizationName: 'MayaData', // Usually your GitHub org/user name.
  projectName: 'oep-e2e', // Usually your repo name.
  themeConfig: {
    navbar: {
      title: 'OEP E2E',
      logo: {
        alt: 'MayaData OEP E2E',
        src: 'img/logo.png',
      },
      links: [
        {
          to: 'docs/getstarted',
          activeBasePath: 'docs',
          label: 'Test Plan',
          position: 'left',
        },
        {
          href: 'https://ci.mayadata.io',
          label: 'E2E Pipelines',
          position: 'left',
        },
        {
          href: 'https://github.com/mayadata-io/oep-e2e',
          label: 'OEP-E2E on GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      copyright: `Copyright © ${new Date().getFullYear()} MayaData, Inc.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl:
            'https://github.com/mayadata-io/oep-e2e/edit/master/testplan/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
  stylesheets: [
    `https://fonts.googleapis.com/css2?family=Comfortaa:wght@300;400;500;700`
  ]
};
