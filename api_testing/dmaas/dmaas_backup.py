from dmaas_schedule import *
from api_request.request import *

class DMaasBackup(Data):
    data = {}
    url = ''
    id = ''

    def __init__(self, clusterName, scheduleName):
        self.scheduleName = scheduleName
        self.clusterName = clusterName
        request_url = ''
        Data.__init__(self, request_url)
        
    def getBackupUrl(self):
        schedule = DMaaSchedule(self.clusterName, self.scheduleName)
        backupUrl = self.data['links']['backups']
        return backupUrl

    def getBackups(self):
        backupUrl = self.getBackupUrl()
        backups = {}
        self.request_url = backupUrl
        data = self.get()
        for dict in data:
            backups[dict['name']] = dict['status']
            return backups