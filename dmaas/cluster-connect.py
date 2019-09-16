#!/usr/bin/env python

import requests
import argparse
import os
import sys
import time
import subprocess
import threading
from tqdm import trange
from config import *
from api_request.request import *
from cluster.cluster import *

def getOrgID():
    organizationsDict = getRequest(organizationsUrl)
    # assuming there is only one organization for now
    organizationsList = organizationsDict['data']
    for dict in organizationsList:
        organizationId = dict['id']
        return(organizationId) 

def isExistingNamespace(func):
    def wrapper():
        listOfNamespaces = str(subprocess.check_output("kubectl get ns -o jsonpath='{.items[*].metadata.name}'",shell=True),'utf-8')
        if 'maya-system' in listOfNamespaces:
            print("Namespace maya-system already exists! Clean-up required")
        else:
            func()
    return wrapper

@isExistingNamespace  
def clusterConnect():     
        clusterName = getClusterName(clusterNameInit)
        clustersDict = getRequest(clustersUrl)
        clusterList = clustersDict['data']
        for dict in clusterList:
            if dict['name'] == clusterName:
                clusterDict = dict
                yamlApply = clusterDict['registrationToken']['clusterCommand']
                if yamlApply != None:
                    os.system(yamlApply)
                    print(f"Cluster {clusterNameInit} is connecting...")
                    upgradeCluster()
                else:
                    print("yaml file not present")

state=["inactive"]

def checkClusterState():
    while getClusterState(clusterNameInit) != "active":
            time.sleep(0.2)
    state[0]="active"
             

def waitForActiveCluster(func):
    def wrapper():
        print(f"Waiting for the cluster {clusterNameInit} to be active...", end="")
        x = threading.Thread(target=checkClusterState)
        x.start()
        blah="\|/-\|/-"
        while state[0] != "active":
            for l in blah:
                sys.stdout.write(l)
                sys.stdout.flush()
                sys.stdout.write('\b')
                time.sleep(0.2)
        print()   
        print("Cluster is active! Let's upgrade")
        func()
    return wrapper

@waitForActiveCluster 
def upgradeCluster():
    clusterName = getClusterName(clusterNameInit)
    plan = "evaluation"
    clusterUpgrageData["accountId"] = getCreatorId(clusterName)
    clusterUpgrageData["clusterId"] = getClusterId(clusterName)
    clusterUpgrageData["kind"] = plan
    clusterUpgrageData["organizationId"] = getOrganizationId(clusterName)
    
    for i in trange(10000000, desc='Upgrading cluster'):
        pass

    if postRequest(subscriptionsUrl, clusterUpgrageData):
        print("Cluster Upgraded")
    else:
        print("Cluster not upgraded")

def calculateTime(func):
    def wrapper(*args, **kwargs):
        # storing time before function execution 
        begin = time.time()
        func(*args, **kwargs)
        # storing time after function execution 
        end = time.time() 
        print(f"Total time taken in : {end-begin} secs") 
    return wrapper

def createCluster(func):
    def wrapper(*args, **kwargs):
        print("Creating cluster..") 
        clusterImportData = func(*args, **kwargs)
        if postRequest(clustersUrl, clusterImportData):
            print(f"Cluster {clusterNameInit} created..Let's connect the cluster")
            clusterConnect()
    return wrapper

@calculateTime
@createCluster
def setData(organizationId):
    clusterImportData["name"] = clusterNameInit
    clusterImportData["organizationId"] = organizationId
    clusterImportData["k8sServerConfig"] = "null"
    clusterImportData["provider"] = "default"
    return clusterImportData

def isClusterValid():
    if len(clusterNameInit) < 6:
        print("Min length of cluster:6!! Try again")
    elif len(clusterNameInit) >24:
         print("Max length of cluster:24!! Try again")
    elif isExisitngCluster(clusterNameInit):
        print("Cluster with the same name already exists! Try with some other name")
    else:
        return True

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--cluster_name",
            help="cluster name minLength: 6,maxLength: 24")
    
    args = parser.parse_args()

    global clusterNameInit 
    clusterNameInit = args.cluster_name
     
    if isClusterValid():
        organizationId = getOrgID()
        setData(organizationId)

if __name__ == '__main__':
    main()

