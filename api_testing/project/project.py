#!/usr/bin/env python

""" director account specific methods """

from api_request.request import *
from config import *

class Projects():
    data = {}

    def __init__(self, director_url, api_key, api_password):
        configobj = Config(director_url, api_key, api_password)
        self.base_url = configobj.PROJECTS_URL
        requestobj = Data(api_key, api_password) 
        self.request = requestobj   
        #Data.__init__(self, )
        self.setData()
        
    def setData(self):
        projectsList = self.request.get(self.base_url)
        if len(projectsList) != 0:
            dict = projectsList[0]
            Projects.data = dict

    def isExist(self):
        return(bool(self.data))
         
    def getUrl(self):
        id = self.getId()
        if id != None:
            url = self.base_url + '/' + id
            return(url)

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
            
          
            
        