'''
Los condicionales como if siempre se ejecutan con expresiones
booleanas, nos ayudan a tomar decisiones mientras se ejecuta el 
código.

La primera condición que se cumpla es la que se va a ejecutar,
ignorando a las otra condiciones, en caso ne no haya, 
se ejecuta el dafault.
'''

print('▒' * 50)

# Tema de la clase, Condicionales

topic = '↓↓↓ Condicionales ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# Uso de if

if True:
    print('Se ejecuta la condición')

if False:
    print('Nunca se ejecuta la condición')

print('▒' * 50)

# Uso del if y else

stock = int(input('Ingrese el número de stock =>: '))

if (stock >= 100) and (stock <= 1000):
  print('la cantidad del stock es correcta'.upper())
else:
  print('el stock es incorrecto'.upper())

print('▒' * 50)

# Uso del if, elif y else

pet = input('¿Cuál es tu mascota favorita? =>: ')

if pet == 'perro':
  print('genial, los perros son el mejor amigo del hombre'.title())
elif pet == 'gato':
  print('genial, Los gatos son la compañía elegante y\nmisteriosa de los humanos'.title())
elif pet == 'pez':
  print('genial, Los peces nadan en silencio, pero su\npresencia tranquila llena de serenidad\nel corazón humano'.title())
else:
  print('Te falta alguna mascota en tu corazón')

print('▒' * 50)
