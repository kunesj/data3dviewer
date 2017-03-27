#!/usr/bin/env python
# encoding: utf-8

import os
from setuptools import setup, find_packages

import data3dviewer

setup(name='data3dviewer',
        version = data3dviewer.__version__,
        description = 'Viewer for 3d data (mostly from CT).',
        long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
        author = 'Jiří Kuneš',
        author_email = 'jirka642@gmail.com',
        url = 'https://github.com/kunesj/data3dviewer',
        keywords = ['viewer', '3d'],
        packages = find_packages(),
        include_package_data = True,
        license = "GPL3",
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Topic :: Multimedia :: Graphics :: Viewers',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
        ],
        entry_points = {
        'console_scripts': ['data3dviewer = data3dviewer.__main__:main'],
        },
        install_requires = [
          'io3d',
          'sed3',
        ],
    )
