#!/usr/bin/env python

""" This module contains api requests methods """
import os
import requests
import json

def getRequest(url):
    """ Fetches credentials from envs , sends request and returns response data """
    key = os.environ.get('KEY')
    value = os.environ.get('VALUE')
    auth = (key, value)
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        keys = []
        responseDict = json.loads(response.content.decode('utf-8'))
        for key in responseDict:
            keys.append(key)
        if 'data' not in keys:
            return responseDict
        else:
            return(responseDict['data'])
    else:
        print(response.status_code, response.reason)

def postRequest(url, data):
    """ Fetches credentials from envs , sends request and returns response data """
    key = os.environ.get('KEY')
    value = os.environ.get('VALUE')
    auth = (key, value)
    response = requests.post(url, data=data, auth=auth)
    responseDict = json.loads(response.content.decode('utf-8'))
    if response.status_code == 201:
        return(responseDict)
    else:
        print(response.status_code, response.reason)
        print("Error!",responseDict['message'])
    
