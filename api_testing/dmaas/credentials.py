import json
import base64
from config import *
from account.account import *
from api_request.request import *

class Credential(Data):
    data = {}
    url = ''
    id = ''
    
    def __init__(self, name, provider):
        self.name = name
        self.provider = provider
        requestUrl = ''
        Data.__init__(self, requestUrl)
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
        self.requestUrl = CREDENTIALS_URL
        credentialsList = self.get()
        for cred in credentialsList:
            if cred['name'] == self.name and cred['providerId'] == providerId:
                Credential.url = cred['links']['self']
                Credential.data = cred
                Credential.id = cred['id']
                return True
        print(f"Credential {self.name} does not exists!")

    def getId(self):
        if self.url != '':
            return(self.data['id'])
        else:
            print(f"Credential {self.name} does not exists!")

    def aws(self):
        awsPath = os.environ.get('AWSPATH', 'Not Set')
        if os.path.exists(awsPath):
            with open(awsPath) as json_file:
                credential = json.load(json_file)
                return credential
        else:
            print("AWS credentials file does not exist in the path provided!!")
    
    def gcp(self):
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
        accountobj = Account()
        providerDict = {"gcp" : "1bp2", "aws" : "1bp1"}
        if self.provider == "aws":
            credential = self.aws()
        elif self.provider == "gcp":
            credential = self.gcp()
        providerId = providerDict[self.provider]
        CREDENTIALS_Dict["name"] = self.name
        CREDENTIALS_Dict["organizationId"] = accountobj.getProjectID()
        CREDENTIALS_Dict["providerId"] = providerId
        CREDENTIALS_Dict["credential"] = credential
        credentialsData = json.dumps(CREDENTIALS_Dict)
        self.requestUrl = CREDENTIALS_URL
        response = self.post(credentialsData)
        if response:
            print(f"Credential {self.name} is created!!")
            Credential.url = CREDENTIALS_URL + response['id']
    
