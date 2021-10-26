#!/usr/bin/env python3

# this is a list we want to augment
proto = ['ssh', 'http', 'https']

# this is a list we want to augment a bit differently
protoa = ['ssh', 'http', 'https']

# print the first list we created
print(proto)

#change our first list
proto.append('dns') #this line will add 'dns' to the list

#perform the same change to the second list
protoa.append('dns') #this will add 'dns' to the end of the list

print(proto)

print(protoa)

proto2 = [ 22, 80, 443, 53 ] # a list of common ports

#perform DIFFERENT change operations on our two lists
# first we perform the EXTEND method
# list.extend()
proto.extend(proto2) #pass proto2 as an argument to the extended method
print("\This is what list.extend() did our list. \n")
print(proto)

#perform append()
protoa.append(proto2)
print("\This is what list.append() did to our list.\n")
print (protoa)

print (proto[4])
print (protoa[4])
print (protoa[4][0])

