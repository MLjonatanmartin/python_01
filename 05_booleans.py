'''
Los Boleanos, en inglés Bool o Booleans (plurar) son un tipo de dato muy importante
ya que nos permite la toma de decisiones en nuestro script. Solo cuenta
con dos valores: 
    -True.
    -False.
Es como los 0 1 en codigo binario. 

Para cambiar su valor sin declarar explicitamente una variable en uso puedes
usar el operador:
    -not, 
que retorna el valor contrario de una variable de True y False.

NOTA: En python podemos hacer la conversion de valores, es decir, podemos hacer 
de un string a un int. Cuando vamos a convertir valores a datos booleanos, los 
valores:
    - 0.
    - '' (string vacio).
    - None (valor nulo).
Siempre nos darán False, todos los demás valores diferentes a estos nos darán True.
Por último, cuando hacemos comparaciones o comprobaciones con el valor None lo mejor
es usar el operador:
    -is
'''


print('▒' * 50)

# Tema de la clase, booleanos

topic = '↓↓↓ Boleanos ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# Uso de Booleanos

is_single = True
print(f'Var is_single => {is_single}, type => {type(is_single)}')

print('▒' * 50)

# Actualizacion de la variable

is_single = False
print(f'Var is_single => {is_single}, type => {type(is_single)}\nCambio de valor a False')

print('▒' * 50)

# Uso del operador not para cambiar el valor de la variable.

is_single = not is_single
print(f'Var is_single => {is_single}, type => {type(is_single)}\nCambio de valor a True por el operador not')

print('▒' * 50)

a = None
print(a, type(a))

a = not a
print(a, type(a))