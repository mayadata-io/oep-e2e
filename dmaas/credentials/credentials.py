import os
import json
import sys
import base64
sys.path.append("..")
from config import *
from api_request.request import *

def getOrgID():
    organizationsDict = getRequest(organizationsUrl)
    # assuming there is only one organization for now
    organizationsList = organizationsDict['data']
    for dict in organizationsList:
        organizationId = dict['id']
        return(organizationId)

def isExistingCredential(credentialName):
    credentialsDict = getRequest(credentialsUrl)
    credentialList = credentialsDict['data']
    for dict in credentialList:
        if dict['name'] == credentialName:
                return True

def getCredentialId(credentialName):
    credentialsDict = getRequest(credentialsUrl)
    credentialList = credentialsDict['data']
    for dict in credentialList:
        if dict['name'] == credentialName:
            return(dict['id'])
            
def setData(credentialName, providerId, credential):
    credentialsDict["name"] = credentialName
    credentialsDict["organizationId"] = getOrgID()
    credentialsDict["providerId"] = providerId
    credentialsDict["credential"] = credential
    credentialsData = json.dumps(credentialsDict)
    return(credentialsData)

def credential(credentialName, provider):
    providerDict = {"gcp" : "1bp2", "aws" : "1bp1"}
    
    if provider == "aws":
        awsPath = os.environ.get('AWSPATH', 'Not Set')
        if os.path.exists(awsPath):
            with open(awsPath) as json_file:
                credential = json.load(json_file)
        else:
            print("AWS credentials file does not exist in the path provided!!")
    if provider == "gcp":
        gcpPath = os.environ.get('GCPPATH', 'Not Set')
        if os.path.exists(gcpPath):
            with open(gcpPath) as json_file:
                credential = json.load(json_file)
                credential = json.dumps(credential)
                credential = base64.b64encode(credential.encode('utf-8'))
                credential = str(credential, 'utf-8')
                credential = {"gcloud_credential":credential}
        else:
            print("GCP credentials file does not exist in the path provided!!")


    providerId = providerDict[provider]
    
    credentialsData = setData(credentialName, providerId, credential)
    return(postRequest(credentialsUrl, credentialsData))  
