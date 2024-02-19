'''
Métodos más comunes con strings:

    1-in: se usa para saber si hay algo en dentro.
    2-len(): da el tamaño de toda la cadena de caracteres.
    3-.upper(): coloca todo el string en MAYUSCULA.
    4-.lower(): coloca todo el string en minuscula.
    5-.swapcase(): coloca en MAYUSCULA un string en minucuslas y viceversa.
    6-.count('value'): cuentas las veces que aparece un caracter en el string.
    7-.startswith('value'): nos muestra si el string comienza con 'value', return boolean.
    8-.endswith('value'): nos muestra si el string termina con 'value', return boolean.
    9-.replace('old_value', 'new_value'): reemplaza un valor del string.
    10-.capitalize(): Coloca el primer caracter del string en Mayuscula.
    11-.tittle(): Coloca en Mayuscula, la primera letra de cada palabra.
    12-.isdigit(): Nos dice si el texto es un digito, return boolean.

'''

print('▒' * 50)

# String, Métodos
topic = '↓↓↓ String, Métodos ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# Uso del operador in con string
text = 'Ella sabe programar en Python'
print(f'Uso de IN con \'JavaScript\'\nEn =>: {text} =>: {'JavaScript' in text}')
print(f'Uso de IN con \'Python\'\nEn =>: {text} =>: {'Python' in text}')

print('▒' * 50)

# Uso de condicional y in
if 'JS' in text:
    print('Elegiste Bien!!!')
else:
    print('Has elegido bien x2')

print('▒' * 50)

# Uso del len
love = 'amor *'

print(f'Uso de len() en ({love}) =>: {len(love)}')
print(f'Uso de len() en\n({text}) =>: {len(text)}')

print('▒' * 50)

# Uso de .upper()
print(f'Uso de .upper() con\n{text}\n{text.upper()}')

print('▒' * 50)

# Uso de .lower()
print(f'Uso de .lower() con\n{text}\n{text.lower()}')

print('▒' * 50)

# Uso de .count()
print(f'Uso de .count(\'a\') con\n{text}\n{text.count('a')}')

print('▒' * 50)

# Uso de .swapcase()
print(f'Uso de .swapcase() con\n{text}\n{text.swapcase()}')

print('▒' * 50)

# Uso de .startswith('value')
print(f'Uso de .startwith(\'Ella\') con\n{text}\n{text.startswith('Ella')}')

print('▒' * 50)

# Uso de .endswith('value')
print(f'Uso de .endswith(\'Rust\') con\n{text}\n{text.endswith('Rust')}')

print('▒' * 50)

# Uso de .replace('old_velue', 'new_value')
print(f'Uso de .replace(\'Python\', \'Go\') con\n{text}\n{text.replace('Python', 'Go')} ')

print('▒' * 50)

# New text
text_2 = 'este es un titulo'
print(f'Nuevo texto =>: {text_2}')

print('▒' * 50)

# Uso de .capitalize()
print(f'Uso de .capitalize() con\n{text_2}\n{text_2.capitalize()}')

print('▒' * 50)

# Uso de .tittle()
print(f'Uso de .tittle() con\n{text_2}\n{text_2.title()}')

print('▒' * 50)

# Uso de .isdigit()

print(f'Uso de .isdigit() con {text_2} =>: {text_2.isdigit()}')
print(f'Uso de .isdigit() con \'890\' =>: {'890'.isdigit()}')

print('▒' * 50)