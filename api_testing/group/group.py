""" director account specific methods """

import argparse
from api_request.request import *

class Groups():
    projectAccData = {}

    def __init__(self, director_url, api_key, api_password):
        # configobj = Config(director_url, api_key, api_password)
        # self.base_url = configobj.GROUPS_URL
        self.director_url = director_url
        base_url = director_url + "/v3"
        GROUPS_URL = f"{base_url}/groups"
        self.base_url = GROUPS_URL
        # Data request object initialize
        requestobj = Data(api_key, api_password) 
        self.request = requestobj  
      
    def setProjectAccountDataIfExists(self):
        groupsList = self.request.get(self.base_url)
        account = "ProjectAccount"
        for dict in groupsList:
            if account == dict["name"]:
                Groups.projectAccData = dict
                return Groups.projectAccData
        print("Project Account does not exist")
        return None
        
    def setClusterAccountDataIfExists(self):
        groupsList = self.request.get(self.base_url)
        account = "ClusterAccount"
        #cluster_id = id
        for dict in groupsList:
            #if account == dict["name"] and cluster_id == dict['clusterId']:
            if account == dict["name"]:
                clusterAccData = dict
                return clusterAccData
        print(f"Cluster Account does not exist")
        return None

    def getMayaApps(self, acc):
        if acc == "ClusterAccount":
            account_data = self.setClusterAccountDataIfExists()
        elif acc == "ProjectAccount":
            account_data = self.setProjectAccountDataIfExists()
        if account_data != None:
            apps_api_endpoint = account_data['links']['mayaApplications']
            apps_data = self.request.get(apps_api_endpoint)
            for app_data in apps_data:
                print(app_data['name'])
        else:
            print("Data is None")
        
    def getMayaStoragePools(self, acc):
        if acc == "ClusterAccount":
            account_data = self.setClusterAccountDataIfExists()
        elif acc == "ProjectAccount":
            account_data = self.setProjectAccountDataIfExists()
        if account_data != None:
            apps_pool_endpoint = account_data['links']['mayaStoragePools']
            pools_data = self.request.get(apps_pool_endpoint)
            for pool_data in pools_data:
                print(pool_data['data']['pods'][0]['name'])
        else:
            print("Data is None")
        
    def getProjectAccountID(self):
        data = self.setProjectAccountDataIfExists()
        if data:
            return self.projectAccData['id']
        else:
            return None

    def getProjectOwner(self):
        id = self.getProjectAccountID()
        url = self.base_url + f"/{id}/groupmembers"
        groupMembersList = self.request.get(url)
        for member in groupMembersList:
            role = member['role']
            if role == 'ProjectOwner':
                return member['id']

    def searchMemberByEmailID(self, email_id):
        member_emailId = email_id
        print(member_emailId)
        project_acc_id = self.getProjectAccountID()
        url = self.base_url + f"/{project_acc_id}/groupmembers/member_id"
        groupMembersList = self.request.get(url)
        for member in groupMembersList:
            if member['accountDetails']['email'] == member_emailId:
                return member

    
    
   
  


   




