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
        request_url = ''
        #super(Cluster, self).__init__('')
        Data.__init__(self, request_url)
        self.nameInit = nameInit
        self.setData()

    def setData(self):
        """ searches for cluster and sets cluster properties if it exists so that ohter methods don't need to send get requests """
        self.request_url = CLUSTERS_URL
        clusterList = self.get()
        for dict in clusterList:
            if re.match(self.nameInit, dict["name"]):
                Cluster.data = dict
                Cluster.id = self.data['id']
                Cluster.url = CLUSTERS_URL + '/' + self.id
                Cluster.name = self.data["name"]
                self.request_url = self.url 

    def remove(self):
        if self.isExist():
            self.delete()
            print(f"Cluster {self.name} deleted!!")
        else:
            print("Cluster doesn't exist!")

    def isExist(self):
        if self.name != '':
            return True
        else:
            return False

    def cleanup(self):
        print("Starting cleanup...")
        print("Deleting maya-system namespace...")
        delete_maya = "kubectl delete ns maya-system"
        os.system(delete_maya)

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

    def create(self, organizationId, provider):
        print("Creating cluster..") 
        # set post-request data
        CLUSTER_IMPORT_DATA["name"] = self.nameInit
        CLUSTER_IMPORT_DATA["organizationId"] = organizationId
        CLUSTER_IMPORT_DATA["k8sServerConfig"] = "null"   
        CLUSTER_IMPORT_DATA["provider"] = provider
        # post-request to create cluster
        self.request_url = CLUSTERS_URL
        response = self.post(CLUSTER_IMPORT_DATA)
        # if response is valid set cluster properties
        if response:
            Cluster.id = response['id']
            Cluster.url = CLUSTERS_URL + '/' + self.id
            Cluster.name = response['name']
            print(f"Cluster {self.nameInit} created..Let's connect the cluster")
            return True

    def connect(self): 
        """ checks if cluster exists and setup is clean then deploys kuberentes yaml """
        if self.isExist():
            namespace_cmd = "kubectl get ns -o jsonpath='{.items[*].metadata.name}'"
            namespaceList = str(subprocess.check_output(namespace_cmd, shell=True),'utf-8')
            mayaNamespace = 'maya-system'
            if mayaNamespace in namespaceList: 
                print("Namespace maya-system already exists! Clean-up required")   
                self.cleanup()
            self.request_url = self.url
            Cluster.data = self.getById()
            yamlApply = self.data['registrationToken']['clusterCommand']
            if yamlApply != None:
                os.system(yamlApply)
                print(f"Cluster {self.nameInit} is connecting...")
                return True
            else:
                print("Kubernetes yaml file not present")

    def upgrade(self):
        """ checks if cluster is active and sets cluster upgrade post-request data and upgrades the cluster"""
        if self.isActive():
            CLUSTER_UPGRADE_DATA["accountId"] = self.getCreatorId()
            CLUSTER_UPGRADE_DATA["clusterId"] = self.id
            CLUSTER_UPGRADE_DATA["kind"] = "evaluation"
            CLUSTER_UPGRADE_DATA["organizationId"] = self.getProjectId()
            self.request_url = SUBSCRIPTIONS_URL
            if self.post(CLUSTER_UPGRADE_DATA):
                print("Cluster Upgraded")
                return True
            else:
                print("Cluster not upgraded")
        else:
            print("Cannot upgrade! Cluster not active")
            return False
                
    def getGroupId(self): 
        """ checks if cluster exists to fetch project id from project-name and cluster id """ 
        if self.isExist():
            self.request_url = GROUPS_URL
            groupList = self.get()
            if groupList:
                for dict in groupList:
                    if dict['name'] == 'Default' and dict['clusterId'] == self.id:
                        groupId = dict['id']
                        return(groupId)
        else:
            return False

    def getCreatorId(self):
        if self.isExist():
            return(self.data['creatorId'])
         
    def getState(self):
        if self.isExist():
            self.request_url = self.url
            data = self.getById()
            state = data['state']
            return(state)
       
    def isActive(self):
        if self.getState() == 'active':
            return True
        else:
            print(f"Cluster {self.name} not found!!")
            return False

    def getId(self):
        if self.isExist():
            return(self.data['id'])   
    
    def getProjectId(self):
        if self.isExist():
            return(self.data['organizationId']) 

  
                
    

    

