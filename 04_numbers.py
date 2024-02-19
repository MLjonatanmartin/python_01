'''
Los numeros se inicializan sin comillas, si los declaras con comillas se toman como un string. 
Con las variables puedes hacer operaciones aritmeticas y actualizar su valor. 

Para hacer operaciones rapidas usa el operador y el igual con el valor: var += 1
Cuando usamos números muy grandes, py los imprime con anotación cientifica.

Clases de Numeros:

    1. Enteros: Son positivos y negativos, llamados integers, represantados int.
    2. Flotantes: Son los números decimales, llamados float, representados float.
    3. Complejos: Son los númeors con partes real e imaginario, represantados complex

'''

from cgitb import small


print('▒' * 50)

# Tema de la clase, numbers

topic = '↓↓↓ Numeros ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

lives = 3
print(f'Var lives => {lives}, type => {type(lives)}')

print('▒' * 50)

lives_2 = '3'
print(f'Var lives_2 => {lives_2}, type => {type(lives_2)}\nEs string porque se ha declarado con comillas.')

print('▒' * 50)

temperature = 12.2
print(f'Var temperature => {temperature}, type => {type(temperature)}\nEs un tipo float porque es decimal')

print('▒' * 50)

lives = 12 + 15
print(f'Var update lives => {lives}, type => {type(lives)}')

print('▒' * 50)

lives -= 7
print(f'Var update lives => {lives}, type => {type(lives)}\nOperacion rapida con -=')

print('▒' * 50)

big_number = 40000000000000000900.789

print(f'Var big_number => {big_number}, type => {type(big_number)}\nAnotación cientifica con números muy grandes o pequeños')

print('▒' * 50)

small_number = 0.000000000000000000000078900001

print(f'Var small_number => {small_number}, type => {type(small_number)}\nAnotación cientifica con números muy pequeños o grandes')

print('▒' * 50)