'''
Programa para evaluar si un número es par o impar
'''

from turtle import title


print('▒' * 50)

greeting_message = 'Bienvenido a Calcu.App'.center(47)

print(f'\n{greeting_message}\n')

print('▒' * 50)
print('-' * 50)

user_number = int(input('por favor digite un número =>: '.title()))

if user_number % 2 == 0:
    print('-' * 50)
    print(f'el número {user_number} es par'.title())
    print('-' * 50)
else:
    print('-' * 50)
    print(f'el número {user_number} es impar'.title())
    print('-' * 50)

print('▒' * 50)

end = 'Gracias por tomar nuestros servicios'.center(47)

print(f'\n{end}\n')

print('▒' * 50)