import argparse
import base64
from api_request.request import *
from project import *

def main():  
    parser = argparse.ArgumentParser()
    parser.add_argument("--url",
            help="director onprem url")
    parser.add_argument("--username",
            help="director api key")
    parser.add_argument("--password",
            help="director api password")
    parser.add_argument("--id",
            help="admin unique id")
    args = parser.parse_args()
    args = parser.parse_args()
    director_url = args.url
    api_key = args.username
    api_password = args.password
    id = args.id
    data = {'identity': id}
    projectobj = Projects(director_url, api_key, api_password)
    url = projectobj.getUrl() + "/?action=getapikey"
    requestobj = Data(api_key, api_password) 
    response = requestobj.post(url, data) 
    api_key = response['apiKey']
    credentials_pair = base64.b64decode(api_key).decode('utf-8')
    credentials = credentials_pair.split(':')
    username = credentials[0]
    password = credentials[1]
    print(username)
    print(password)

if __name__ == '__main__':
    main()
