#!/usr/bin/env python

from setuptools import setup, find_packages
import os.path

setup(name='tap-tickettailor',
      version='0.0.1',
      description='Singer.io tap for extracting data from the TicketTailor API',
      author='Fishtown Analytics',
      url='http://fishtownanalytics.com',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_slack'],
      install_requires=[
          'tap-framework==0.0.4',
      ],
      entry_points='''
          [console_scripts]
          tap-tickettailor=tap_tickettailor:main
      ''',
      packages=find_packages(),
      package_data={
          'tap_tickettailor': [
              'schemas/*.json'
          ]
      })
