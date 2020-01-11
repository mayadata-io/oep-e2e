import argparse
from invite import *
from group.group import *

def main():  
    parser = argparse.ArgumentParser()
    parser.add_argument("--url",
            help="director onprem url")
    parser.add_argument("--inviter_username",
            help="director api key")
    parser.add_argument("--inviter_password",
            help="director api password")
    parser.add_argument("--invitee_username",
            help="director api key")
    parser.add_argument("--invitee_password",
            help="director api password")
    parser.add_argument("--account_id",
            help="account_id")
    args = parser.parse_args()
    director_url = args.url
    inviter_api_key = args.inviter_username
    inviter_api_password = args.inviter_password
    invitee_api_key = args.invitee_username
    invitee_api_password = args.invitee_password
    account_id = args.account_id
    inviteObj= Invite(director_url)
    inviteObj.invite(inviter_api_key, inviter_api_password, account_id)
    inviteObj.accept(invitee_api_key, invitee_api_password)

if __name__ == '__main__':
    main()