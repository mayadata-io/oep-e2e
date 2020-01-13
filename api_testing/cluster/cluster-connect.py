#!/usr/bin/env python

""" This script connects cluster to director onprem  """
import argparse
import time
import sys
import subprocess
from config import *
from api_request.request import *
from cluster import *
from project.project import *

def calculateTime(func):
    """ this is a decorator method which calculates time of connect cluster """
    def wrapper(*args):
        # storing time before function execution 
        begin = time.time()
        if func(*args):
            print("Cluster is active now...")
            # storing time after function execution 
            end = time.time() 
            print(f"Total time taken in connecting cluster: {end-begin} secs") 
            return True    
    return wrapper

@calculateTime
def connectCluster(clusterobj, provider):
    """ creates, deploys and upgrade cluster """
    if clusterobj.connect(provider):
        return True
    else:
        return False
        
def main():  
    parser = argparse.ArgumentParser()
    parser.add_argument("--cluster_name",
            required=True,
            help="cluster name minLength: 6,maxLength: 24")
    parser.add_argument("--provider",
            help="cluster provider")
    parser.add_argument("--url",
            help="director onprem url")
    parser.add_argument("--username",
            help="director api key")
    parser.add_argument("--password",
            help="director api password")
    args = parser.parse_args()
    clusterNameInit = args.cluster_name
    provider = args.provider
    director_url = args.url
    api_key = args.username
    api_password = args.password
    clusterobj = Cluster(clusterNameInit, director_url, api_key, api_password)
    if clusterobj.isValid():
        if clusterobj.isActive():
            print(clusterobj.getId())
        else:
            print("Connecting cluster...")
            if connectCluster(clusterobj, provider):
                print("Cluster connected")
            else:
                print("Cluster not connected")
                sys.exit(1)
    else:
        print("Cluster name is not valid")
        sys.exit(1)
    
if __name__ == '__main__':
    main()
