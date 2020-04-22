module.exports = {
  someSidebar: {
    Overview: ['getstarted', 'platforms', 'testbed', 'pipelines'],
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
				'director/teaming/TC-Team-InviteUser',
				'director/teaming/TC-Team-RoleChange',
				'director/teaming/TC-Team-RoleChange-Negative'
			],
		},
		{
		        type: 'category',
		        label: 'OpenEBS Provisioning',
		        items: [
                		'director/openebs-provisioning/plan',
		                'director/openebs-provisioning/TCID-DIR-OP-BD-VIEW-ALL',
                		'director/openebs-provisioning/TCID-DIR-OP-BD-VIEW-SCALE',
		                'director/openebs-provisioning/TCID-DIR-OP-BD-VIEW-SCALE-RESTART',
                		'director/openebs-provisioning/TCID-DIR-OP-BD-FILTER-SSD',
		                'director/openebs-provisioning/TCID-DIR-OP-BD-FILTER-PATH',
                		'director/openebs-provisioning/TCID-DIR-OP-BD-IGNORE',
		                'director/openebs-provisioning/TCID-DIR-OP-BD-VIEW-TOGGLE',
                		'director/openebs-provisioning/TCID-DIR-OP-CSP-REC-LIST',
		                'director/openebs-provisioning/TCID-DIR-OP-CSP-REC-LIST-NO-NDM',
                		'director/openebs-provisioning/TCID-DIR-OP-CSP-REC-LIST-STRIPE',
		                'director/openebs-provisioning/TCID-DIR-OP-CSP-REC-CREATE-STRIPE',
                		'director/openebs-provisioning/TCID-DIR-OP-CSP-REC-LIST-MIRROR',
		                'director/openebs-provisioning/TCID-DIR-OP-CSP-REC-CREATE-MIRROR'
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
