
from group.group import *

class Config():
    def __init__(self, director_url, api_key, api_password):
        # base director url
        self.BASE_URL = director_url + "/v3"
        # fetch groups id
        self.GROUPS_URL = f"{self.BASE_URL}/groups"
        groupobj = Groups(director_url, api_key, api_password) 
        group_id = groupobj.getProjectAccountID()
        # project
        self.PROJECTS_URL = f"{self.GROUPS_URL}/{group_id}/projects"
        # cluster 
        self.CLUSTERS_URL = f"{self.GROUPS_URL}/{group_id}/clusters"
        self.CLUSTER_CONNECT_LIST = ["name", "projectId", "provider"]
        self.CLUSTER_CONNECT_DATA = dict.fromkeys(self.CLUSTER_CONNECT_LIST, "default")
        # api-key
        self.API_KEY_URL = f"{self.BASE_URL}/apikey"