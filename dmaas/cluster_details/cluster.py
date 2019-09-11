import re
import sys
from endpoints.url import *
from get.getRequest import *


def isExisitngCluster(clusterNameInit):
    clustersDict = getRequest(clustersUrl)
    clusterList = clustersDict['data']
    for dict in clusterList:
        if re.match(clusterNameInit, dict["name"]):
            return True
            
def getProjectId(clusterId):
    if getRequest(projectsUrl):
        projectsDict = getRequest(projectsUrl)
        projectsList = projectsDict['data']
        for dict in projectsList:
            if dict['name'] == 'Default' and dict['clusterId'] == clusterId:
                projectId = dict['id']
                return(projectId)
            
def getClusterName(clusterNameInit):
    if getRequest(clustersUrl):
        clustersDict = getRequest(clustersUrl)
        clusterList = clustersDict['data']
        for dict in clusterList:
            if re.match(clusterNameInit, dict["name"]):
                return(dict["name"])
        print("Cluster {clusterNameInit} doesn't exists")

def getClusterState(clusterNameInit):
    clusterName = getClusterName(clusterNameInit)
    clustersDict = getRequest(clustersUrl)
    clusterList = clustersDict['data']
    for dict in clusterList:
        if dict["name"] == clusterName:
            return(dict['state'])

def getCreatorId(clusterNameInit):
    clusterName = getClusterName(clusterNameInit)
    clustersDict = getRequest(clustersUrl)
    clusterList = clustersDict['data']
    for dict in clusterList:  
        if dict["name"] == clusterName:
            return(dict['creatorId']) 

def getClusterId(clusterNameInit):
    if getClusterName(clusterNameInit):
        clusterName = getClusterName(clusterNameInit)
        clustersDict = getRequest(clustersUrl)
        clusterList = clustersDict['data']
        for dict in clusterList:  
            if dict["name"] == clusterName:
                return(dict['id'])  
    else: 
        print("Cannot get cluster id, cluster doesn't exists")
         

def getOrganizationId(clusterNameInit):
    clusterName = getClusterName(clusterNameInit)
    clustersDict = getRequest(clustersUrl)
    clusterList = clustersDict['data']
    for dict in clusterList:  
        if dict["name"] == clusterName:
            return(dict['organizationId']) 
