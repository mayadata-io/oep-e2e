#!/usr/bin/env python3

from distutils.core import setup

setup(name='Distutils',
      version='2.0',
      description='Python Distribution Utilities',
      author='Harshita Sharma',
      author_email='harshita.sharma@mayadata.io',
      py_modules=['api_testing.cluster.cluster', 
      'api_testing.account.account',
      'api_testing.api_request.request', 
      'api_testing.dmaas.credentials', 
      'api_testing.dmaas.schedule', 
      'api_testing.dmaas.restore', 
      'api_testing.mayapps.mayapps',
      'api_testing.config'
      ]
     )
