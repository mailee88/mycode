#!/usr/bin/env python3

def main():
    # Read in our list data
    networklists = []
    with open('driverip.txt', 'r') as driveip:
        for sline in driveip: #single line from our file is sline
            # append adds to the end of our list
            # rstrip removes and special characters on the right 
            # of the str split breaks our string into a list
            # the result is we add a list of driver and ip to
            # networklists
            networklists.append(sline.rstrip("\n").split(' '))

    print(networklists) # display networklists to ensure we recreated it

    for driveandip in networklists:
        print ('SSH to '+ ' using driver ' + driveandip[0])

main()

