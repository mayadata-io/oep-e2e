#!/usr/bin/env python

""" This script connects cluster to mayaonline/dop   """

import argparse
import time
import subprocess
from account import *
from config import *
from api_request.request import *
from cluster import *

def waitForActiveCluster(clusterobj, plan):
    print(f"Waiting for the cluster to be active...", end="")
    while not clusterobj.isActive():
        print(clusterobj.isActive())
        time.sleep(0.2)  
    print("Cluster is active! Let's upgrade")
    # wait for sometime after cluster is active to upgrade
    time.sleep(20)
    clusterobj.upgrade()    
 
def calculateTime(func):
    """ this is a decorator method which calculates time of connect cluster """
    def wrapper(*args):
        # storing time before function execution 
        begin = time.time()
        func(*args)
        # storing time after function execution 
        end = time.time() 
        print(f"Total time taken in : {end-begin} secs") 
    return wrapper

@calculateTime
def connectCluster(clusterobj, organizationId, plan):
    """ creates, deploys and upgrade cluster """
    if clusterobj.create(organizationId):
        if clusterobj.deployMaya():
            if clusterobj.checkSubscription != plan:
                waitForActiveCluster(clusterobj, plan)
    
def main():  
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--cluster_name",
            required=True,
            help="cluster name minLength: 6,maxLength: 24")
    parser.add_argument("--subscription-plan",
            default="evaluation",
            help="cluster name minLength: 6,maxLength: 24")
    args = parser.parse_args()
    clusterNameInit = args.cluster_name
    plan = args.subscription_plan
    clusterobj = cluster(clusterNameInit)
    accountobj = account()

    if clusterobj.isValid():
        organizationId = accountobj.getOrganizationID()
        connectCluster(clusterobj, organizationId, plan)

if __name__ == '__main__':
    main()
