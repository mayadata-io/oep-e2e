""" This script contains all the constants """
import os

#baseUrl = "https://director.mayadata.io/v3"
BASE_URL = os.environ.get('BASEURL') + "/v3"
print("Director url:",BASE_URL)

# Credential provider id
GCP_ID = "1bp3"
AWS_ID = "1bp1"

# organization
PROJECTS_URL = f"{BASE_URL}/organizations"

# subscription
SUBSCRIPTIONS_URL = f"{BASE_URL}/subscriptions"
CLUSTER_SUBSCRIPTION_URL = f"{BASE_URL}/clusters/clusterId/subscriptions"

#groups
GROUPS_URL = f"{BASE_URL}/groups/"

# cluster 
CLUSTERS_URL = f"{BASE_URL}/clusters"
CLUSTER_IMPORT_LIST = ["name", "organizationId", "k8sServerConfig", "provider"]
CLUSTER_IMPORT_DATA = dict.fromkeys(CLUSTER_IMPORT_LIST, "default")
CLUSTER_UPGRADE_LIST = ["accountId", "clusterId", "kind", "organizationId"]
CLUSTER_UPGRADE_DATA = dict.fromkeys(CLUSTER_UPGRADE_LIST, "default")

#credential
CREDENTIALS_URL = f'{BASE_URL}/providercredentials/'
CREDENTIALS_LIST = ["name", "organizationId", "providerId", "credential"]
CREDENTIALS_Dict = dict.fromkeys(CREDENTIALS_LIST, "default")

# maya-apps
MAYA_APPS_URL = f"{BASE_URL}/groups/groupId/mayaapplications"

# schedule
SCHEDULES_URL = f"{BASE_URL}/dmaasschedules"
SCHEDULE_LIST = ["applicationId", "clusterId", "credentialId", "name", "organizationId", "scheduleInterval", "transferType", "region"]
SCHEDULE_DICT = dict.fromkeys(SCHEDULE_LIST, "default")

#restore
RESTORE_URL = f"{BASE_URL}/dmaasjobs/"
RESTORE_LIST = ['backupName', 'dstClusterId', 'organizationId']
RESTORE_DICT = dict.fromkeys(RESTORE_LIST, "default")


