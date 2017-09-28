#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

CONTAINING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

package_list = find_packages(where=CONTAINING_DIRECTORY)

setup(
    name='qidata_devices',
    version='0.0.3',
    description='List of device models supported by QiData',
    author='Surya Ambrose <sambrose@softbankrobotics.com>',
    author_email='sambrose@softbankrobotics.com',
    license='LICENSE',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='metadata annotation tagging',
    packages=package_list,
    entry_points={
        'qidata.context.device_models': [
            'Panasonic        = qidata_devices.panasonic:device_model_list',
            'SoftbankRobotics = qidata_devices.softbank_robotics:device_model_list',
        ]
    }
)
