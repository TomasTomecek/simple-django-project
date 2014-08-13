#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from setuptools import setup
from distutils.command.install import INSTALL_SCHEMES

project_name            = "simple-django-project"
project_dirs            = ["simple"]
project_url             = "https://github.com/TomasTomecek/simple-django-project"
project_author          = "Tomas Tomecek"
project_author_email    = "ttomecek@redhat.com"
project_description     = "Simple django 1.7 project deployed on RHEL 7 with RHSCL"
package_name            = project_name
package_module_name     = 'simple'
package_version         = "1"
packages                = ['simple']

data_files = {}
paths = ['simple/static/']
for path in paths:
    for root, dirs, files in os.walk(path):
        data_files[root] = [os.path.join(root, f) for f in files]

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

setup (
        name            = package_name,
        version         = package_version,
        url             = project_url,
        author          = project_author,
        author_email    = project_author_email,
        description     = project_description,
        packages        = packages,
        include_package_data = True,
        data_files      = data_files.items(),
)

