'''
Indexings: indicador.

Todo string tiene un indexing, esto permite ingresar a posiciones especificas
del string. Cuando vas a una posición del string que no se encuentra lanza un 
error. 

    1. [0] : Primera posición del string.
    2 [-1] : Ultima posición del string.

Slicing: Forma eficiente de extraer elementos de una secuencia.

Sintaxis: secuencia[inicio:final:paso]

    0. Secuencia: el string.
    1. Inicio: de donde parte.
    2. Final: de donde termina.
    3. Paso: los saltos que haga, en dos en dos por ejemplo

    Se puede saltar el inicio, si no se coloca nada python entiende que comienza desde cero.
    De igual manera con el final.
    
'''
print('▒' * 50)

# Indexing
topic = '↓↓↓ Indexing  Slicing ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# Ejemplo de indexing
text = 'Ella sabe Python'

print(f'Uso de Indexing con =>: {text}')
print(f'text[0] =>: {text[0]}')
print(f'text[1] =>: {text[1]}')

print('▒' * 50)

# Uso de indexing para la ultima posición

print(f'Uso de Indexing con =>: {text}')
print(f'Ultima posición, text[-1] =>: {text[-1]}')

print('▒' * 50)

# Uso de slicing

print(f'Uso de slicing con =>: {text}')
print(f'text[0:5] =>: {text[0:5]}')
print(f'text[10:16] =>: {text[10:16]}')
print(f'text[0:10] =>: {text[0:10]}')

print('▒' * 50)

# Us de slicing saltando el incio y el final

print(text)
print(f'text[:13] =>: {text[:13]}')
print(f'text[5:] =>: {text[5:]}')
print(f'text[:] =>: {text[:]}')

print('▒' * 50)

# Uso de slicing con saltos

print(text)
print('Usando slicing para saltar en el string ↓↓↓')
print(f'text[10:16:2] =>: {text[10:16:2]}')
print(f'text[::2] =>: {text[::2]}')

print('▒' * 50)