#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

while True:
    ## where to connect to
    ex = input("Continue (y/n)").lower()
    if ex == "n" or ex == "no":
        break

    ipaddr = input('Enter an IP address to connect: ')
    usern = input('Enter the username" ')
    passw = input('Enter the password of the user: ')

    #t = paramiko.Transport("10.10.2.3", 22) ## IP and port

    t = paramiko.Transport(ipaddr, 22)

    ## how to connect (see other labs on using id_rsa Private/Public keypairs)
    #t.connect(username="bender", password="alta3")
    t.connect (username=usern, password=passw)

    ## Make an sftp connection object
    sftp = paramiko.SFTPClient.from_transport(t)

    ## iterate across the files within directory
    for x in os.listdir("/home/student/filestocopy/"): #iterate directory contents
        if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
            sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

    ## close the connection
    sftp.close() # close connection
