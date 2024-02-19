'''
Las candenas de caracteres, conocidas ccomo String, son bastante útiles y tambié muy usados.
A continuación vamos a ver sus métodos más comunes de concatenación: 

1. Concatenar:  Existen varias formas, la tercera es la mejor
    - Es unir dos strings. Se realiza con el operador "+". Recuerda que une las cosas sin espacio.
      Si quieres que las palabras se unan con un espacio, debes colocar ese caracter.
    - Hacer el string y usar {}, luego al final colocar .format(vars, vars) ver Linea 34
    - La mejor y más usada forma es colocar al comienzo f'text {vats} text {vars}' Ver linea Linea 42

'''
print('▒' * 50)

# Tema de la clase, strings

topic = '↓↓↓ Strings y Concatenación ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# Concatenación con el operador +

name = 'Jonatan'
last_name = 'Martin'

print('Cocateneción de name, last_name y \' \' => ', name + ' ' + last_name)

print('▒' * 50)

# Concatenación con el método format

quote = 'Hola, mi nombre es {} y mi apellido es {}'.format(name, last_name)
print('Cocateneción con format => ', quote)

print('▒' * 50)

# Concatenación con el mejor método f'text {var} text {var} ...'

best_quote = f'Hola mi nombre es {name} y mi apellido es {last_name}'

print('Cocateneción con el mejor metodo, F" " => ', best_quote)

print('▒' * 50)