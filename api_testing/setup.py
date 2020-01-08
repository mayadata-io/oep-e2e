#!/usr/bin/env python3

from distutils.core import setup

setup(name='Distutils',
      version='2.0',
      description='Python Distribution Utilities',
      author='Harshita Sharma',
      author_email='harshita.sharma@mayadata.io',
      py_modules=['cluster.cluster', 
      'api_request.request', 
      'config',
      'project.project',
      'group.group',
      'api-key.api-key'
      ]
     )
