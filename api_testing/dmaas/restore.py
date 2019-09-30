from schedule import *
from config import *
from cluster.cluster import *
from account.account import *
import argparse
import time

class Restore(Data):
    name = ''
    id = ''
    url = ''
    def __init__(self, clusterName, scheduleName):
        requestUrl = ''
        Data.__init__(self, requestUrl)
        self.clusterName = clusterName
        self.scheduleName = scheduleName

    def getBackupUrl(self):
        scheduleobj = Schedule(self.scheduleName)
        backupUrl = scheduleobj.data['links']['backups']
        print(backupUrl)
        return backupUrl

    def getBackups(self):
        backupUrl = self.getBackupUrl()
        backupStatus = {}
        self.requestUrl = backupUrl
        for dict in self.get():
            backupStatus[dict['name']] = dict['status']
        return backupStatus

    def preChecksPass(self):
        scheduleobj = Schedule(self.scheduleName)
        clusterobj = Cluster(self.clusterName)
        if not scheduleobj.isExist():
            print(f"Schedule {self.scheduleName} doesn't exist!!")
            return False
        if not scheduleobj.isActive():
            print(f"Schedule {self.scheduleName} not active!!")
            return False
        if not clusterobj.isExist():
            print(f"Cluster {self.clusterName} doesn't exist!!")
            return False
        if not clusterobj.isActive():
            print(f"Cluster {self.clusterName} not active!!")
            return False
        if not clusterobj.checkSubscription():
            print(f"Cluster {self.clusterName} not upgraded!!")
            return False
        return True

    def create(self):
        scheduleobj = Schedule(self.scheduleName)
        clusterobj = Cluster(self.clusterName)
        if self.preChecksPass():
            accountobj = Account()
            backupStatus = self.getBackups()
            for backup in backupStatus:
                if backupStatus[backup] == 'Completed':
                    RESTORE_DICT['backupName'] = backup
                    break
            RESTORE_DICT['dmaasScheduleId'] = scheduleobj.id     
            RESTORE_DICT['dstClusterId'] = clusterobj.id
            RESTORE_DICT['organizationId'] = accountobj.getProjectID()
            self.requestUrl = RESTORE_URL
            response = self.post(RESTORE_DICT)
            if response:
                Restore.name = response['name']
                Restore.id = response['id']
                print("Restore started!!")
                self.checkState()

    def checkState(self):
        Restore.url = RESTORE_URL + self.id
        self.requestUrl = self.url
        while self.get()['state'] != 'completed' and self.get()['state'] != 'failed':
            #print(self.get()['state'])
            time.sleep(0.2)
        if self.get()['state'] == 'failed':
            print("Restore failed!!")
        elif self.get()['state'] == 'completed':
            print("Restore done!!")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cluster-name",
            required=True)
    parser.add_argument("-s", "--schedule-name",
            required=True)
    args = parser.parse_args()
    clusterName = args.cluster_name
    scheduleName = args.schedule_name
    restoreobj = Restore(clusterName, scheduleName)
    restoreobj.create()

if __name__ == '__main__':
    main()
