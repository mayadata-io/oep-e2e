#!/usr/bin/env python

""" This module has api-key-specific methods  """
import argparse
from api_request.request import *
#from config import *

class API_KEY():
    def __init__(self, director_url):
        #configobj = Config(director_url, '', '')
        self.base_url = director_url + "/v3" + "/apikey"
        requestobj = Data('', '') 
        self.request = requestobj
    
    def create(self, jwt):
        url = self.base_url
        data = {'name': 'harshita'}
        cookie = {'token': jwt,'authProvider': 'localAuthConfig'}
        response = self.request.postByCookie(url, data, cookie) 
        username = response['publicValue']
        print(username)
        password = response['secretValue']
        print(password)

def main():  
    parser = argparse.ArgumentParser()
    parser.add_argument("--url",
            help="director onprem url")
    parser.add_argument("--token",
            help="token")
    args = parser.parse_args()
    director_url = args.url
    token = args.token
    api_key_obj = API_KEY(director_url)
    api_key_obj.create(token)

    
if __name__ == '__main__':
    main()
