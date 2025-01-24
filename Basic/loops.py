## Loops ##
# Loops are used to iterate over a sequence (list, tuple, string) or other iterable objects.
# There are two types of loops in Python, for and while.

#While Loop

my_condition = 0

while my_condition < 10: 
    print(my_condition) 
    my_condition += 2 # Increment the value of my_condition by 1
else: # Optional else block
    print("my_condition is no longer less than 10")

print("End of while loop")

while my_condition < 20:
    my_condition += 2
    if my_condition ==  15:
        print('the exectuoion will break')
        break
    print(my_condition)

    print('my_condition is less than 20')

#For Loop

my_list = [1, 2, 3, 4, 5]

for element in my_list:
    print(element)

my_set = {1, 2, 3, 4, 5}
for element in my_set:
    print(element)