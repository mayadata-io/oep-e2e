#!/usr/bin/env python

""" This module has cluster-specific methods  """
import re
import sys
import subprocess
from config import *
from api_request.request import *
#from test import *

class Cluster(Data):
    data = {}
    url = ''
    name = ''
    id = ''
    
    def __init__(self, nameInit):
        requestUrl = ''
        Data.__init__(self, requestUrl)
        self.nameInit = nameInit
        self.setData()

    def setData(self):
        """ searches for cluster and sets cluster properties if it exists so that ohter methods don't need to send get requests """
        self.requestUrl = CLUSTERS_URL
        clusterList = self.get()
        for dict in clusterList:
            if re.match(self.nameInit, dict["name"]):
                Cluster.data = dict
                Cluster.id = self.data['id']
                Cluster.url = CLUSTERS_URL + '/' + self.id
                Cluster.name = self.data["name"]
              
    def isExist(self):
        if self.name != '':
            return True
        else:
            return False

    def isValid(self):
        """ this method checks validity of cluster specified by user """
        if len(self.nameInit) < 6:
                print("Min length of cluster:6!! Try again")
        elif len(self.nameInit) >24:
            print("Max length of cluster:24!! Try again")
        elif self.isExist():
            print("Cluster with the same name already exists! Try with some other name")
        else:
            return True

    def create(self, organizationId):
        print("Creating cluster..") 
        # set post-request data
        CLUSTER_IMPORT_DATA["name"] = self.nameInit
        CLUSTER_IMPORT_DATA["organizationId"] = organizationId
        CLUSTER_IMPORT_DATA["k8sServerConfig"] = "null"   
        CLUSTER_IMPORT_DATA["provider"] = "default" 
        # post-request to create cluster
        self.requestUrl = CLUSTERS_URL
        response = self.post(CLUSTER_IMPORT_DATA)
        # if response is valid set cluster properties
        if response:
            Cluster.id = response['id']
            Cluster.url = CLUSTERS_URL + '/' + self.id
            Cluster.name = response['name']
            print(f"Cluster {self.nameInit} created..Let's connect the cluster")
            return True

    def deployMaya(self): 
        if self.isExist():
            listOfNamespaces = str(subprocess.check_output("kubectl get ns -o jsonpath='{.items[*].metadata.name}'",shell=True),'utf-8')
            mayaNamespace = 'maya-system'
            if mayaNamespace not in listOfNamespaces: 
                self.requestUrl = self.url
                Cluster.data = self.get()
                yamlApply = self.data['registrationToken']['clusterCommand']
                if yamlApply != None:
                    os.system(yamlApply)
                    print(f"Cluster {self.nameInit} is connecting...")
                    return True
                else:
                    print("Kubernetes yaml file not present")
            else:
                print("Namespace maya-system already exists! Clean-up required")                    
    
    def upgrade(self):
        """ checks if cluster is active and sets cluster upgrade post-request data and upgrades the cluster"""
        if self.isActive():
            CLUSTER_UPGRADE_DATA["accountId"] = self.getCreatorId()
            CLUSTER_UPGRADE_DATA["clusterId"] = self.id
            CLUSTER_UPGRADE_DATA["kind"] = "evaluation"
            CLUSTER_UPGRADE_DATA["organizationId"] = self.getProjectId()
            self.requestUrl = SUBSCRIPTIONS_URL
            if self.post(CLUSTER_UPGRADE_DATA):
                print("Cluster Upgraded")
                return True
            else:
                print("Cluster not upgraded")
        else:
            print("Cannot upgrade! Cluster not active")
            return False
    
    def checkSubscription(self):
        if self.isExist():
            subscriptionUrl = f"{BASE_URL}/clusters/{self.id}/subscriptions"
            self.requestUrl = subscriptionUrl
            SubscriptionList = self.get()
            if len(SubscriptionList) != 0:
                return(SubscriptionList[0]['kind'])
            else:
                print("Cluster is not on the evaluation or premium mode!")
                return False
                
    def getGroupId(self): 
        """ checks if cluster exists to fetch project id from project-name and cluster id """ 
        if self.isExist():
            self.requestUrl = GROUPS_URL
            groupList = self.get()
            if groupList:
                for dict in groupList:
                    if dict['name'] == 'Default' and dict['clusterId'] == self.id:
                        groupId = dict['id']
                        return(groupId)

    def getCreatorId(self):
        if self.isExist():
            return(self.data['creatorId'])
         
    def getState(self):
        if self.isExist():
            self.requestUrl = self.url
            data = self.get()
            state = data['state']
            return(state)
       
    def isActive(self):
        if self.getState() == 'active':
            return True
        else:
            return False

    def getId(self):
        if self.isExist():
            return(self.data['id'])   
    
    def getProjectId(self):
        if self.isExist():
            return(self.data['organizationId']) 
