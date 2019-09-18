baseUrl = "https://director.mayadata.io/v3"

# organization
organizationsUrl = f"{baseUrl}/organizations"

# subscription
subscriptionsUrl = f"{baseUrl}/subscriptions"

#credential
credentialsUrl = f'{baseUrl}/providercredentials/'
credentialsList = ["name", "organizationId", "providerId", "credential"]
credentialsDict = dict.fromkeys(credentialsList, "default")

#project
projectsUrl = f"{baseUrl}/projects/"

# cluster 
clustersUrl = f"{baseUrl}/clusters"
clusterImportList = ["name", "organizationId", "k8sServerConfig", "provider"]
clusterImportData = dict.fromkeys(clusterImportList, "default")
clusterUpgrageList = ["accountId", "clusterId", "kind", "organizationId"]
clusterUpgrageData = dict.fromkeys(clusterUpgrageList, "default")

# maya-apps
mayaAppsUrl = f"{baseUrl}/projects/projectId/mayaapplications"

# schedule
schedulesUrl = f"{baseUrl}/projects/projectId/mayaapplications/mayaAppID/dmaasschedules"
scheduleList = ["applicationId", "clusterId", "credentialId", "name", "organizationId", "scheduleInterval", "transferType", "region"]
scheduleDict = dict.fromkeys(scheduleList, "default")







