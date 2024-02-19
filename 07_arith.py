'''
Para realizar operaciones aritmeticas usamos los operadores:
    - + para sumar. 
    - - para restar.
    - * para multiplicar.
    - / para dividir.
    - // para realizar operación entera, sin decimales.
    - % para devolver el resto de la división.
    - ** para potenciar. 

Los operadores funcionan de una manera diferento con otros tipos de datos:
    1. String:
        - +: Para concatenar.
        - *: Para replicar el numero de veces que sea multiplicado.

Para poder realizar las operaciones aritmeticas, se sigue un orden establecido PEMDAS:
    1. Paréntesis (P): Primero, se resuelven las expresiones dentro de los parentisis.
    2. Exponentes (E): Segundo, se resuelven las potencias y raices.
    3. Multiplicación (M) y División (D): Tercero, se hacen las multiplicaciones y divisiones
        de izquierda a derecha como aparezcan en la expresión.
    4. Adición (A) y Resta (S): Cuarto, al igual que el punto anterior se hacen de izquierda
        a derecha como aparezcan en la expresión.
    Las operaciones PEMDAS se hacen de izquierda a derecha siguiendo el orden de cada categoría.   
'''

print('▒' * 50)

# Tema de la clase, Operadores Aritmeticos

topic = '↓↓↓ Operaciones Aritmeticas ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# suma
print(f'Ejemplo de suma 3 + 5: {3 + 5}')

print('▒' * 50)

# resta
print(f'Ejemplo de resta 10 - 7: {10 - 7}')

print('▒' * 50)

# multiplicación
print(f'Ejemplo de multiplicación 2 * 9: {2 * 9}')

print('▒' * 50)

# división
print(f'Ejemplo de división 779 / 380: {779 / 380}')

print('▒' * 50)

# resto de la división
print(f'Ejemplo del resto de la división 779 % 380: {779 % 380}')

print('▒' * 50)

# división entera, sin decimales
print(f'Ejemplo de división sin decimales 779 % 380: {779 // 380}')

print('▒' * 50)

# potencia
print(f'Ejemplo de de potencia 20 ** 4: {20 ** 4}')

print('▒' * 50)

print('-' * 50)

# Operadores aritmeticos con string

print(f'Uso del operador +, Hola + Mundo => {'Hola ' + 'Mundo'}')

print('-' * 50)

print(f'Uso del operador *, Panela * 5 ↓↓↓\n{'Panela' * 5}')

print('-' * 50)

print('▒' * 50)

# Expresión con PEMDAS

print('Operación aritmetica con PEMDAS ↓↓↓')
print(2 ** 3 + 3 - 7 / 1 // 4)

print('▒' * 50)