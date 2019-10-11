#!/usr/bin/env python

""" This module has cluster-specific methods  """
import re
import sys
import subprocess
from config import *
from api_request.request import *
from cluster.cluster import *

class ClusterSubscription(Data):
   
    def __init__(self, nameInit):
        request_url = ''
        #super(Cluster, self).__init__('')
        Data.__init__(self, request_url)
        self.nameInit = nameInit
    
    def checkSubscription(self):
        cluster= cluster()
        if cluster.isExist():
            subscriptionUrl = CLUSTER_SUBSCRIPTION_URL.replace("clusterId", cluster.id)
            self.requestUrl = subscriptionUrl
            SubscriptionList = self.getById()
            if len(SubscriptionList) != 0:
                return(SubscriptionList[0]['kind'])
            else:
                print("Cluster is not on the evaluation or premium mode!")
                return False