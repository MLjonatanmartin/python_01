'''
Las variables son nombres que apuntan a un objeto de memoria. 
Con ellas se 'guardan' datos con los cuales se puede trabajar
en el código.

Las variables pueden actualizar su valor a lo largo del código, 
es decir que su valor puede cambiar. Por otro lado, en python 
tenemos variables sin tipar y tipadas, es decir, podemos tener
variables con un tipo de dato unico o sin espicificar su tipo 
de dato.

Por último, es una excelente práctica nombrar variables con nombres
descriptivos.
'''

print('▒' * 50)

# Tema de la clase, variables

topic = '↓↓↓ Manejo de variables ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

# Esto es una variable
my_name = 'Martin'

print('Variable my_name =>: ', my_name)

print('▒' * 50)

# Esto es una variable con un numero
my_age = 23

print('Variable my_age =>: ', my_age)

print('▒' * 50)

# Cambio del valor de una variable
my_name = 'Jonatan'

print('Variable my_name cambiada =>: ', my_name)

print('▒' * 50)

# Solicitar un valor para una variable

my_name = input('Por favor, ingrese su nomber: \n')
print('Valor ingresado a una variable =>: ', my_name)

print('▒' * 50)