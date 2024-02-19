'''
Listas: Una estructura de datos para almacenar.

Utilidades de las listas:

    1. Almacenar cualquier tipo de dato.
    2. Son mutables.
    3. Son indexadas.

Nota: Sinonimos son Array, Vector
'''
print('▒' * 50)

# Listas
topic = '↓↓↓ Listas ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# Ejemplo de una lista
numbers = [1, 2, 3, 4]
print(f'Ejemplo de una Lista =>: {numbers}')
print(f'Tipo de dato de una Lista =>: {type(numbers)}')

print('▒' * 50)

# Ejemplo de lista
tasks = ['make a dishes', 'relax']
print(f'Lista con string =>: {tasks}')
print(f'Tipo de dato de una Lista =>: {type(tasks)}')

print('▒' * 50)

# Ejemplo de lista con tipos de datos diferentes
types = [1, True, 'hola']
print(f'Lista con varios tipos de datos =>: {types}')
print(f'Tipo de dato de una Lista =>: {type(types)}')

print('▒' * 50)

# Indexing de la lista
print(f'Lista =>: {numbers}')
print(f'Indexing con una Lista numbers[0] =>: {numbers[0]}')
print(f'Lista =>: {tasks}')
print(f'Indexing con una Lista task[0] =>: {tasks[0]}')

print('▒' * 50)

# Ejemplo de mutabilidad de una lista

print(f'cambiando La Lista tasks =>: {tasks}')
print('tasks[0] = \'watch platzi courses\'')
tasks[0] = 'watch platzi courses'
print(f'Update de tasks =>: {tasks}')

print('▒' * 50)

# Uso de Slicing con  una Lista
print(f'Slicin con numbers[:3] =>: {numbers[:3]}')

print('▒' * 50)

# Uso del operador in en una Lista
print(f'Operador in: True in types =>: {True in types}')
print(f'Operador in: \'hola\' in types =>: {'hola' in types}')

print('▒' * 50)