#!/usr/bin/env python

""" Maya application specific methods """

import sys
from config import *
from api_request.request import *
from cluster.cluster import *

class Mayapps(Data):
    url = ''
    id = ''
    data = {}
    
    def __init__(self, groupId, deployment, namespace):
        self.deployment = deployment
        self.namespace = namespace
        self.groupId = groupId
        requestUrl = ''
        Data.__init__(self, requestUrl)
        self.setData()

    def makeAppUrl(self):
        mayaAppUrl = MAYA_APPS_URL.replace("groupId", self.groupId)
        return(mayaAppUrl)

    def isExist(self):
        if self.id:
            return True
        else:
            print("Maya Apps not found!")
            
    def setData(self):
        """ sets maya-apps properties if it exists so that ohter methods don't need to send get requests """ 
        mayaAppUrl = self.makeAppUrl()
        if mayaAppUrl:
            self.requestUrl = mayaAppUrl
            mayaAppsList = self.get()
            for dict in mayaAppsList:
                mayaAppDict = dict
                if mayaAppDict['name'] == self.deployment and mayaAppDict['data']['namespace'] == self.namespace:
                    #print("Maya application exists!")
                    Mayapps.data = mayaAppDict
                    Mayapps.url = self.data['links']['self']
                    Mayapps.id = self.data['id']
                    return True
            #print("Maya application does not exists!")
    