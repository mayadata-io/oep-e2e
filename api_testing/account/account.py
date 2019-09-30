#!/usr/bin/env python

""" director account specific methods """

from api_request.request import *
from config import *

class Account(Data):
    def __init__(self):
        requestUrl = ''
        Data.__init__(self, requestUrl)

    def getProjectID(self):
        self.requestUrl = PROJECTS_URL
        projectsList = self.get()
        # assuming there is only one organization for now
        if len(projectsList) != 0:
            for dict in projectsList:
                projectId = dict['id']
                return(projectId) 

