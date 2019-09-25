import os

#baseUrl = "https://director.mayadata.io/v3"
baseUrl = os.environ.get('BASEURL')

# organization
organizationsUrl = f"{baseUrl}/organizations"

# subscription
subscriptionsUrl = f"{baseUrl}/subscriptions"

#project
projectsUrl = f"{baseUrl}/projects/"

# cluster 
clustersUrl = f"{baseUrl}/clusters"
clusterImportList = ["name", "organizationId", "k8sServerConfig", "provider"]
clusterImportData = dict.fromkeys(clusterImportList, "default")
clusterUpgrageList = ["accountId", "clusterId", "kind", "organizationId"]
clusterUpgrageData = dict.fromkeys(clusterUpgrageList, "default")

#credential
credentialsUrl = f'{baseUrl}/providercredentials/'
credentialsList = ["name", "organizationId", "providerId", "credential"]
credentialsDict = dict.fromkeys(credentialsList, "default")

# maya-apps
mayaAppsUrl = f"{baseUrl}/projects/projectId/mayaapplications"

# schedule
schedulesUrl = f"{baseUrl}/dmaasschedules"
scheduleList = ["applicationId", "clusterId", "credentialId", "name", "organizationId", "scheduleInterval", "transferType", "region"]
scheduleDict = dict.fromkeys(scheduleList, "default")


