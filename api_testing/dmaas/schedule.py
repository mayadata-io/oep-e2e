from mayapps import *
from config import *
from account.account import *
from api_request.request import *
from cluster.cluster import *
from credentials import *
from mayapps.mayapps import *

class Schedule(Data):
    data = {}
    url = ''
    id = ''

    def __init__(self, name):
        self.name = name
        requestUrl = ''
        Data.__init__(self, requestUrl)
        self.setData()

    def setData(self):
        """ sets schedule properties if it exists so that ohter methods don't need to send get requests """ 
        self.requestUrl = SCHEDULES_URL
        schedulesList = self.get()
        for dict in schedulesList:
            if dict["name"] == self.name:
                Schedule.data = dict
                Schedule.id = self.data['id']
                Schedule.scheduleUrl = self.data['links']['self']
                return True
    
    def isExist(self):
        if self.id != '':
            return True
        else:
            return False

    def isActive(self):
        state = self.data['state']
        if state == "active":
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
        dict = self.preValidation(args)
        if dict:
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
            self.requestUrl = self.url
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
        clusterobj = Cluster(clusterNameInit)
        
        if clusterobj.isExist() and not self.isExist():
            groupId = clusterobj.getGroupId()
            maya = Mayapps(groupId, deployment, namespace)    
            credentialobj = Credential(credentialName, provider)
            accountobj = Account()
            """ sets validation conditions """
            conditions = [
                    clusterobj.isActive(),
                    clusterobj.checkSubscription(),
                    credentialobj.isExist(),
                    maya.isExist()
                    ]   
            """ performing checks """
            check_status = "pass"
            
            for condition in conditions:
                if not condition: 
                    check_status = "fail"
                    
            if check_status == "pass":
                dict = {"applicationId":maya.id,
                "clusterId" : clusterobj.id,
                "credentialId" : credentialobj.id,
                "organizationId":accountobj.getProjectID(),
                "url":maya.url,
                "region":region
                }
                return dict
        else:
            print("Cluster not found!")
