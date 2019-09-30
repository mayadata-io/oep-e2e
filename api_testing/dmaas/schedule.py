from mayapps import *
from config import *
from account import *
from api_request.request import *
from cluster.cluster import *
from dmaas.credentials import *
from mayapps.mayapps import *

class schedule:
    data = {}
    url = ''
    id = ''

    def __init__(self, name):
        self.name = name
        self.setData()

    def setData(self):
        """ sets schedule properties if it exists so that ohter methods don't need to send get requests """ 
        schedulesList = getRequest(schedulesUrl)
        for dict in schedulesList:
            if dict["name"] == self.name:
                schedule.data = dict
                schedule.id = self.data['id']
                schedule.scheduleUrl = self.data['links']['self']
                return True
    
    def isExist(self):
        if self.url != '':
            return True
        else:
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
            scheduleDict["applicationId"] = dict["applicationId"]
            scheduleDict["clusterId"] = dict["clusterId"]
            scheduleDict["credentialId"] = dict["credentialId"]
            scheduleDict["name"] = self.name
            scheduleDict["organizationId"] = dict["organizationId"]
            scheduleDict["scheduleInterval"] = "*/02 * * * *"
            scheduleDict["transferType"] = 1 
            scheduleDict["region"] = dict["region"]
            schedule.url = dict["url"] + "/dmaasschedules"
            print("DMaaS schedule URl:", schedule.url)
            response = postRequest(schedule.url, scheduleDict)
            if response:
                schedule.data = response
                schedule.id = self.data['id']
                schedule.url = self.data['links']['self']
            print(f"Cluster {self.name} created..Let's connect the cluster")
            
    def preValidation(self, args):
        credentialName = args["credential_name"]
        provider = args["provider"]
        clusterNameInit = args["cluster_name"]
        deployment = args["deployment"]
        namespace = args["namespace"]
        region = args["region"]
        clusterobj = cluster(clusterNameInit)
        
        if clusterobj.isExist() and not self.isExist():
            projectId = clusterobj.getProjectId()
            maya = mayapps(projectId, deployment, namespace)    
            credentialobj = credential(credentialName, provider)
            accountobj = account()

            """ sets validation conditions """
            conditions = {
                clusterobj.isActive():"Cluster not active!",
                clusterobj.checkSubscription():"Cluster is not on the evaluation or premium mode!",
                credentialobj.isExist():"Credential not found!",
                maya.isExist():"Maya Apps not found!"
                }
        
            """ performing checks """
            check_status = "pass"
            
            for condition in conditions:
                if not condition: 
                    check_status = "fail"
                    print(conditions[condition])

            if check_status == "pass":
                dict = {"applicationId":maya.id,
                "clusterId" : clusterobj.id,
                "credentialId" : credentialobj.id,
                "organizationId":accountobj.getOrganizationID(),
                "url":maya.url
                }
                print(dict)
                return dict
               
        else:
            print("Cluster not found!")
