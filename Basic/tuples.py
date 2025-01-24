## Tuples ##
# Tuples are similar to lists, but they are immutable, that is, they cannot be modified.
# Tuples are defined with parentheses ().
# Tuples are faster than lists.
# Tuples are used when you want to protect the data from being modified.
# Tuples are used when you want to use data as a key in a dictionary.

tuple = tuple()
tuple2 = ()

tuple = (1, 2, 3, 'Axel', 'Orozco')
tuple2 = (4, 5, 6)
print(tuple)
print(type(tuple))

print(tuple[0])

print(tuple.count('Axel')) # Count the number of elements
print(tuple.index('Axel')) # Return the index of the element
print(len(tuple)) # Return the length of the tuple

#tuple[1] = 1.70
#print(tuple) # Tuples are immutable X ERROR

print(tuple + tuple2) # Concatenation

sum_tuple = tuple + tuple2
print(sum_tuple) # Concatenation

print(sum_tuple[1:4]) # Slicing

tuple = list(sum_tuple) # Convert tuple to list
print(type(tuple))

tuple[3] = 'Axel Orozco' # Modify the list
tuple.insert(0, 'Hola') # Insert element in the list
print(tuple) 


