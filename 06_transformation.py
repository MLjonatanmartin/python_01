'''
Python nos permite cambiar de manera dinamica el tipo de datos de las variables en la ejecución del codigo.
Para hacer operaciones entre variables deben de ser del mismo tipo de dato, sino causa un error.
Los metodos para cambiar el tipo de dato son:
    Coloca el metodo y el valor de la variable para cambiar tu tipo de dato:
    - str(value): cambia a string los valores.
    - int(value): cambia a integers los valores.
    - float(value): cambia a float los valores.
    - complex(value): camabia complex los valores.
    - chr(value): cambia de un número a su caracter Unicode.
    - ord(value): convierte un caracter Unicode a su numero enterro correspondiente.
    - bool(value): cambia a booleanos los valores:
        Importante recordar que 0, '' (string vacio), None (valor nulo) son False, el resto con True
    - list(value): cambia a una lista los valores.
    - tuple(value): cambia a una tupla los valores. 
    - dict(valure): convierte un iterable de pares claver-valor a un diccionario.

    nota:
    - Cuando usas input siempre tendras un dato tipo string. 
    - Cuando usas el formato f'tex {value} text' no es necesario hacer el cambio explicito de las variables para 
    concatenar.

'''

print('▒' * 50)

# Tema de la clase, cambio de tipos de datos

topic = '↓↓↓ Transformacion de Datos ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

name = 'Jonatan'

print(f'Var name => {name}, type => {type(name)}')

print('▒' * 50)

name = 23

print(f'Var name => {name}, type => {type(name)}\nCambio Dinamico del tipo de dato de la variable')

print('▒' * 50)

name = True

print(f'Var name => {name}, type => {type(name)}\nCambio Dinamico de la variable, ahora a un bool')

print('▒' * 50)

age = input('¿Cuál es tu edad? =>: ')

print(f'Var age => {age}, type => {type(age)}\nInput siempre es un string')

# Convertir age a int

age = int(age) 

print(f'Var age => {age}, type => {type(age)}\nCambio de tipo de dato con int()')

# Operacion de suma
age += 10

print(f'Var age => {age}, type => {type(age)}\nOperación de suma age += 10')

print('▒' * 50)
