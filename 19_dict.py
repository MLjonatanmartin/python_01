'''
Para hacer ediciones a un diccionario:

    Actualizar:
        1. Coloca el nombre del diccionario y su clave, puedes editarlo con =,
            si es una lista puedes usar sus métodos.
    Eliminar:
        1. Para eliminar usar del metodo, el nomrbe del diccionario y la clave:
            - del
            - .pop('key')
    
    Otros metodos del diccionario:

    1-.items(): para obtener los items del diccionario clave y valor en tuplas.
    2-.keys(): para obtener las llaves del los diccionarios, es dinamico.
    3-.values(): para obtener los valores de las claves de los diccionarios, es dinamico x2.
'''


print('▒' * 50)

# Diccionarios 2
topic = '↓↓↓ Diccionarios 2 ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# ejemplo de un diccionario

person = {
    'name': 'nico',
    'last_name' : 'molina',
    'langs' : ['py', 'js'],
    'age' : 99
}

print(person)

print('▒' * 50)

# actualizacion de llaves en diccionario

person['name'] = 'santi'
person['age'] -= 50
person['langs'].append('rust')
print(person)

print('▒' * 50)

# Eliminar un atributo del diccionario

del person['last_name']
person.pop('age')
print(person)

print('▒' * 50)

# Uso del .items(), keys() y values()

print(f'Itmes del diccionario =>:\n{person.items()}')
print(f'keys del diccionario =>:\n{person.keys()}')
print(f'values del diccionario =>:\n{person.values()}')

print('▒' * 50)
