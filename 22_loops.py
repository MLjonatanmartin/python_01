'''
Ciclos anidados:

Se pueden tener ciclos dentro de otros ciclos para hacer cosas

'''

print('▒' * 50)

# Ciclos Anidados
topic = '↓↓↓ Ciclos Anidandos ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# ejemplo de una lista con listas, vectores
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0][1])

print('▒' * 50)

# ciclos anidado en la lista de vectores

for row in matriz:
    print('-' * 20)
    print(row)
    print('-' * 20)
    for column in row:
        print(column)

print('▒' * 50)
