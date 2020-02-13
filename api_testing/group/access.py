import argparse
from group import *

def main():  
    parser = argparse.ArgumentParser()
    parser.add_argument("--url",
            help="director onprem url")
    parser.add_argument("--username",
            help="director api key")
    parser.add_argument("--password",
            help="director api password")
    parser.add_argument("--account",
            help="director user account")
    parser.add_argument("--resource",
            help="type of cluster resource ex, pool, application")
    #parser.add_argument("--cluster_id",
    #       help="cluster id")
    args = parser.parse_args()
    director_url = args.url
    api_key = args.username
    api_password = args.password
    account = args.account
    resource = args.resource
    groupobj = Groups(director_url, api_key, api_password)
    #groupobj.getMayaApps(account)
    if resource == "pool":
        groupobj.getMayaStoragePools(account)
    elif resource == "maya-app":
        groupobj.getMayaApps(account)
if __name__ == '__main__':
    main()