'''
Absolute: abs() En matematicas mira que tan alejado se encuentra el número x del zero
        En la recta númerica, sin importar la dirección que tenga. Por eso mismo el 
        el abs(5) es 5, y el abs(-5) es 5, ya que no importa la dirección, solo se mide 
        la distancia del numero X con el 0, por eso ambos dan 5. 

Cuando se hacen operaciones con decimales en computadoras es muy dificil tener una 
precisión exacta, ya que esos números no se pueden representar de forma exacta con bits.
Los bits son pulsos de energía en el procesador, entonces solo puedes tener o un 1 o 0,
no puedes tener un 1.1 o 0.5 en bits.

Para lograr trabajar con números decimlaes en computadoras, hay una limitación finita de números
para representar la precisión exacta de los números decimales. 
Python sigue el estandar de punto flotante de doble precisión (double-precision floating-point).
Es por eso que cuando realizamos operaciones con ellos nos agruega zeros para lograr esa precisión
del número que se quiere representar. 

Esta es la razón por la cual se hace un margen de tolerancia de error para poder trabajar con ellos 
de forma matemática y se usa el metodo absolute abs().
'''

print('▒' * 50)

# Tema de la clase, Comaparción con Flotantes

topic = '↓↓↓ Comparación con Flotantes ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# Valor de Números flotantes

x = 3.3
y = 1.1 + 2.2

print(f'Valor de x =>: {x}\nValor de y =>: {y}')

print('▒' * 50)

# Comparación de números flotantes

print(f'Igualdad con X: {x} y Y: {y}\nResultado =>: {x == y}')

print('▒' * 50)

# Transformación a strig para igualdad

y_string = format(y, '.2g') # uso del metodo para tener dos digitos, nada más

print(f'Igualdad hecha con string con X: {str(x)} y Y: {y_string}\nResultado =>: {str(x) == y_string}')

print('▒' * 50)

# Igualdad de Decimales con metodos matematico

tolerance = 0.00001

print(f'Igualdad matemática de X:{x} y Y:{y}\nResultado =>: {(x - y) < tolerance}')

print('▒' * 50)