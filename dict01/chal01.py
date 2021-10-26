# Part 1

# Take the following lists

dogs = ["fido", "spot", "lucky"]

cats = ["fluffy", "snowball", "garfield"]

# And combine them into a list called pets.
pets = dogs + cats

#need to create an empty list
# pets = []
# pets.extend(dogs)
# pets.extend(cats)
# setting pets= dogs would also change the dogs list
#pets.extend(cats)

print(dogs)
print(cats)
print(pets)

# Part 2

# Using the same lists from above,
# create a dictionary called my_pets
# that has the keys of 'dogs' and 'cats'
# with the values being the appropriate
# lists.

# In this example, changing the 'dogs' list later would also change the values
# of the dictionary.
# To prevent this problem, create the dictionary with the followings
# mypets = {'dogs': dogs.copy(), 'cats': cats.copy()}

mypets = {'dogs': dogs, 'cats': cats}
print( mypets['dogs'])
print( mypets['cats'])

# Part 3

# Prove you can use the pets list to print
# "I only own spot and snowball"
# txt = f"I only own {dogs[1]} and {cats[1]}"
# print (txt)

print (f"I only own {dogs[1]} and {cats[1]}")

print (f"I only own {mypets['dogs'][1]} and {mypets['cats'][1]}")
# Part 4

# Prove you can use the my_pets dict to print
# "I want to adopt fido and garfield too"

print(f"I want to adopt {dogs[0]} and {cats[2]} too")
print(f"I want to adopt {mypets['dogs'][0]} and {mypets['cats'][2]} too")

# To print memory space of a list
# print(id(pets))
# pets = dogs.copy()
