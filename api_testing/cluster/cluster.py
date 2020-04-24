#!/usr/bin/env python

""" This module has cluster-specific methods  """
import re
import sys
import time
import subprocess
from config import *
from project.project import *
from api_request.request import *

class Cluster():
    data = {}
    id = ''
   
    def __init__(self, nameInit, director_url, api_key, api_password):
        # cluster name provided by the user
        self.nameInit = nameInit
        # get cluster base_url and post request data fields from Config module
        configobj = Config(director_url, api_key, api_password)
        self.base_url = configobj.CLUSTERS_URL  
        self.connect_data = configobj.CLUSTER_CONNECT_DATA
        # request
        requestobj = Data(api_key, api_password) 
        self.request = requestobj
        # get projectid from Projects modules
        projectsobj = Projects(director_url, api_key, api_password)
        self.projectId = projectsobj.getId()
        # setter method
        self.setData()   
        
    def setData(self):
        """ searches for cluster and sets cluster properties if it exists so that other methods don't need to send get requests """
        url = self.base_url
        clusterList = self.request.get(url)
        for dict in clusterList:
            if re.match(self.nameInit, dict["name"]):
                Cluster.data = dict
            
    def isValid(self):
        """ this method checks length of cluster name specified by user """
        min_length = 6
        max_length = 24
        cluster_name_length = len(self.nameInit)
        if len(self.nameInit) < min_length:
            print(f"Length of cluster name given {cluster_name_length}, min length expected is {min_length}. Try again")
        elif len(self.nameInit) > max_length:
            print(f"Length of cluster name given {cluster_name_length}, max length expected is {max_length}. Try again")
        else:
            return True

    def create(self, provider):
        print("Creating cluster..")
        # set post-request data
        self.connect_data["name"] = self.nameInit
        self.connect_data["projectId"] = self.projectId  
        #self.connect_data["k8sServerConfig"] = "null" 
        self.connect_data["provider"] = provider
        # post-request to create cluster
        url = self.base_url
        response = self.request.post(url, self.connect_data)
        Cluster.data = response
       
    def isMayaNamespaceExist(self):
        namespace_cmd = "kubectl get ns -o jsonpath='{.items[*].metadata.name}'"
        namespaceList = str(subprocess.check_output(namespace_cmd, shell=True),'utf-8')
        mayaNamespace = 'maya-system'
        if mayaNamespace in namespaceList: 
            return True
        else:
            return False
    
    def preConnect(self, provider):
        self.create(provider) 
        if self.isMayaNamespaceExist():
            print("Namespace maya-system already exists. Clean-up required")   
            if not self.cleanup():
                print("Namespace maya-system not getting deleted")
                sys.exit(1)
            
    def connect(self, provider): 
        """ creates cluster and checks if setup is clean then deploys kuberentes yaml """
        self.preConnect(provider)
        url = self.getUrl()
        print("Cluster url:",url)
        Cluster.data = self.request.getById(url)
        while self.data['state'] != 'inactive' and self.data['state'] != 'active':
            Cluster.data = self.request.getById(url)
            time.sleep(5)
        # check until cluster is inactive, if it is it should have yaml
        yamlApply = self.data['registrationToken']['clusterCommand']
        if yamlApply != None:
            os.system(yamlApply)
            print(f"Cluster {self.nameInit} is connecting...")
            # wait for cluster to be Active
            timer = 3
            total_time = 0
            while not self.isActive():
                if total_time >= 180:
                    print("Cluster is not getting Active. Something is wrong")
                    sys.exit(1)
                time.sleep(timer)
                total_time += timer        
            print(f"Cluter {self.nameInit} is active now")
            return True
        else:
            print("Kubernetes yaml file not present. Cluster connection failed.")
            return False
    
    def getState(self):
        if self.isExist():
            # request api to fetch state
            url = self.getUrl()
            data = self.request.getById(url)
            state = data['state']
            return(state)
        else:
            print(f"{self.nameInit} does not exist")
            return None
            
    def isActive(self):
        state = self.getState()
        if state == 'active':
            return True
        else:
            return False

    def cleanup(self):
        print("Starting cleanup...")
        print("Deleting maya-system namespace...")
        delete_maya = "kubectl delete ns maya-system"
        os.system(delete_maya)
        if not self.isMayaNamespaceExist():
            print("Cleanup done")
            return True
        else:
            return False
        
    def isExist(self):
        return(bool(self.data))
         
    def getUrl(self):
        if self.getId() != None:
            url = self.base_url + '/' + self.getId()
            return(url)
        else:
            print("Cannot get url as Id is None")
            return None

    def getId(self):
        if self.isExist():
            return(self.data['id'])  
        else:
            print(f"{self.nameInit} does not exist")
            return None
         
    def remove(self):
        if self.isExist():
            self.request.delete()
            print(f"{self.nameInit} deleted")
            return True
        else:
            print(f"{self.nameInit} does not exist")
            return False