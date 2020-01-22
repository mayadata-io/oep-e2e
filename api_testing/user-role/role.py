from api_request.request import *
from group.group import *

class Role():
   
    def __init__(self, director_url, api_key, api_password):
        self.base_url = director_url
        self.api_key = api_key
        self.api_password = api_password
       
    def changeRole(self, member_emailId, role):
        groupObj = Groups(self.base_url, self.api_key, self.api_password)
        member_data = groupObj.searchMemberByEmailID(member_emailId)
        api_endpoint = member_data['actions']['changerole']
        data = {}
        data['role'] = role
        requestobj = Data(self.api_key, self.api_password) 
        response = requestobj.post(api_endpoint, data)



    
        