import json
import base64
from config import *
from api_request.request import *

def getOrgID():
        organizationsDict = getRequest(organizationsUrl)
        # assuming there is only one organization for now
        organizationsList = organizationsDict['data']
        for dict in organizationsList:
            organizationId = dict['id']
            return(organizationId)

class credential:
    data = {}
    url = ''
    id = ''
    def __init__(self, credentialName, provider):
        self.name = credentialName
        self.provider = provider
        self.isExist()

    def isValid(self):
        if len(self.name) < 3:
            print("Min length of schedule:3!! Try again")
        elif len(self.name) > 24:
            print("Max length of schedule:24!! Try again")
        else:
            return True

    def isExist(self):
        providerDict = {"gcp" : "1bp2", "aws" : "1bp1"}
        providerId = providerDict[self.provider]
        credentialList = getRequest(credentialsUrl)
        for cred in credentialList:
            if cred['name'] == self.name and cred['providerId'] == providerId:
                credential.url = cred['links']['self']
                credential.data = cred
                credential.id = cred['id']
                return True
        print(f"Credential {self.name} does not exists!")

    def getId(self):
        if self.url != '':
            return(self.data['id'])
        else:
            print(f"Credential {self.name} does not exists!")

    def awsCredential(self):
        awsPath = os.environ.get('AWSPATH', 'Not Set')
        if os.path.exists(awsPath):
            with open(awsPath) as json_file:
                credential = json.load(json_file)
                return credential
        else:
            print("AWS credentials file does not exist in the path provided!!")
    
    def gcpCredential(self):
        gcpPath = os.environ.get('GCPPATH', 'Not Set')
        if os.path.exists(gcpPath):
            with open(gcpPath) as json_file:
                credential = json.load(json_file)
                credential = json.dumps(credential)
                credential = base64.b64encode(credential.encode('utf-8'))
                credential = str(credential, 'utf-8')
                credential = {"gcloud_credential":credential}
                return credential
        else:
            print("GCP credentials file does not exist in the path provided!!")
                
    def create(self):
        providerDict = {"gcp" : "1bp2", "aws" : "1bp1"}

        if self.provider == "aws":
            credential = self.awsCredential()

        if self.provider == "gcp":
            credential = self.gcpCredential()

        providerId = providerDict[self.provider]
        credentialsDict["name"] = self.name
        credentialsDict["organizationId"] = getOrgID()
        credentialsDict["providerId"] = providerId
        credentialsDict["credential"] = credential
        credentialsData = json.dumps(credentialsDict)
        self.url = credentialsUrl + postRequest(credentialsUrl, credentialsData)['id']
        return(self.url)  
