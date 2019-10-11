#!/usr/bin/env python

""" This module has cluster-specific methods  """
import sys
import subprocess

class ClusterAgents():
    
    def isDMaaSAgents(self):
        """ Checks if DMaaS agents are deployed and are in healthy state """
        dmaas_cmd = "kubectl get po -n maya-system | grep -E dmaas-agent"
        dmaas_pod_cmd = dmaas_cmd + "| awk '{print $1}'"
        dmaas_status_cmd = dmaas_cmd + "| awk '{print $3}'"
        velero_cmd = "kubectl get po -n maya-system | grep -E velero"
        velero_pod_cmd =  velero_cmd + "| awk '{print $1}'"
        velero_status_cmd =  velero_cmd + "| awk '{print $3}'"
        dmaas_pod = str(subprocess.check_output(dmaas_pod_cmd,shell=True),'utf-8').strip('\n')
        dmaas_status = str(subprocess.check_output(dmaas_status_cmd,shell=True),'utf-8').strip('\n')
        velero_pod =  str(subprocess.check_output(velero_pod_cmd,shell=True),'utf-8').strip('\n') 
        velero_status = str(subprocess.check_output(velero_status_cmd,shell=True),'utf-8').strip('\n')
        if dmaas_pod != '' and velero_pod != '':
            if dmaas_status == 'Running' and velero_status == 'Running':
                return True
            else:
                print("DMaaS agents not running!")
                print(f"DMaaS agents status: {dmaas_status}")
                print(f"Velero pod status: {velero_status}")
                return False
        else:
            print("DMaaS agents not deployed..")
            return False