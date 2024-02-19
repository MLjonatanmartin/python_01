'''
Los comparadores de Comparación e igualada nos ayudan a desarrollar la lógica
del programa y retornar True or False:
    - Comparación:
        1. > : Mayor que.
        2. < : Menor que.
        3. >= : Mayo o igual que.
        4. <= : Menor o igual que.
    - Igualdad:
        1. == : Igualdad a, comprueba si dos valores son iguales.
        2. != : No igual a, comprues si dos valores no son iguales.

Se pueden utilizar con cualquier tipos de datos en python.
'''

print('▒' * 50)

# Tema de la clase, Operadores de Comparación

topic = '↓↓↓ Operadores de Comparación ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# Uso de Mayor que >

print(f'Usando Mayor que \'>\' con 7 > 3 =>: {7 > 3}')
print(f'Usando Mayor que \'>\' con 3 > 7 =>: {3 > 7}')
print(f'Usando Mayor que \'>\' con 7 > 7 =>: {7 > 7}')

print('▒' * 50)

# Uso de Menor que <

print(f'Usando Menor que \'<\' con 5 < 6 => : {5 < 6}')
print(f'Usando Menor que \'<\' con 6 < 5 => : {6 < 5}')
print(f'Usando Menor que \'<\' con 6 < 6 => : {6 < 6}')

print('▒' * 50)

# Uso de Mayor o Igual que >=

print(f'Uso Mayor o Igual que \'>=\' con 2 >= 1 => : {2 >= 1}')
print(f'Uso Mayor o Igual que \'>=\' con 2 >= 3 => : {2 >= 3}')
print(f'Uso Mayor o Igual que \'>=\' con 2 >= 2 => : {2 >= 2}')

print('▒' * 50)

# Uso de Menor o igual que <=

print(f'Uso Menor o Igual que \'<=\' con 1 <= 2 => : {1 <= 2}')
print(f'Uso Menor o Igual que \'<=\' con 2 <= 1 => : {2 <= 1}')
print(f'Uso Menor o Igual que \'<=\' con 2 <= 2 => : {2 <= 2}')

print('▒' * 50)

# Uso de Igualda ==

print(f'Uso de igualdad \'==\' con 6 == 6 => : {6 == 6}')
print(f'Uso de igualdad \'==\' con 5 == 2 => : {5 == 2}')

print('▒' * 50)

# Uso de No Igual a !=

print(f'Uso de No Igual a \'!=\' con 6 != 10 => : {6 != 10}')
print(f'Uso de No Igual a \'!=\' con 6 != 6 => : {6 != 6}')

print('▒' * 50)

# Uso de igualdad == con string

print(f'Uso de Igualadad con \'Apple\' == \'Apple\' =>: {'Apple' == 'Apple'}')
print(f'Uso de Igualadad con \'Apple\' == \'apple\' =>: {'Apple' == 'apple'}')

print('▒' * 50)

# Uso de igualdad == con tipos de datos diferentes

print(f'Uso de Igualadad con tipos de datos diferente\n\'1\' == 1 =>: {'1' == 1}')

print('▒' * 50)

# Uso de lógica con Mayor o Igual a, caso mayo de edad

age = 18
print(f'Lógica con Mayor o Igual con \'age\' >= 18 =>: {age >= 18}')

# Cambio de age a 15

age = 15
print(f'Lógica con Mayor o Igual con \'age\' >= 15 =>: {age >= 18}')

print('▒' * 50)