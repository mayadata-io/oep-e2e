#!/usr/bin/env python
import sys
from config import *
from api_request.request import *
from cluster.cluster import *
sys.path.append("..")
from cluster.cluster import *


# requires clusternameinit for clusterid -> for projectid -> to create mayaappurl 
# -> get ns and deploy to find app

def getmayaAppId(clusterNameInit, deploymentName, namespace):
    mayaAppUrl = makeAppUrl(clusterNameInit)
    #print(mayaAppUrl)
    mayaAppList = isExistingNamespace(clusterNameInit, deploymentName, namespace)
    if mayaAppList:
        mayaAppId = mayaAppList['id']
        #print("app found with id:", mayaAppId)
        return(mayaAppUrl, mayaAppId)
    

def makeAppUrl(clusterNameInit):
    clusterId = getClusterId(clusterNameInit)
    projectId = getProjectId(clusterId)
    mayaAppUrl = mayaAppsUrl.replace("projectId", projectId)
    return(mayaAppUrl)
            
def isExistingNamespace(clusterNameInit, deployment, namespace):
    mayaAppsList = isExistingDeployment(clusterNameInit, deployment)
    if mayaAppsList:
        if mayaAppsList['data']['namespace'] == namespace:
            return mayaAppsList
        print(f"namespace {namespace} in deployment {deployment} does not exist")
   
def isExistingDeployment(clusterNameInit, deployment):
    mayaAppUrl = makeAppUrl(clusterNameInit)
    mayaAppsDict = getRequest(mayaAppUrl)
    mayaAppsList = mayaAppsDict['data']
    for dict in mayaAppsList:
        mayaAppList = dict
        if mayaAppList['name'] == deployment:
            return(mayaAppList)     
    print(f"deployment: {deployment} does not exist")
   

