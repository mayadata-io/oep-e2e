#!/usr/bin/env python

""" This module contains api requests methods """
import os   
import sys
import requests
import json
from http import HTTPStatus

class Data():

    def __init__(self, url):
        #echo api_key | base64 --decode
        self.request_url = url
        auth_api_key = os.environ.get('USERNAME')
        auth_password = os.environ.get('PASSWORD')
        auth = (auth_api_key, auth_password)
        self.auth = auth
     
    def get(self):
        """ sends get request and returns response data """
        try:
            response = requests.get(self.request_url, auth=self.auth)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
            requests.exceptions.ConnectionError
        if response.status_code == HTTPStatus.OK:
            responseDict = json.loads(response.content.decode('utf-8'))
            keys = list(responseDict.keys())
            return(responseDict['data'])
        else:
            print(response.status_code, response.reason)
            sys.exit(1)

     
    def getById(self):
        """ sends get request and returns response data """
        try:
            response = requests.get(self.request_url, auth=self.auth)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
            requests.exceptions.ConnectionError
        if response.status_code == HTTPStatus.OK:
            responseDict = json.loads(response.content.decode('utf-8'))
            keys = list(responseDict.keys())
            return responseDict
        else:
            print(response.status_code, response.reason)
            sys.exit(1)    
    
    def post(self, data):
        """ sends post request and returns response data """     
        try:
            response = requests.post(self.request_url, data=data, auth=self.auth)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        responseDict = json.loads(response.content.decode('utf-8'))
        if response.status_code == HTTPStatus.CREATED:
            return(responseDict)
        else:
            print(response.status_code, response.reason)
            print("Error!",responseDict['message'])
            sys.exit(1)

    def delete(self):
        """ sends delete request """
        try:
            response = requests.delete(self.request_url, auth=self.auth)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        if response.status_code != HTTPStatus.OK:
            print(response.status_code, response.reason)
            sys.exit(1)

        
