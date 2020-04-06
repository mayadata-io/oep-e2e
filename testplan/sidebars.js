module.exports = {
  someSidebar: {
    Overview: ['getstarted', 'platforms', 'testbed', 'gitlabstages'],
    Director: [
		{
		        type: 'category',
		        label: 'Install and Upgrade',
		        items: [
				'director/installation/directorInstall',
				'director/installation/tc-install-gpd-std',
				'director/installation/tc-install-ssd-lpv',
				'director/installation/tc-install-gpd-lpv',
				'director/installation/tc-install-ssd-cstor',
				'director/installation/tc-upgrade-gpd-std',
				'director/installation/tc-upgrade-ssd-lpv',
				'director/installation/tc-upgrade-ssd-cstor'
			],
		},
		{
		        type: 'category',
		        label: 'Authentication',
		        items: [
				'director/authentication/directorAuth',
				'director/authentication/tc-auth-la-admin',
				'director/authentication/tc-auth-la-user',
				'director/authentication/tc-auth-la-signup',
				'director/authentication/tc-auth-github-user',
				'director/authentication/tc-auth-github-signup',
				'director/authentication/tc-auth-gmail-user',
				'director/authentication/tc-auth-gmail-signup',
				'director/authentication/tc-auth-ad-user',
				'director/authentication/tc-auth-ad-signup'
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
				'director/openebs/directorOpenEBS',
                'director/openebs/TC-CSP-REC-LIST',
                'director/openebs/TC-CSP-REC-LIST-NO-NDM',
                'director/openebs/TC-CSP-REC-LIST-STRIPE',
                'director/openebs/TC-CSP-REC-CREATE-STRIPE',
                'director/openebs/TC-CSP-REC-LIST-MIRROR',
                'director/openebs/TC-CSP-REC-CREATE-MIRROR'
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
		{
		        type: 'category',
		        label: 'Alerts',
		        items: [
				'director/alerts/alerts',
				'director/alerts/test1'
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
