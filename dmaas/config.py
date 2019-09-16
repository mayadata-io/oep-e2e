# organization
organizationsUrl = "https://director.mayadata.io/v3/organizations"

# subscription
subscriptionsUrl = "https://director.mayadata.io/v3/subscriptions"

#credential
credentialsUrl = 'https://director.mayadata.io/v3/providercredentials/'
credentialsList = ["name", "organizationId", "providerId", "credential"]
credentialsDict = dict.fromkeys(credentialsList, "default")

#project
projectsUrl = "https://director.mayadata.io/v3/projects/"

# cluster 
clustersUrl = "https://director.mayadata.io/v3/clusters"
clusterImportList = ["name", "organizationId", "k8sServerConfig", "provider"]
clusterImportData = dict.fromkeys(clusterImportList, "default")
clusterUpgrageList = ["accountId", "clusterId", "kind", "organizationId"]
clusterUpgrageData = dict.fromkeys(clusterUpgrageList, "default")

# maya-apps
mayaAppsUrl = "https://director.mayadata.io/v3/projects/projectId/mayaapplications"

# schedule
schedulesUrl = "https://director.mayadata.io/v3/projects/projectId/mayaapplications/mayaAppID/dmaasschedules"
scheduleList = ["applicationId", "clusterId", "credentialId", "name", "organizationId", "scheduleInterval", "transferType", "region"]
scheduleDict = dict.fromkeys(scheduleList, "default")







