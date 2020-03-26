module.exports = {
  someSidebar: {
    Overview: ['getstarted', 'platforms', 'testbed'],
    Director: [
		{
		        type: 'category',
		        label: 'Install and Upgrade',
		        items: [
				'director/installation/directorInstall',
				'director/installation/install-tcid-1240'
			],
		},
		{
		        type: 'category',
		        label: 'Authentication',
		        items: [
				'director/authentication/directorAuth',
				'director/authentication/test1'
			],
		},
		{
		        type: 'category',
		        label: 'Teaming',
		        items: [
				'director/teaming/directorTeaming',
				'director/teaming/test1'
			],
		},
		{
		        type: 'category',
		        label: 'OpenEBS',
		        items: [
				'director/openebs/directorOpenebs',
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
		{
		        type: 'category',
		        label: 'Logging',
		        items: [
				'director/logging/logging',
				'director/logging/test1'
			],
		},
		{
		        type: 'category',
		        label: 'Visualization',
		        items: [
				'director/visualization/visualization',
				'director/visualization/test1'
			],
		},

    ],
    "OpenEBS Enterprise": [
		{
		        type: 'category',
		        label: 'DAO',
		        items: [
				'openebs/dao/dao',
				'openebs/dao/test1'
			],
		},
    ],	  
    Help: ['doc1', 'mdx'],
  },
};
