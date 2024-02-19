'''
Ciclo For: hace un ciclo hasta que una condición se cumpla con un 
numero de iteraciones dadas.

la sintaxis es: 

for value in value: 
    # code

Los clicos for se usan cuando sabes cuantas iteraciones son necesarias
y los ciclos whiles cuando no.    

'''
print('▒' * 50)

# Ciclos For
topic = '↓↓↓ Ciclo For ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# ejemplo de for

for element in range(1, 21):
    print(element)

print('▒' * 50)

# ejemplo de ciclo for con una lista
my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element)

print('▒' * 50)

# ejemplo de for con una tupla

my_tuple = ('nico', 'juli', 'santi')

for element in my_tuple:
    print(element)

print('▒' * 50)

# ejemplo de for con un diccionario

producto = {
    'name' : 'camisa',
    'price' : 100,
    'stock' : 89
}

for key in producto:
    print(key, '=>:', producto[key])

print('▒' * 50)

# Otra manera de iterar un diccionario
for key, value in producto.items():
    print(key, '=>:', value)

print('▒' * 50)

# iteraciones con listas con diccionarios

people = [
    {
        'name' : 'nico',
        'age' : 34
    },
    {
        'name' : 'zule',
        'age' : 45
    },
    {
        'name' : 'santi',
        'age' : 4
    }
]

for person in people:
    print('name =>:', person['name'])

print('▒' * 50)
