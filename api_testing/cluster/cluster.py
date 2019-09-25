#!/usr/bin/env python

""" This module has cluster-specific methods  """
import re
import sys
import subprocess
from config import *
from api_request.request import *

class cluster:
    data = {}
    url = ''
    name = ''
    id = ''
    
    def __init__(self, nameInit):
        self.nameInit = nameInit
        self.setData()

    def setData(self):
        """ searches for cluster and sets cluster properties if it exists so that ohter methods don't need to send get requests """
        clusterList = getRequest(clustersUrl)
        for dict in clusterList:
            if re.match(self.nameInit, dict["name"]):
                cluster.data = dict
                cluster.id = self.data['id']
                cluster.url = clustersUrl + '/' + self.id
                cluster.name = self.data["name"]
              
    def isExist(self):
        if self.name != '':
            return True
        else:
            print(f"Cluster {self.nameInit} not found!")
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
        clusterImportData["name"] = self.nameInit
        clusterImportData["organizationId"] = organizationId
        clusterImportData["k8sServerConfig"] = "null"   
        clusterImportData["provider"] = "default" 
        # post-request to create cluster
        response = postRequest(clustersUrl, clusterImportData)
        # if response is valid set cluster properties
        if response:
            cluster.id = response['id']
            cluster.url = clustersUrl + '/' + self.id
            cluster.name = response['name']
            print(f"Cluster {self.nameInit} created..Let's connect the cluster")
            return True

    def deployMaya(self): 
        if self.isExist():
            listOfNamespaces = str(subprocess.check_output("kubectl get ns -o jsonpath='{.items[*].metadata.name}'",shell=True),'utf-8')
            mayaNamespace = 'maya-system'
            if mayaNamespace not in listOfNamespaces: 
                cluster.data = getRequest(self.url)
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
            clusterUpgrageData["accountId"] = self.getCreatorId()
            clusterUpgrageData["clusterId"] = self.id
            clusterUpgrageData["kind"] = "evaluation"
            clusterUpgrageData["organizationId"] = self.getOrganizationId()
            if postRequest(subscriptionsUrl, clusterUpgrageData):
                print("Cluster Upgraded")
                return True
            else:
                print("Cluster not upgraded")
        else:
            print("Cannot upgrade! Cluster not active")
        
    def checkSubscription(self):
        if self.isExist():
            checkSubscriptionUrl = f"https://director.mayadata.io/v3/clusters/{self.id}/subscriptions"
            SubscriptionList = getRequest(checkSubscriptionUrl)
            if len(SubscriptionList) != 0:
                return(SubscriptionList[0]['kind'])
                
    def getProjectId(self): 
        """ checks if cluster exists to fetch project id from project-name and cluster id """ 
        if self.isExist():
            projectList = getRequest(projectsUrl)
            if projectList:
                for dict in projectList:
                    if dict['name'] == 'Default' and dict['clusterId'] == self.id:
                        projectId = dict['id']
                        return(projectId)

    def getCreatorId(self):
        if self.isExist():
            return(self.data['creatorId'])
         
    def getState(self):
        if self.isExist():
            state = getRequest(self.url)['state']
            return(state)
       
    def isActive(self):
        if self.getState() == 'active':
            return True

    def getId(self):
        if self.isExist():
            return(self.data['id'])   
      
    def getOrganizationId(self):
        if self.isExist():
            return(self.data['organizationId']) 
      