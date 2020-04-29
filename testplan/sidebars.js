module.exports = {
  someSidebar: {
    Overview: ['getstarted', 'platforms', 'testbed', 'pipelines'],
    Director: [
		{
		        type: 'category',
		        label: 'Install and Upgrade',
		        items: [
				'director/installation/installation',
			],
		},
		{
		        type: 'category',
		        label: 'Workflow',
		        items: [
				'director/workflow/onboarding',
				'director/workflow/test1'
			],
		},
		{
		        type: 'category',
		        label: 'Authentication',
		        items: [
				'director/authentication/authentication',
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
				'director/teaming/TC-Team-InviteUser',
				'director/teaming/TC-Team-RoleChange',
				'director/teaming/TC-Team-RoleChange-Negative'
			],
		},
		{
		        type: 'category',
		        label: 'OpenEBS Provisioning',
		        items: [
                		'director/openebs-provisioning/provisioning',
		                'director/openebs-provisioning/TCID-DIR-OP-DEVICE-VIEW-ALL',
                		'director/openebs-provisioning/TCID-DIR-OP-DEVICE-VIEW-SCALE',
		                'director/openebs-provisioning/TCID-DIR-OP-DEVICE-VIEW-SCALE-RESTART',
                		'director/openebs-provisioning/TCID-DIR-OP-DEVICE-FILTER-SSD',
		                'director/openebs-provisioning/TCID-DIR-OP-DEVICE-FILTER-PATH',
                		'director/openebs-provisioning/TCID-DIR-OP-DEVICE-IGNORE',
		                'director/openebs-provisioning/TCID-DIR-OP-DEVICE-VIEW-TOGGLE',
                		'director/openebs-provisioning/TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST',
		                'director/openebs-provisioning/TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-NO-NDM',
                		'director/openebs-provisioning/TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-STRIPE',
		                'director/openebs-provisioning/TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-STRIPE',
                		'director/openebs-provisioning/TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-MIRROR',
		                'director/openebs-provisioning/TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-MIRROR'
			],
		},
		{
		        type: 'category',
		        label: 'DMaaS',
		        items: [
				'director/dmaas/dmaas',
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
			],
		},
    ],
    "OpenEBS Enterprise": [
		{
		        type: 'category',
		        label: 'OpenEBS Enterprise',
		        items: [
				    'openebs-enterprise/openebs/openebs'
			    ],
		},
		{
		        type: 'category',
		        label: 'DAOs',
		        items: [
				    'openebs-enterprise/dao/dao'
			    ],
        	},
    ],	  
    Help: ['doc1', 'mdx'],
  },
};
