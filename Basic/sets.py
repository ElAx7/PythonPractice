## Sets ## 
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
# Sets are unordered, so you cannot be sure in which order the items will appear.
# Sets are unchangeable, meaning that we cannot change the items after the set has been created.
# Sets are faster than lists.
# Sets are defined with curly brackets {}.


set = set()
set2 = {}

print(type(set)) # This will print set
print(type(set2)) # This will print dict, not set. This is because {} is used to define both sets and dictionaries.

set2 = {'Axel', 'Orozco', 1, 2, 3}
print(type(set2)) # This will print set

set2.clear()
print(len(set2)) # This will print 0

set2 = {'Kotlin', 'Java', 'Python', 'JavaScript'}

my_new_set = set.union(set2)
print(my_new_set.union(my_new_set).union(set).union({'javaScript', 'C#'})) # This will print {'Kotlin', 'Java', 'Python', 'JavaScript'}

print(my_new_set.difference(set)) 


