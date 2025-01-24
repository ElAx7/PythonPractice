import array   

balance = array.array ('i', [1000, 2000, 3000, 4000])

#Inserting elements in array
balance.insert(2, 5000)
print(balance)

#Removing elements from array
balance.remove(5000)
print(balance)

#Finding the index of an element
print(balance.index(2000))

#Update an element
balance[2] = 6000
print(balance)

#Traversal of array
for i in balance:
    print(i)

