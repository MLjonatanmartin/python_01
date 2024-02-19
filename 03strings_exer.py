'''
Programa para imprimir el nombre, apellido y edad del usuario
'''

print('▒' * 90)

greeting_message = 'Bienvenido a BATTLE CAT'.center(90)

print(f'\n{greeting_message}\n')

print('▒' * 90)

print('-' * 90)

print('Para poder iniciar a jugar BATTLE CAT, por favor cree un usario ↓↓↓')

print('-' * 90)

user_name = input('Por favor, digite el nombre de su usuario: ')
user_nick_name = input('Por favor, digite el apodo de su usuario: ')
user_hability = input('Por favor, digite la habilidad del usuario: ')

print('-' * 90)

print('▒' * 90)
print('-' * 90)

user_presentation = f'Bienvenido a BATTLE CAT {user_name}\ntambién conocido como {user_nick_name}\ncon su habilidad rotisima {user_hability}'

print(f'\n{user_presentation}\n')

print('-' * 90)

print('▒' * 90)

print('--> Iniciar Partida <--')

print('▒' * 90)