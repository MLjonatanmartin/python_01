'''
Las variables se clasifican en tipos de datos:

1. String: Cadenas de caracteres, es decir texto.
2. Number: Se divide en sub categorias:
    - Int: Enteros, números positivos o negativos sin decimales.
    - Float: Flotantes, números decimales.
    - Complex: Complejos, números con partes real e imaginaría.
3. Booleans: Boleanos, True or False.
4. None: Literalmente nada.

Con el método type() podemos ver el tipo de valor de una variable. 
'''

print('▒' * 50)

# Tema de la clase, tipos de datos

topic = '↓↓↓ Tipos de Datos ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

print('-' * 50)

# Sub tema, type() para saber el tipo de dato

sub_topic = '↓↓↓ Metodo para saber el tipo de dato ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{sub_topic}\n')

print('-' * 50)

print('Con la función type() imprime el tipo de dato')
print('type(sub_topic) =>', type(topic))

print('-' * 50)

print('▒' * 50)

# Tipo de Dato String (cadena de texto) 

my_name = 'Jonatan' # Se inicializa con comillas/comillas dobles

print('my_name dato string => ', my_name)
print('type(my_name) =>', type(my_name))

print('▒' * 50)

# Tipo de Dato int (numeros enteros)

my_age = 23 # No necesitan de ninguna comilla para inicializar
print('my_name dato int => ', my_age)
print('type(my_age) =>', type(my_age))

print('▒' * 50)

# Tipo de Datos Boolean (falso o verdadero)

is_single = True # True or false va la inicial en mayuscula

print('is_single bool => ', is_single)
print('type(is_single) =>', type(is_single))

print('▒' * 50)