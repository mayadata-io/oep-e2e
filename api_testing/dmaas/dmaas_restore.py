import argparse
import time
import json
import base64
from dmaas_schedule import *
from config import *
from cluster.cluster import *
from account.user_account import *
from mayapps.cluster_apps import *

class DMaasRestore(Data):
    name = ''
    id = ''
    url = ''
    data = ''
    def __init__(self, sourceCluster, destCluster, scheduleName):
        request_url = ''
        Data.__init__(self, request_url)
        self.sourceCluster = sourceCluster
        self.destCluster = destCluster
        self.scheduleName = scheduleName

    def preChecksPass(self):
        # dest cluster should exist , active and has dmaas agents
        # source cluster should have running schedule
        # apps should not exist in the dest cluster
        print("Pre-validation started")
        schedule = DMaaSchedule(self.sourceCluster, self.scheduleName)
        cluster = Cluster(self.destCluster)
        if not cluster.isExist():
            print(f"Cluster {self.destCluster} doesn't exist!!")
            return False
        if not cluster.isActive():
            print(f"Cluster {self.destCluster} not active!!")
            return False
        if not cluster.isDMaaSAgents():
            print(f"Cluster {self.destCluster} not upgraded!!")
            return False
        if not schedule.isExist():
            print(f"Schedule {self.scheduleName} doesn't exist!!")
            return False
        if not schedule.isActive():
            print(f"Schedule {self.scheduleName} not active!!")
            return False
        deployment = schedule.data['application']['name']
        namespace = schedule.data['application']['namespace']
        apps = ClusterApps(self.destCluster, deployment, namespace)
        if apps.isExist():
            print("Application already exists!!")
            return False
        print("Pre-validation done")
        return True
    
    def create(self):
        """ creating required objects """
        schedule = DMaaSchedule(self.sourceCluster, self.scheduleName)
        backups = DMaasBackup(self.sourceCluster, self.scheduleName)
        backups = backups.getBackups()
        # checking if a completed backup exists in the DMaaS schedule 
        isBackupComplete = False
        for backup in backups:
            if backups[backup] == 'Completed':
                isBackupComplete = True
                RESTORE_DICT['backupName'] = backup
                break
        # if completed backup exists
        if isBackupComplete == True:
            cluster = Cluster(self.destCluster)
            account = UserAccount()
            # set restore post request data
            RESTORE_DICT['dmaasScheduleId'] = schedule.id     
            RESTORE_DICT['dstClusterId'] = cluster.id
            RESTORE_DICT['organizationId'] = account.getProjectID()
            self.request_url = RESTORE_URL
            print("Restore starting..")
            # sends restore create post request
            response = self.post(RESTORE_DICT)
            # set restore id,name state fir 
            Restore.name = response['name']
            Restore.id = response['id']
            print("Restore started!!")
            # check restore status
            self.checkState()
            return True
        else:
            return False

    def checkState(self):
        Restore.url = RESTORE_URL + self.id
        self.request_url = self.url
        # wait while restore in in-progress
        state = self.getById()['state']
        while state != 'completed' and state != 'failed':
            time.sleep(0.2)
            state = self.getById()['state']
        # once restore finishes checks if it has failed or completed
        if  state == 'failed':
            print("Restore failed!!")
        elif state == 'completed':
            print("Restore done!!")
            self.printRestoreDetails()
            
    def printRestoreDetails(self):
        """ prints DMaaS restore details when it is successful """
        Restore.url = RESTORE_URL + self.id
        self.request_url = self.url
        Restore.data = self.getById()
        stripped_status = (self.data['statusData']).strip('\"')
        status_data = json.loads(base64.b64decode(stripped_status))
        print("Total time taken:",status_data['timestamp']['totalTime'])
        print("Backup Count:",status_data['restores']['backupCount'])
        total_size_bytes = status_data['restores']['totalSize']
        total_size_kbs = total_size_bytes/1000
        print("Total size:",total_size_kbs)
        completed_size_bytes = status_data['restores']['completedRestoresSize']
        completed_size_kbs = completed_size_bytes/1000
        print("Completed Restore Size:",completed_size_kbs)



#k get po -n maya -o jsonpath='{.items[*].spec.containers[*].resources.requests}'



