import json
import base64
from config import *
from account.user_account import *
from api_request.request import *

class CloudCredential(Data):
    data = {}
    url = ''
    id = ''
    
    def __init__(self, name, provider):
        self.name = name
        self.provider = provider
        request_url = ''
        Data.__init__(self, request_url)
        self.setData()

    def isValid(self):
        if len(self.name) < 3:
            print("Min length of schedule:3!! Try again")
        elif len(self.name) > 24:
            print("Max length of schedule:24!! Try again")
        else:
            return True

    def setData(self):
        providerId = self.getProviderId()
        self.request_url = CREDENTIALS_URL
        credentialsList = self.get()
        for cred in credentialsList:
            if cred['name'] == self.name and cred['providerId'] == providerId:
                Credential.data = cred
                Credential.url = self.data['links']['self']
                Credential.id = self.data['id']
          
    def isExist(self):
        if self.id != '':
            return True
        else:
            print(f"Credential {self.name} not found!")
            return False

    def remove(self):
        if self.isExist():
            self.delete()
            print(f"Credential {self.name} deleted!!")
        else:
            print("Credential doesn't exist!")

    def getId(self):
        if self.url != '':
            return(self.data['id'])
        else:
            print(f"Credential {self.name} does not exists!")

    def aws(self):
        #awsPath = os.environ.get('AWSPATH', 'Not Set')
        awsPath = "./credential/aws_auth.json"
        if os.path.exists(awsPath):
            with open(awsPath) as json_file:
                credential = json.load(json_file)
                return credential
        else:
            print("AWS credentials file does not exist in the path provided!!")
    
    def gcp(self):
        #gcpPath = os.environ.get('GCPPATH', 'Not Set')   
        gcpPath = "./credential/gcp_auth.json"
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

    def getProviderId(self):
        if self.provider == "gcp":
            providerId = GCP_ID
        if self.provider == "aws":
            providerId = AWS_ID
        return providerId

    def create(self):
        account = UserAccount()
        if self.provider == "gcp":
            credential = self.gcp()
        if self.provider == "aws":
            credential = self.aws()
        providerId = self.getProviderId()
        CREDENTIALS_Dict["name"] = self.name
        CREDENTIALS_Dict["organizationId"] = account.getProjectID()
        CREDENTIALS_Dict["providerId"] = providerId
        CREDENTIALS_Dict["credential"] = credential
        credentialsData = json.dumps(CREDENTIALS_Dict)
        self.request_url = CREDENTIALS_URL
        response = self.post(credentialsData)
        if response:
            print(f"Credential {self.name} is created!!")
            Credential.url = CREDENTIALS_URL + response['id']
    
