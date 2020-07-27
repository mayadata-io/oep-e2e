module.exports = {
	someSidebar: {
		Overview: ['getstarted', 'platforms', 'testbed', 'pipelines', 'compatibility'],
		Director: [
			{
				type: 'category',
				label: 'Install and Upgrade',
				items: [
					'director/installation/installation',
					'director/installation/TCID-DIR-INSTALL-ON-LOCAL-HP'
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
					'director/authentication/TCID-GUI-AUTH',
					'director/authentication/TCID-GUI-CLUSTER',
					'director/authentication/TCID-GUI-DASHBOARD',
					'director/authentication/TCID-GUI-PROFILE',
					'director/authentication/TCID-DIR-AUTH-LOCAL-ADMIN',
					'director/authentication/TCID-DIR-AUTH-LOCAL-USER',
					'director/authentication/TCID-DIR-AUTH-LOCAL-PERF',
				],
			},
			{
				type: 'category',
				label: 'Teaming',
				items: [
					'director/teaming/directorTeaming',
					'director/teaming/TCID-DIR-TEAMING-USER-INVITE',
					'director/teaming/TCID-DIR-TEAMING-USER-ROLE-UPDATE',
					'director/teaming/TCID-DIR-TEAMING-USER-ROLE-UPDATE-NEGATIVE'
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
					'director/openebs-provisioning/TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-NO-NDM',
					'director/openebs-provisioning/TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-STRIPE',
					'director/openebs-provisioning/TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-RAIDZ',
					'director/openebs-provisioning/TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-RAIDZ',
					'director/openebs-provisioning/TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-STRIPE',
					'director/openebs-provisioning/TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-MIRROR',
					'director/openebs-provisioning/TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-MIRROR',
					'director/openebs-provisioning/TCID-DIR-OP-INSTALL-OPENEBS',
					'director/openebs-provisioning/TCID-DIR-OP-INSTALL-OPENEBS-CP-ON-SPECIFIC-NODE',
					'director/openebs-provisioning/TCID-DIR-OP-INSTALL-OPENEBS-DP-ON-SPECIFIC-NODE',
					'director/openebs-provisioning/TCID-DIR-OP-INSTALL-OPENEBS-LIMIT-RESOURCE',
					'director/openebs-provisioning/TCID-DIR-OP-RE-INSTALL-OPENEBS',
					'director/openebs-provisioning/TCID-DIR-GUI-OPENEBS-COMPONENTS-VERSION',
					'director/openebs-provisioning/TCID-DIR-OP-DELETE-SPC-WITH-NO-VOLUME',
					'director/openebs-provisioning/TCID-DIR-OP-DELETE-CSPC-WITH-NO-VOLUME'


				],
			},
			{
				type: 'category',
				label: 'DMaaS',
				items: [
					'director/dmaas/dmaas',
					'director/dmaas/TCID-DIR-DMAAS-SCHD-CSTOR-AWS-BUCKET',
					'director/dmaas/TCID-DIR-DMAAS-SCHD-CSTOR-MINIO-BUCKET',
					'director/dmaas/TCID-DIR-DMAAS-SCHD-JIVA-AWS-BUCKET',
					'director/dmaas/TCID-DIR-DMAAS-SCHD-JIVA-MINIO-BUCKET',
					'director/dmaas/TCID-DIR-DMAAS-SCHD-LOCAL-DEV-AWS-BUCKET',
					'director/dmaas/TCID-DIR-DMAAS-SCHD-LOCAL-DEV-MINIO-BUCKET',
					'director/dmaas/TCID-DIR-DMAAS-SCHD-LOCAL-HP-AWS-BUCKET',
					'director/dmaas/TCID-DIR-DMAAS-SCHD-LOCAL-HP-MINIO-BUCKET',
					'director/dmaas/TCID-DIR-DMAAS-MINIO-DELETE',
					'director/dmaas/TCID-DIR-DMAAS-CSTOR-NON-RESTIC'
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
			{
				type: 'category',
				label: 'OpenEBS Functional',
				items: [
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-CSTOR-CLONE-CREATE',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-CSTOR-SNAPSHOT-CREATE',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-CSTOR-VOLUME-EXT4-RESIZE',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-CSTOR-VOLUME-XFS-RESIZE',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-JIVA-APP-TARGET-AFFINITY',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-JIVA-SNAPSHOT-CREATE',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-JIVA-VOLUME-SCALEUP',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-LOCALPV-HOSTPATH-CREATE',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-LOCALPV-RANDOM-DEVICE-CREATE',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-LOCALPV-SELECTED-DEVICE-CREATE',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-ZFS-LOCALPV-PROVISIONER-DEPLOY',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-ZFS-VOL-RESIZE-ZFS',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-ZFS-VOL-RESIZE-EXT4',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-ZFS-VOL-RESIZE-XFS',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-ZFSPV-CUSTOM-TOPOLOGY-VERIFY',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-ZFSPV-SNAPSHOT-CLONE-ZFS-CREATE',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-ZFSPV-SNAPSHOT-CLONE-XFS-CREATE',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-ZFSPV-SNAPSHOT-CLONE-EXT4-CREATE',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-ZFSPV-PROPERTY-MODIFY-ZFS',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-ZFSPV-PROPERTY-MODIFY-XFS',
					'openebs-enterprise/OPENEBS-FUNCTIONAL/TCID-ZFSPV-PROPERTY-MODIFY-EXT4',
				],
			},
			{
				type: 'category',
				label: 'OpenEBS Chaos',
				items: [
					'openebs-enterprise/OPENEBS-CHAOS/TCID-JIVA-BUSYBOX-KILL',
					'openebs-enterprise/OPENEBS-CHAOS/TCID-JIVA-MULTIPLE-REPLICAS-FAILURE',
					'openebs-enterprise/OPENEBS-CHAOS/TCID-JIVA-REPLICA-NETWORK-DELAY',
					'openebs-enterprise/OPENEBS-CHAOS/TCID-JIVA-CONTROLLER-KILL',
					'openebs-enterprise/OPENEBS-CHAOS/TCID-JIVA-CONTROLLER-NETWORK-DELAY',
					'openebs-enterprise/OPENEBS-CHAOS/TCID-JIVA-REPLICA-NODE-AFFINITY',
					'openebs-enterprise/OPENEBS-CHAOS/TCID-CSTOR-BUSYBOX-APP-KILL',
					'openebs-enterprise/OPENEBS-CHAOS/TCID-CSTOR-TARGET-KILL'
				],
			},
		],
        "Release Notes": [
            'kubera-e2e-release-1-10', 
            'kubera-e2e-release-1-11', 
        ],
        "Manual Testing": [
            'manual/kubera-authentication', 
        ],
        Help: ['doc1', 'mdx'],
	},
};
