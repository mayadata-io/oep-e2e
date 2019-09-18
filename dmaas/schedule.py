import argparse
import sys
sys.path.append("..")
from credentials.credentials import *
from mayapps.mayapps import *
from config import *
from api_request.request import *
from cluster.cluster import *
    
def isExisitngSchedule(scheduleName, clusterNameInit, deployment, namespace):
    mayaAppUrl, mayaAppId = getmayaAppId(clusterNameInit, deployment, namespace)
    scheduleUrl = mayaAppUrl + f"/{mayaAppId}/dmaasschedules"
    #print(scheduleUrl)
    schedulesDict = getRequest(scheduleUrl)
    schedulesList = schedulesDict['data']
    for dict in schedulesList:
        if dict["name"] == scheduleName:
            return True

def createSchedule(credentialName, scheduleName, provider, region, clusterNameInit, deployment, namespace):
    if isExistingCredential(credentialName, provider):
        print(f"Credential with the name {credentialName} and cloud-provider {provider} exists")
        credentialId = getCredentialId(credentialName)
    else:
        if credential(credentialName, provider):
            credentialId = getCredentialId(credentialName)
            #print(credentialId)
    
    mayaAppUrl, mayaAppId = getmayaAppId(clusterNameInit, deployment, namespace)
    scheduleUrl = mayaAppUrl + f"/{mayaAppId}/dmaasschedules"
    scheduleData = setData(clusterNameInit, scheduleName, credentialId, mayaAppId, region)
    print("DMaaS schedule URl:", scheduleUrl)
    if postRequest(scheduleUrl, scheduleData):
        return True
    

def setData(clusterNameInit, scheduleName, credentialId, mayaAppId, region):  
    scheduleDict["applicationId"] = mayaAppId
    scheduleDict["clusterId"] = getClusterId(clusterNameInit)
    scheduleDict["credentialId"] = credentialId 
    scheduleDict["name"] = scheduleName
    scheduleDict["organizationId"] = getOrgID()
    scheduleDict["scheduleInterval"] = "*/02 * * * *"
    scheduleDict["transferType"] = 1 
    scheduleDict["region"] = region
    return scheduleDict

def isScheduleValid(scheduleName, clusterName, deployment, namespace):
    if len(scheduleName) < 3:
        print("Min length of schedule:3!! Try again")
    elif len(scheduleName) > 24:
        print("Max length of schedule:24!! Try again")
    # elif  isExisitngSchedule(scheduleName, clusterName, deployment, namespace):
    #     print("DMaaS schedule with the same name already exists! Try with some other name")
    else:
        #print("Schedule valid!")
        return True

def isCredentialValid(credentialName):
    if len(credentialName) < 6:
        print("Min length of credential:6!! Try again")
    elif len(credentialName) > 25:
        print("Max length of credential:25!! Try again")
    else:
        return True
  
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--credential_name",
            help="credential name")
    parser.add_argument("--schedule_name",
            help="schedule name minLength: 3,maxLength: 24")
    parser.add_argument("--region",
            help="aws schedule region")
    parser.add_argument("--provider",
            help="cloud provider gcp/aws")
    parser.add_argument("--cluster_name",
            help="cluster name minLength: 6,maxLength: 24")
    parser.add_argument("--deployment",
            help="deployment name of your maya app")
    parser.add_argument("--namespace",
            help="namespace of your maya app")
    
    args = parser.parse_args()
    # deployment = 'minio-deployment'
    # namespace = "minio"
    # "us-east-1"
    
    credentialName = args.credential_name
    scheduleName = args.schedule_name
    provider = args.provider
    clusterNameInit = args.cluster_name
    deployment = args.deployment
    namespace = args.namespace
    region = args.region

    print("Performing Validation checks...")
    if isExisitngCluster(clusterNameInit):
        print("Cluster exists!")
        if isExistingNamespace(clusterNameInit, deployment, namespace):
            print(f"namespace {namespace} in deployment {deployment} exist")
            if isScheduleValid(scheduleName, clusterNameInit, deployment, namespace):
                print("Schedule validation done!")
                if isCredentialValid(credentialName):
                    print("Done with validation checks...")
                    print("Creating DMaaS schedule!")
                    createSchedule(credentialName, scheduleName, provider, region, clusterNameInit, deployment, namespace)
    else:
        print(f"Cluster {clusterNameInit} does not exist.Try again!")    
if __name__ == '__main__':
    main()


