#!/usr/bin/env python3
import os
import time
import argparse
from cluster.cluster import *
from dmaas.credentials import *
from mayapps.mayapps import *
from schedule import *

def waitForActiveSchedule(scheduleobj):
    print("Waiting for DMaaS schedule to be active!")
    timer = 2
    total_time = 0
    while not scheduleobj.isActive():
        if total_time >= 300:
            print("DMaaS schedule not getting active!! Something is wrong!")
            sys.exit(1)
        time.sleep(timer)
        total_time += timer        
    time_in_mins = round(total_time/60)
    print("DMaaS schedule active!!")
    print(f"Time taken for the DMaaS schedule to be active {time_in_mins} minutes")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cluster-name",
            required=True,
            help="cluster name minLength: 6,maxLength: 24")
    parser.add_argument("--credential-name",
            required=True,
            help="credential name")
    parser.add_argument("--schedule-name",
            required=True,
            help="schedule name minLength: 3,maxLength: 24")
    parser.add_argument("--region",
            help="aws region")
    parser.add_argument("--provider",
            help="cloud provider")
    parser.add_argument("--deployment",
            help="app deployment")
    parser.add_argument("--namespace",
            help="app namespace")
    args = parser.parse_args()
    scheduleName = args["schedule_name"]
    clusterName = args["cluster_name"]
    scheduleobj = Schedule(clusterName, scheduleName)
    if scheduleobj.preValidation(args):
        scheduleobj.create(args)
        waitForActiveSchedule(scheduleobj)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()


