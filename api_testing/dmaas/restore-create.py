""" This script creates restore if all pre-checks """

# python built-in modules
import argparse
import sys
# packages
from restore import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--source-cluster",
            required=True)
    parser.add_argument("-d", "--dest-cluster",
            required=True)
    parser.add_argument("-s", "--schedule-name",
            required=True)
    args = parser.parse_args()
    source_cluster = args.source_cluster
    dest_cluster = args.dest_cluster
    schedule_name = args.schedule_name
    restoreobj = Restore(source_cluster, dest_cluster, schedule_name)
    if restoreobj.preChecksPass():
        restoreobj.create()
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
