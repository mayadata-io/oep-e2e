#!/usr/bin/env python

""" This script connects cluster to mayaonline/dop   """

import argparse
import time
import sys
import subprocess
from account.account import *
from config import *
from api_request.request import *
from cluster import *

def waitAndUpgrade(clusterobj, plan):
    print("Waiting for the cluster to be active...", end="")
    while not clusterobj.isActive():
        time.sleep(20)  
    print("Cluster is active! Let's upgrade")
    # wait for sometime after cluster is active to upgrade
    time.sleep(20)
    if clusterobj.upgrade():
        return True
 
def waitForDMaaSAgents(clusterobj):
    print("Waiting for the DMaaS Agents to come up")
    timer = 60
    total_time = 0
    while not clusterobj.isDMaaSAgents():
        if total_time >= 540:
            print("DMaaS agents not coming up!! Something is wrong!")
            sys.exit(1)
        if total_time >= 240:
            timer = 0.2
        time.sleep(timer)
        total_time += timer        
    time_in_mins = round(total_time/60)
    print("DMaaS agents deployed!!")
    print(f"Time taken for the DMaaS to come up {time_in_mins} minutes")

def calculateTime(func):
    """ this is a decorator method which calculates time of connect cluster """
    def wrapper(*args):
        # storing time before function execution 
        begin = time.time()
        if func(*args):
            print("Connected and upgraded the cluster...")
            # storing time after function execution 
            end = time.time() 
            print(f"Total time taken in connecting cluster: {end-begin} secs") 
            return True    
    return wrapper

@calculateTime
def connectCluster(clusterobj, organizationId, provider, plan):
    """ creates, deploys and upgrade cluster """
    if clusterobj.create(organizationId, provider):
        if clusterobj.connect():
            if clusterobj.checkSubscription != plan:
                if waitAndUpgrade(clusterobj, plan):
                    return True
    
def main():  
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--cluster_name",
            required=True,
            help="cluster name minLength: 6,maxLength: 24")
    parser.add_argument("--provider",
            help="cluster provider")
    parser.add_argument("--subscription-plan",
            default="evaluation",
            help="subscription plan")
    args = parser.parse_args()
    clusterNameInit = args.cluster_name
    provider = args.provider
    plan = args.subscription_plan
    provider = args.provider
    clusterobj = Cluster(clusterNameInit)
    accountobj = Account()

    organizationId = accountobj.getProjectID()
    if organizationId:
        if clusterobj.isValid():
            if connectCluster(clusterobj, organizationId, provider, plan):
                waitForDMaaSAgents(clusterobj)
        else:
            sys.exit(1)
    else:
        print("No organization present!")
        sys.exit(1)
   
if __name__ == '__main__':
    main()
