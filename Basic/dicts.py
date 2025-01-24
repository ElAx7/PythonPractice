## Dictionaries ##
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# Dictionaries are used to store data values in key:value pairs.
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# Dictionaries are faster than lists.
# Dictionaries are defined with curly brackets {}.

my_dict = dict()
my_other_dict = {}

print(type(my_dict)) 
print(type(my_other_dict)) 

my_other_dict = {"Name" : "Axel", "LasName" : "Orozco", "Age" : 23, "Lenguajes" : {"Python", "Java", "JavaScript"}, 1:1.75}

my_dict = {
    "Name" : "Axel",
    "LasName" : "Orozco",
    "Age" : 23,
    "Lenguajes" : {"Python", "Java", "JavaScript"},
    1:1.75
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict)) 
print(len(my_dict))

print(my_dict["Name"])

my_dict["Name"] = "Axel David" # Change a value
print(my_dict)

my_dict["City"] = "Mexico" # Add a key
print(my_dict)

del my_dict["City"] # Delete a key
print(my_dict) 

print('Axel' in my_dict) # Check if a key exists
print('lasName' in my_dict) # Check if a key exists

print(my_dict.items()) # Return a list containing a tuple for each key value pair

print(my_dict.keys()) # Return a list containing the dictionary's keys

print(my_dict.values()) # Return a list containing the dictionary's values


my_list = ['Name', 1, 'Piso']

my_other_dict = dict.fromkeys(my_list) # Return a dictionary with the specified keys and values
print(my_other_dict)

my_other_dict = dict.fromkeys(('name', 1, 'Piso')) # Return a dictionary with the specified keys and values
print(my_other_dict) 

#my_other_dict = dict.fromkeys(my_dict, 'Axel', 'Orozco') # Return a dictionary with the specified keys and values
#print((my_other_dict))

print(list(my_dict.values())) # Return a list containing the dictionary's keys
print(list(dict.fromkeys(list(my_other_dict.values()).keys()))) 
print(tuple(my_other_dict))
print(set(my_other_dict))

