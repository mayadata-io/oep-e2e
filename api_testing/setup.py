#!/usr/bin/env python3

from distutils.core import setup

setup(name='Distutils',
      version='2.0',
      description='Python Distribution Utilities',
      author='Harshita Sharma',
      author_email='harshita.sharma1729@gmail.com',
      py_modules=['cluster.cluster', 
      'account.account',
      'api_request.request', 
      'dmaas.credentials', 
      'dmaas.schedule', 
      'dmaas.restore', 
      'mayapps.mayapps',
      'config',
      'api_request.status_codes']
     )
