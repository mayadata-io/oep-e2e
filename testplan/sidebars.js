module.exports = {
  someSidebar: {
    Overview: ['getstarted', 'platforms', 'testbed'],
    Director: [
		{
		        type: 'category',
		        label: 'Install&Upgrade',
		        items: [
				'director/installation/directorinstall',
				'director/installation/install-tcid-1240'
			],
		},
		{
		        type: 'category',
		        label: 'Authentication',
		        items: [
				'director/authentication/directorauth',
				'director/authentication/test1'
			],
		},
		{
		        type: 'category',
		        label: 'Teaming',
		        items: [
				'director/authentication/directorauth',
				'director/authentication/test1'
			],
		},
		{
		        type: 'category',
		        label: 'OpenEBS',
		        items: [
				'director/openebs/summary',
				'director/openebs/test1'
			],
		},
		{
		        type: 'category',
		        label: 'DMaaS',
		        items: [
				'director/dmaas/dmaas',
				'director/dmaas/test1'
			],
		},
    ],
    Help: ['doc1', 'mdx'],
  },
};
