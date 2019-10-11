#!/usr/bin/env python

""" director account specific methods """

from api_request.request import *
from config import *

class UserAccount(Data):
    def __init__(self):
        request_url = ''
        Data.__init__(self, request_url)

    def getProjectID(self):
        self.request_url = PROJECTS_URL
        projectsList = self.get()
        # assuming there is only one organization for now
        if len(projectsList) != 0:
            for dict in projectsList:
                projectId = dict['id']
                return(projectId) 

