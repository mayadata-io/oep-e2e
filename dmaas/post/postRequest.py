import os
import requests

def postRequest(url, data):
    key = os.environ.get('KEY')
    value = os.environ.get('VALUE')
    auth = (key, value)
    response = requests.post(url, data=data, auth=auth)
    #responseDict = json.loads(response.content.decode('utf-8'))
    if response.status_code == 201:
        return True
    else:
        print(response.status_code, response.reason)
        return False
