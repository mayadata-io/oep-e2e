#!/usr/bin/env python3
from cluster.cluster import *
from dmaas.credentials import *
from mayapps.mayapps import *
from schedule import *
        
def main():

    if os.path.exists("schedule_config.json"):
        with open("schedule_config.json") as json_file:
                args = json.load(json_file)

    scheduleName = args["schedule_name"]
    region = args["region"]

    scheduleobj = schedule(scheduleName, region)
    scheduleobj.create(args)

if __name__ == '__main__':
    main()


