import argparse
from credentials import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--credential",
        required=True,
        help="credential name")
    parser.add_argument("-p", "--provider",
        required=True,
        help="cloud provider")
    args = parser.parse_args()
    credentialName = args.credential
    provider = args.provider
    credentialobj = Credential(credentialName, provider)
    credentialobj.create()

if __name__ == '__main__':
    main()
