 ## Strings ##

my_string = "Hello, World!"
my_string2 = 'Hello, World!'

print(len(my_string))
print(len(my_string2))

print(my_string + "," + my_string2 + '\n')

my_new_line_string = 'Este es un string\ncon un salto de linea!'
print(my_new_line_string)

my_tap_string = 'Este es un string\tcon un tabulador!'
print(my_tap_string)

my_scaped_string = '\\tEste es un string \ncon un backslash '
print(my_scaped_string)

#Formateo

name, surname, age = 'Axel', 'Orozco', 23

print('Mi nombre es  {} {} y tengo {} años'.format(name, surname, age))
print('Mi nombre es  %s %s y tengo %d años' % (name, surname, age))
print('Mi nombre es {1} {0} y tengo {2} años'.format(surname, name, age))
print(f'Mi nombre es {name} {surname} y tengo {age} años')

#Desempaquetado de caracteres
language = 'Python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Division
language_slice = language[1:4]
print(language_slice)

language_slice = language[1:2:4]
print(language_slice)

#Reverse
reversed_language = language[::-1]
print(reversed_language)

#Funciones
print(language.capitalize())
print(language.upper())
print(language.count('t'))
print('1'.isnumeric())
print(language.isnumeric())
print(language.lower())
print(language.upper().isupper())


