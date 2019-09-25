#!/usr/bin/env python

""" director account specific methods """

from api_request.request import *
from config import *


class account:
    def getOrganizationID(self):
        organizationsList = getRequest(organizationsUrl)
        # assuming there is only one organization for now
        for dict in organizationsList:
            organizationId = dict['id']
            return(organizationId) 

