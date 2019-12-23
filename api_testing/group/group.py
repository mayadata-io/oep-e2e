#!/usr/bin/env python

""" director account specific methods """

from api_request.request import *
from config import *

class Groups():
    data = {}

    def __init__(self, director_url, api_key, api_password):
        # configobj = Config(director_url, api_key, api_password)
        # self.base_url = configobj.GROUPS_URL
        base_url = director_url + "/v3"
        GROUPS_URL = f"{base_url}/groups"
        self.base_url = GROUPS_URL
        # Data request object initialize
        requestobj = Data(api_key, api_password) 
        self.request = requestobj  
        # setter method 
        self.setData()
        
    def setData(self):
        groupsList = self.request.get(self.base_url)
        if len(groupsList) != 0:
            dict = groupsList[0] 
            Groups.data = dict
         
    def isExist(self): 
        return(bool(self.data))
         
    def getUrl(self):
        if getId() != None:
            url = self.baseUrl + '/' + self.getId()
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
            
          
            
        