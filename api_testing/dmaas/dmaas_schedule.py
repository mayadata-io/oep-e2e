from config import *
from account.user_account import *
from api_request.request import *
from cluster.cluster import *
from cloud_credentials import *
from apps.cluster_apps import *

class DMaaSchedule(Data):
    data = {}
    url = ''
    id = ''

    def __init__(self, clusterName, name):
        self.name = name
        self.clusterName = clusterName
        request_url = ''
        Data.__init__(self, request_url)
        self.setData()

    def setData(self):
        """ sets schedule properties if it exists so that ohter methods don't need to send get requests """ 
        cluster = Cluster(self.clusterName)
        self.request_url = SCHEDULES_URL.replace("clusterId", cluster.id)
        schedulesList = self.getById()
        for dict in schedulesList:
            if dict["name"] == self.name:
                Schedule.data = dict
                Schedule.id = self.data['id']
                Schedule.url = self.data['links']['self']
                self.request_url = self.url
                return True
    
    def isExist(self):
        if self.id != '':
            return True
        else:
            return False

    def getState(self):
        if self.isExist():
            self.request_url = self.url
            data = self.getById()
            state = data['state']
            return(state)

    def isActive(self):
        state = self.getState()
        if state == 'active':
            return True
        elif state == "stopped":
            return False

    def isValid(self):
        if len(self.name) < 3:
            print("Min length of schedule:3!! Try again")
        elif len(self.name) > 24:
            print("Max length of schedule:24!! Try again")
        else:
            return True

    def create(self, args):
        """ sets post-request data and sends the request to create schedule """
        credentialName = args["credential_name"]
        provider = args["provider"]
        clusterNameInit = args["cluster_name"]
        deployment = args["deployment"]
        namespace = args["namespace"]
        region = args["region"]
        cluster = Cluster(clusterNameInit)
        apps = ClusterApps(clusterNameInit, deployment, namespace)    
        credential = CloudCredential(credentialName, provider)
        account = UserAccount()
        dict = {"applicationId":apps.id,
                "clusterId" : cluster.id,
                "credentialId" : credential.id,
                "organizationId":account.getProjectID(),
                "url":apps.url,
                "region":region
                }
        SCHEDULE_DICT["applicationId"] = dict["applicationId"]
        SCHEDULE_DICT["clusterId"] = dict["clusterId"]
        SCHEDULE_DICT["credentialId"] = dict["credentialId"]
        SCHEDULE_DICT["name"] = self.name
        SCHEDULE_DICT["organizationId"] = dict["organizationId"]
        SCHEDULE_DICT["scheduleInterval"] = "*/02 * * * *"
        SCHEDULE_DICT["transferType"] = 1 
        SCHEDULE_DICT["region"] = dict["region"]
        Schedule.url = dict["url"] + "/dmaasschedules"
        print("DMaaS schedule URl:", self.url)
        self.request_url = self.url
        response = self.post(SCHEDULE_DICT)
        if response:
            Schedule.data = response
            Schedule.id = self.data['id']
            Schedule.url = self.data['links']['self']
        print(f"DMaaS schedule {self.name} created!")
            
    def preValidation(self, args):
        credentialName = args["credential_name"]
        provider = args["provider"]
        clusterNameInit = args["cluster_name"]
        deployment = args["deployment"]
        namespace = args["namespace"]
        region = args["region"]
        cluster = Cluster(clusterNameInit)
        
        if cluster.isExist(): 
            apps = ClusterApps(clusterNameInit, deployment, namespace)    
            credential = CloudCredential(credentialName, provider)
            account = UserAccount()
            """ sets validation conditions """
            conditions = [
                    cluster.isActive(),
                    credential.isExist(),
                    apps.isExist()
                    ]   
            """ performing checks """
            check_status = "pass"
            
            for condition in conditions:
                if not condition: 
                    check_status = "fail"
                    
            if check_status == "pass":
               return True
            else:
                return False
        else:
            print("Cluster not found!")
            return False
    