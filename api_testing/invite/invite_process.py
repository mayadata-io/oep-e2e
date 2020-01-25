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
    parser.add_argument("--action",
            help="action")

    args = parser.parse_args()
    director_url = args.url
    inviter_api_key = args.inviter_username
    inviter_api_password = args.inviter_password
    invitee_api_key = args.invitee_username
    invitee_api_password = args.invitee_password
    account_id = args.account_id
    action = args.action
    inviteObj= Invite(director_url)
    inviteObj.invite(inviter_api_key, inviter_api_password, account_id)
    # wait till the invite is active
    flag = inviteObj.isActive(invitee_api_key, invitee_api_password)
    retry_counter = 1
    retries = 10
    while retry_counter <= retries:
        if flag:
                if action == "accept":
                        inviteObj.accept(invitee_api_key, invitee_api_password)
                elif action == "reject":
                        inviteObj.reject(invitee_api_key, invitee_api_password)
                break
        flag = inviteObj.isActive(invitee_api_key, invitee_api_password)
        retry_counter += 1

if __name__ == '__main__':
    main()