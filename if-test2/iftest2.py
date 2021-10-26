#!/usr/bin/env python3

import ipaddress
import sys

#ipchk = '192.168.0.1'

ipchk = input('Apply an IP address: ') # this line now prompts the user for input

if ipchk == '192.168.70.1': # if a match on '192.168.70.1'
    print('Looks like the IP address of the Gateway was set: ' + ipchk + ' This is not recommended.')
elif ipchk: #if any data is provided, this will be true
    print ('Looks like the IP address was set: ' + ipchk)
else: # if data is NOT provided
    print ('You did not provide an input.')

try: 
    ip = ipaddress.ip_address(sys.argv[1])
    print('%s is a correct IP%s address.' % (ip, ip.version))
except ValueError:
    print('address/netmask is invalid: %s' % sys.argv[1])
except:
    print('Usage : %s ip' % sys.argv[0])


