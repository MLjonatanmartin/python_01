'''
El Operador NOT sirve para negar expresiones, es decir
retornar lo contrario en booleano.
'''

print('▒' * 50)

# Tema de la clase, Operadores Lógico NOT

topic = '↓↓↓ Operadores Lógico NOT ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# not

print(f'Uso de NOT con True =>: {not True}') # False
print(f'Uso de NOT con False =>: {not False}') # True

print('▒' * 50)

# Uso de not con and

print(f'Uso de NOT con (True and True) =>: {not (True and True)}') # False
print(f'Uso de NOT con (True and False) =>: {not (True and False)}') # True
print(f'Uso de NOT con (False and True) =>: {not (False and True)}') # True
print(f'Uso de NOT con (False and False) =>: {not (False and False)}') # True

print('▒' * 50)

# Ejemplo de NOT con el stock de la pagina web

stock = int(input('Ingrese el número de stock =>: '))
print(f'El stock es {not ((stock >= 100) and (stock <= 1000))}')

print('▒' * 50)
