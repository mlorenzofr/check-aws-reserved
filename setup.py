#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='check-aws-reserved',
      version='0.1',
      description='Check the expiration time of AWS reserved instances',
      url='https://github.com/mlorenzofr/check-aws-reserved',
      author='Manuel Lorenzo Frieiro',
      author_email='mlorenzofr@gmail.com',
      maintainer='Manuel Lorenzo Frieiro',
      maintainer_email='mlorenzofr@gmail.com',
      license='BSD',
      keywords='nagios aws amazon ec2 instances',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Environment :: Plugins',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Monitoring',
          'Topic :: Utilities'
      ],
      packages=['check_aws_reserved'],
      install_requires=[
          'boto3',
          'python-dateutil'
      ],
      entry_points={
          'console_scripts':
              ['check_aws_reserved = check_aws_reserved.__main__:main']
      },
      zip_safe=False)
