#!/usr/bin/env python

""" Maya application specific methods """

import sys
from config import *
from api_request.request import *
from cluster.cluster import *

class mayapps:
    url = ''
    id = ''
    data = {}
    
    def __init__(self, projectId, deployment, namespace):
        self.deployment = deployment
        self.namespace = namespace
        self.projectId = projectId
        self.setData()

    def makeAppUrl(self):
        mayaAppUrl = mayaAppsUrl.replace("projectId", self.projectId)
        return(mayaAppUrl)

    def isExist(self):
        if self.id:
            return True
        
    def setData(self):
        """ sets maya-apps properties if it exists so that ohter methods don't need to send get requests """ 
        mayaAppUrl = self.makeAppUrl()
        if mayaAppUrl:
            mayaAppsList = getRequest(mayaAppUrl)
            for dict in mayaAppsList:
                mayaAppDict = dict
                if mayaAppDict['name'] == self.deployment and mayaAppDict['data']['namespace'] == self.namespace:
                    #print("Maya application exists!")
                    mayapps.data = mayaAppDict
                    mayapps.url = self.data['links']['self']
                    mayapps.id = self.data['id']
                    return True
            #print("Maya application does not exists!")
    