#!/usr/bin/env python3

import shutil

import os

#import pwd

#import grp

os.chdir('/home/student/mycode/')
shutil.move('raynor.obj', 'ceph_storage/')
xname = input('What is the new name for kerrigan.obj? ')
# The following line will rename a file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

#uid = pwd.getpwnam("nobody").pw_uid
#gid = grp.getgrnam("nogroup").gr_gid

#print (uid)
#print (gid)

