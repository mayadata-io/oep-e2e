import argparse
from role import *

def main():  
    parser = argparse.ArgumentParser()
    parser.add_argument("--url",
            help="director onprem url")
    parser.add_argument("--username",
            help="director api key")
    parser.add_argument("--password",
            help="director api password")
    parser.add_argument("--group_id",
            help="group_id")
    parser.add_argument("--role",
            help="role")
    parser.add_argument("--member_emailId",
            help="member_emailId") 
    args = parser.parse_args()
    director_url = args.url
    api_key = args.username
    api_password = args.password
    group_id = args.group_id
    role = args.role
    member_emailId = args.member_emailId
    roleObj= Role(director_url, api_key, api_password)
    roleObj.changeRole(member_emailId, role)
 
if __name__ == '__main__':
    main()