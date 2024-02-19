'''
Los Operadores Logicos son muy utilizados para el desarrollo de la logica del programa,
su resultado dará un dato boolenao y se pueden trabajar con cualquier tipo de dato:

1.AND:
    Se usa para evaluar que ambas expresiones sean verdaderas, si ambas son verdaderas
    da True, si alguna expresión es falsa, da como resultado False.

2.OR:
    Se usa para evaluar que una de las condiciones que sea verdadera, si una es verdadera
    da True, si todas falsas da False.
'''

print('▒' * 50)

# Tema de la clase, Operadores Lógicos

topic = '↓↓↓ Operadores Lógicos And y OR ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# Uso del operador AND 

print(f'Uso de AND con True and True =>: {True and True}') # True
print(f'Uso de AND con True and False =>: {True and False}') # False
print(f'Uso de AND con False and True =>: {False and True}') # False
print(f'Uso de AND con False and False =>: {False and False}') # False

print('▒' * 50)

# Uso de AND en una expresion 

print(f'Expresion (10 > 5) and (5 < 10) =>: {(10 > 5) and (5 < 10)}') # True
print(f'Expresion (10 > 5) and (5 > 10) =>: {(10 > 5) and (5 > 10)}') # False

print('▒' * 50)

# Aplicacion de uso en Inventario con AND
# El Stock mayor o igual a 100
# El Stock menor o igaul a 1000

stock = int(input('Ingrese el número de stock =>: '))
print(f'El stock es {(stock >= 100) and (stock <= 1000)}')

print('▒' * 50)

# Uso del Operador Or

print(f'Uso de OR con True or True =>: {True or True}') # True
print(f'Uso de OR con True or False =>: {True or False}') # True
print(f'Uso de OR con False or True =>: {False or True}') # True
print(f'Uso de OR con False or False =>: {False or False}') # True

print('▒' * 50)

# Uso de OR en caso de una web administrativa del Stock

role = input('Digite su Rol por favor =>: ')
print(f'Rol de la Pagina Web =>: {(role == 'admin') or (role == 'seller')}')

print('▒' * 50)