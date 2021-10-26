#!/usr/bin/env python3

import shutil

import os

os.chdir('/home/student/mycode/')

# The following lines will copy a file
shutil.copy('5g_research/sdn_networks.txt', '5g_research/sdn_networks.txt.copy')

# The following lines will create a new directory, if it does not exist
shutil.copytree('5g_research/', '5g_research_backup/')


