#!/usr/bin/env python

""" This module contains api requests methods """
import os   
import requests
from status_codes import *
import json

class Data(statusCodes):

    def __init__(self, url):
        self.requestUrl = url
        auth_api_key = os.environ.get('USERNAME')
        auth_password = os.environ.get('PASSWORD')
        auth = (auth_api_key, auth_password)
        self.auth = auth
     
    def get(self):
        """ sends request and returns response data """
        response = requests.get(self.requestUrl, auth=self.auth)
        if response.status_code == self.OK:
            responseDict = json.loads(response.content.decode('utf-8'))
            # code is fetching data from a list like /clusters endpoint so it have multiple `data` fields for various clusters
            # but when code is fething data from specific endpoint like cluster/specific_cluster_id 
            # thn it doesnt have data field in it 
            # code below is checking the same
            keys = list(responseDict.keys())
            if 'data' not in keys:
                return responseDict
            else:
                return(responseDict['data'])
        else:
            print(response.status_code, response.reason)
             
    def post(self, data):
        """ sends request and returns response data """
        response = requests.post(self.requestUrl, data=data, auth=self.auth)
        responseDict = json.loads(response.content.decode('utf-8'))
        if response.status_code == self.CREATED:
            return(responseDict)
        else:
            print(response.status_code, response.reason)
            print("Error!",responseDict['message'])
        
