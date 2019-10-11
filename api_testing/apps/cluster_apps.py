#!/usr/bin/env python

""" Maya application specific methods """

import sys
from config import *
from api_request.request import *
from cluster.cluster import *

class ClusterApps(Data):
    url = ''
    id = ''
    data = {}
    
    def __init__(self, clusterNameInit, name, namespace):
        # deployment name if the application
        self.name = name
        # namespace of the application
        self.namespace = namespace
        # source cluster name from where maya app is backedup
        self.clusterName = clusterNameInit
        # initializing request_url for inherited Data class
        request_url = ''
        Data.__init__(self, request_url)
        self.setData()

    def makeAppUrl(self):
        """ returns maya-applications endpoint inside source cluster """
        cluster = Cluster(self.clusterName)
        groupId = cluster.getGroupId()
        if groupId:
            mayaAppsUrl = MAYA_APPS_URL.replace("groupId", groupId)
            return(mayaAppsUrl)
        else:
            return False

    def isExist(self):
        """ checks if maya-application exist """
        if self.id:
            return True
        else:
            print(f"Application {self.name} not found!")
            return False
            
    def setData(self):
        """ sets maya-apps properties if it exists so that ohter methods don't need to send api requests """ 
        mayaAppsUrl = self.makeAppUrl()
        if mayaAppsUrl:
            self.request_url = mayaAppsUrl
            mayaAppsList = self.getById()
            for dict in mayaAppsList:
                mayaAppDict = dict
                if mayaAppDict['name'] == self.name and mayaAppDict['data']['namespace'] == self.namespace:
                    #print("Maya application exists!")
                    Mayapps.data = mayaAppDict
                    Mayapps.url = self.data['links']['self']
                    Mayapps.id = self.data['id']
                    return True
            #print("Maya application does not exists!")
    