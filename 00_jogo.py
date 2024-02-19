import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0
rounds = 1

while True:
  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  print('-' * 10)
  print('Computer wins =>: ', computer_wins)
  print('User wins =>: ', user_wins)
  print('-' * 10)

  rounds += 1

  user_option = input('piedra, papel o tijera =>: '.title()).lower()
  if user_option not in options:
      print('esa opcion no es valida'.capitalize())
      continue

  computer_option = random.choice(options)

  print(f'User option =>: {user_option}')
  print(f'Computer option =>: {computer_option}')

  
  if user_option == computer_option:
      print('empate!!!'.title())
  elif user_option == 'piedra':
      if computer_option == 'tijera':
          print('piedra gana a tijera'.title())
          print('user gana!!!'.upper())
          user_wins += 1
      else:
          print('papel gana a piedra'.title())
          print('computer gana!!!'.upper())
          computer_wins += 1
  elif user_option == 'papel':
      if computer_option == 'piedra':
          print('papel gana a piedra'.title())
          print('user gana!!!'.upper())
          user_wins += 1
      else:
          print('tijera gana a papel'.title())
          print('computer gana!!!'.upper())
          computer_wins += 1
  elif user_option == 'tijera':
      if computer_option == 'papel':
          print('tijera gana a papel'.title())
          print('user gana!!!'.upper())
          user_wins += 1
      else:
          print('piedra gana a tijera'.title())
          print('computer gana!!!'.upper())
          computer_wins += 1
  
  if computer_wins ==2:
      print('El ganador es la computadora')
      break
  if user_wins ==2:
      print('El ganador es el usuario')
      break
  

'''
def main():
  
# Iniciamos dando una explicacion breve del programa
  print('JUGUEMOS: PIEDRA, PAPEL O TIJERA!')
  print(' ')
  print('*'*60)
  print(' ')
  print('INSTRUCCIONES')
  print(' ')
  print('El juego consiste en la participacion de 2 jugadores')
  print('Cada jugador elije una de las opciones')
  print('Las combinaciones ganadoras son las siguientes: ')
  print('- Piedra gana a tijera')
  print('- Tijera gana a papel')
  print('- Papel gana a piedra')
  print(' ')
  print('*'*60)
  print(' ')  
  print('Elije una de las opciones teniendo en cuenta que:')
  print('1 - Piedra')
  print('2 - Tijera')
  print('3 - Papel')
  print(' ')
  print('*'*60)
  print(' ')
  print('ELECCION')
  print(' ')
  
  # Solicitamos los valores de los 2 jugadores
  
  gamer1 = input('Eleccion del jugador 1: ')
  gamer1 = int(gamer1)
  
  if gamer1 == 1:
    print('Piedra')
  elif gamer1 == 2:
    print('Tijera')
  elif gamer1 == 3:
    print('Papel')
  else:
    print('Eleccion no valida')
    
  gamer2 = input('Eleccion del jugador 2: ')
  gamer2 = int(gamer2)
  
  if gamer2 == 1:
    print('Piedra')
  elif gamer2 == 2:
    print('Tijera')
  elif gamer2 == 3:
    print('Papel')
  else:
    print('Eleccion no valida')
    
  #Realizamos el proceso logico para determinar quien es el ganador
    
  print(' ')
  print('*'*60)
  print(' ')
  print('RESULTADO')
  print(' ')
  
  if gamer1 == 1 and gamer2 == 2:
    print('El ganador es el jugador 1')
    print(' ')
    print('FELICITACIONES')
  elif gamer1 == 1 and gamer2 == 3:
    print('El ganador es el jugador 2')
    print(' ')
    print('FELICITACIONES')
  elif gamer1 == 2 and gamer2 == 3:
    print('El ganador es el jugador 1')
    print(' ')
    print('FELICITACIONES')
  elif gamer1 == 2 and gamer2 == 1:
    print('El ganador es el jugador 2')
    print(' ')
    print('FELICITACIONES')
  elif gamer1 == 3 and gamer2 == 1:
    print('El ganador es el jugador 1')
    print(' ')
    print('FELICITACIONES')
  elif gamer1 == 3 and gamer2 == 2:
    print('El ganador es el jugador 2')
    print(' ')
    print('FELICITACIONES')
  elif gamer1 == gamer2:
    print('Es un empate')
    print(' ')
    print('FELICITACIONES')
  else:
    print('Elecciones no validas vuelva a intentarlo')

if (__name__  ==  '__main__'):
  main()'''