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
    args = parser.parse_args()
    director_url = args.url
    api_key = args.username
    api_password = args.password
    groupobj = Groups(director_url, api_key, api_password)
    group_id = groupobj.getProjectAccountID()
    print(group_id)
    
if __name__ == '__main__':
    main()