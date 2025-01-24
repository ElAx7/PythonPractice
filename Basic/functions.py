## Functions ##
# This file contains the functions used in the main script

def my_function():
    print("Hello from a function")

my_function() # Call the function

def sum_two_values(first_value, second_value):
    return first_value + second_value

sum_two_values(2, 3) # Call the function
sum_two_values(5, 7) # Call the function

def sum_two_values_with_return(first_value, second_value, retro):
    return first_value + second_value

my_result = sum_two_values_with_return(5, 7) # Call the function
print(my_result)
