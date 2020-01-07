#!/usr/bin/env python

""" This module contains api requests methods """
import os   
import sys
import requests
import json
from http import HTTPStatus

class Data():

    def __init__(self, username, password):
        auth_api_key = username
        auth_password = password
        auth = (auth_api_key, auth_password)
        self.auth = auth
     
    def get(self, url):
        """ sends get request and returns response data """
        try:
            response = requests.get(url, auth=self.auth)
        except requests.exceptions.RequestException as e:
            print(e)
            requests.exceptions.ConnectionError
            sys.exit(1)
        if response.status_code == HTTPStatus.OK:
            responseDict = json.loads(response.content.decode('utf-8'))
            return(responseDict["data"])
        else:
            print(response.status_code, response.reason)
            sys.exit(1)
          
    def getByCookie(self, url, cookie):
        """ sends get request and returns response data """
        try:
            response = requests.get(url, cookies = cookie)
        except requests.exceptions.RequestException as e:
            print(e)
            requests.exceptions.ConnectionError
            sys.exit(1)
        if response.status_code == HTTPStatus.OK:
            responseDict = json.loads(response.content.decode('utf-8'))
            return(responseDict)
        else:
            print(response.status_code, response.reason)
            sys.exit(1)

    def getById(self, url):
        """ sends get request and returns response data """
        try:
            response = requests.get(url, auth=self.auth)
        except requests.exceptions.RequestException as e:
            print(e)
            requests.exceptions.ConnectionError
            sys.exit(1)
        if response.status_code == HTTPStatus.OK:
            responseDict = json.loads(response.content.decode('utf-8'))
            return responseDict
        else:
            print(response.status_code, response.reason)
            sys.exit(1)
          
    def post(self, url, data):
        """ sends post request and returns response data """     
        try:
            response = requests.post(url, data=data, auth=self.auth)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        responseDict = json.loads(response.content.decode('utf-8'))
        if response.status_code == HTTPStatus.CREATED or response.status_code == HTTPStatus.OK:
            return(responseDict)
        else:
            print(response.status_code, response.reason)
            print("Error!",responseDict['message'])
            sys.exit(1)
           
    def delete(self, url):
        """ sends delete request """
        try:
            response = requests.delete(url, auth=self.auth)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        if response.status_code != HTTPStatus.OK:
            print(response.status_code, response.reason)
        else:
            sys.exit(1)
     
        

