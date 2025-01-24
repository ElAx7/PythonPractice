## Listas ##

lista = list()
lista2 = []

print(len(lista))

lista = [1, 2, 3, 4, 5, 5]
print(lista)
print(len(lista))

lista2 = [1, 5, 5.5, 'Hola', 'Mundo', 'Python', 'Python']
print(type(lista2))

print(lista2[0])
print(lista2[1])
print(lista2[2])
print(lista2.count('Python')) # Cuenta cuantas veces se repite el valor 5 en la lista

age, height, name, surname, address, food, python = lista2[2], lista2[3], lista2[4], lista2[5], lista2[6], lista2[0], lista2[1]
print(name)

print(lista + lista2)

lista2.append('Java') # Agrega un elemento al final de la lista
print(lista2)

lista2.insert(3, 'C++') # Agrega un elemento en la posición 3 de la lista
print(lista2)

lista2.remove('Python') # Elimina el primer elemento que coincida con el valor 'Python'
print(lista2)

lista2.pop(3) # Elimina el elemento en la posición 3 de la lista
print(lista2)

