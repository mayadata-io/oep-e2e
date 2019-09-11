#cluster data
clusterImportList = ["name", "organizationId", "k8sServerConfig", "provider"]
clusterImportData = dict.fromkeys(clusterImportList, "default")
clusterUpgrageList = ["accountId", "clusterId", "kind", "organizationId"]
clusterUpgrageData = dict.fromkeys(clusterUpgrageList, "default")
# credentials data
credentialsList = ["name", "organizationId", "providerId", "credential"]
credentialsDict = dict.fromkeys(credentialsList, "default")
# schedule data
scheduleList = ["applicationId", "clusterId", "credentialId", "name", "organizationId", "scheduleInterval", "transferType", "region"]
scheduleDict = dict.fromkeys(scheduleList, "default")
