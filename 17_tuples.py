'''
Tuplas: Son una estructura de datos que usa para almacenar datos igual que una lista.

Se declaran con los () y no son mutables, por lo que no se pueden editar. 
Son mayormente para lectura.

Los metodos que se pueden usar con las tuplas son:

    1-.index(): para saber el indice de un valor.
    2-.count(): para saber cuantas veces hay un valor en la tupla.
    3-type(): para saber el tipo de dato de la tupla o valor de un elemento de una tupla.

Para poder editar una tupla es necesario transformar la a una lista, el metodo para ello es:

    list(tuple)
    tuple(list)
'''

print('▒' * 50)

# Tuplas
topic = '↓↓↓ Tuplas ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# ejemplo de tupla

numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico')

print(f'tuple numbers =>: {numbers}')
print(f'type(numbers) =>: {type(numbers)}')
print(f'tuple strings =>: {strings}')
print(f'type(strings) =>: {type(strings)}')

print('▒' * 50)

# usando indexing tuplas

print(f'numbers[0] =>: {numbers[0]}')
print(f'numbers[-1] =>: {numbers[-1]}')

print('▒' * 50)

# uso de indexing con tuplas

print(f'Tupla strings =>: {strings}')
print(f'strings.index(\'zule\') =>: {strings.index('zule')}')

print('▒' * 50)

# Uso de count con tuplas

print(f'Tupla strings =>: {strings}')
print(f'strings.count(\'nico\') =>: {strings.count('nico')}')

print('▒' * 50)

print(f'tupla Strings =>: {strings}')
my_list = list(strings)
print(f'tupla a lista my_list = list(strings) =>: {my_list}')

print('▒' * 50)

# Modificar la lista 

print(f'Lista my_list =>: {my_list}')
print(f'type(my_list) =>: {type(my_list)}')
my_list[1] = 'juli'
print(f'Lista modificada {my_list}')

print('▒' * 50)

# Covertir una lista a tupla

my_tuple = tuple(my_list)
print(f'Lista a Tupla my_tuple = tuple(my_list) =>: {my_tuple}')
print(f'type(my_tuple) =>: {type(my_tuple)}')

print('▒' * 50)