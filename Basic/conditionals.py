## Conditionals ## 
# Conditionals are used to execute a block of code based on a condition.
# An if statement is written by using the if keyword.

my_condition = True

if my_condition: # If the condition is True, the block of code 
                        #inside the if statement will be executed.
    print('Se ejecuta la condicion del if')

my_condition = 5 * 2

if my_condition == 10:
    print('Se ejecuta la condicion del segundo if')

if my_condition > 10 and my_condition < 20:
    print('Es mayor que 10 y menor que 20')
else:
    print('Es mayor o igual que 10 o mayor o igual que 20')

print('La ejecucion continua...')