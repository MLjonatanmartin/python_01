'''
Mientras la condición sea verdadera se ejecuta el código.
Las cosas del ciclo tienen que estar identadas para su ejecución
Con la sentencia break rompemos el ciclo.
Con la sentencia continue saltas a la siguiente repetición
'''
print('▒' * 50)

# Ciclos While
topic = '↓↓↓ Ciclos While ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# Ciclo while
'''
while True:
    print('Se ejecuta')'''

print('▒' * 50)

# Uso de un while
'''counter = 0 

while counter < 10:
    counter += 1
    print(counter)

print('▒' * 50)'''

# Romper el ciclo while

'''counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
        break
    print(counter)
'''
print('▒' * 50)

counter = 0

while counter < 20:
    counter += 1 
    if counter < 15:
        continue
    print(counter)

print('▒' * 50)
