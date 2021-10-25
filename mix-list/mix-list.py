#!/usr/bin/env python3

mylist = [ "192.168.0.5", 5060, "UP" ]

#print using concatenation

print ("The first item in the list (IP): " + mylist[0])
print ("The second item in the list (port): " + str(mylist[1]))
print ("The last item in the list (state): " + mylist[2])

new_list = [ 5600, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#print string using f format

print (f"The IP addresses are {new_list[3]} and {new_list[4]} with port {new_list[0]}, {new_list[1]}, and {new_list[2]} using {new_list[5]}")

