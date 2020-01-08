#!/usr/bin/env python

""" This module has api-key-specific methods  """

import argparse
from api_request.request import *

class UNIQUE_ID():
    def __init__(self, director_url):
        self.base_url = director_url + "/v3" + "/settings/websocketproxy.unique.identity"
        requestobj = Data('', '') 
        self.request = requestobj
    
    def getId(self, jwt):
        url = self.base_url
        cookie = {'token': jwt,'authProvider': 'localAuthConfig'}
        response = self.request.getByCookie(url, cookie) 
        id = response['value']
        print(id)
       
def main():  
    parser = argparse.ArgumentParser()
    parser.add_argument("--url",
            help="director onprem url")
    parser.add_argument("--token",
            help="token")
    args = parser.parse_args()
    director_url = args.url
    token = args.token
    api_key_obj = UNIQUE_ID(director_url)
    api_key_obj.getId(token)

    
if __name__ == '__main__':
    main()