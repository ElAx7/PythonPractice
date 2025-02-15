'''
FIZZ BUZZ:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
Múltiplos de 3 por la palabra "fizz".
Múltiplos de 5 por la palabra "buzz".
Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''
def fizzbuzz():
    for i in range(1,101):
        divisible_three = i % 3 == 0
        divisible_five = i % 5 == 0
        if divisible_three and divisible_five:
            print("fizzbuzz")
        elif divisible_three:
            print("fizz")
        elif divisible_five:
            print("buzz")
        else:
            print(i)


#Otra forma de hacerlo

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)



#Otra forma de hacerlo

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            if i % 5 == 0:
                print("fizzbuzz")
            else:
                print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizzbuzz()

