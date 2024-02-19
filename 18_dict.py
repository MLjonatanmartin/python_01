'''
Los diccionarios: Un tipod e estructura de almacenamiento de datos con 'clave' : 'valor'.

Se declaran con {}

Metodos:

    1-.get(): sirve para obtener valores del diccionario, en caso que no exista nos dice None
    2- in: puede buscar valores con el operador in en un diccionario

'''

print('▒' * 50)

# Diccionarios
topic = '↓↓↓ Diccionarios ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

my_dict = {
    'avion' : ('bla bla bla',),
    'name' : ('Nicolas',),
    'last_name' : ('Molina Monroy',),
    'age' : (87,)
}

print(my_dict)

print('▒' * 50)

# uso del metodo len con diccionario
print(my_dict)
print(len(my_dict))

print('▒' * 50)

# Uso para acceder a una posición especifica del dict con ['key']
print(my_dict['age'])
print(my_dict['last_name'])

print('▒' * 50)

# Metodo .get() con diccionario

print(my_dict.get('age'))

print('▒' * 50)

# Uso del operador in con dict

print('avion' in my_dict)
print('otroqueno' in my_dict)

print('▒' * 50)
