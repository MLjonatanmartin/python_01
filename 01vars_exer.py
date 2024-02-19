'''
Programa para agendar citas
input usuario nombre, edad, identificacion.
output mensaje con los datos y la cita asignada
'''

print('▒' * 70)

greeting_message = 'Bienvenido a EPS Salud y Bienestar'.center(70)

print(f'\n{greeting_message}\n')

print('▒' * 70)

print('-' * 70)

print('Para poder agendar su cita, diligencie los siguientes datos ↓↓↓')

print('-' * 70)

user_name = input('Por favor, digite el nombre del paciente: ')
user_age = input('Por favor, digite la edad del paciente: ')
user_identification = input('Por favor, digite la identificación del paciente: ')

print('-' * 70)

print('▒' * 70)

user_healt_specialty = input('Por favor, Digite la especialidad de la cual desea ser atentido\n')

print('▒' * 70)

print('-' * 70)

print('Hay disponibilidad para el mes de Junio')

print('-' * 70)

user_date = input('Digite el día que desea ser atendido: ')

print('▒' * 70)

print('-' * 70)

health_appointment_date = 'CITA DEL PACIENTE'.center(70)

print(f'\n{health_appointment_date}\n')

print('-' * 70)

print('NOMBRE: ' + user_name)
print('EDAD: ' + user_age)
print('IDENTIFICACION: ' + user_identification)
print('ESPECIALIDAD: ' + user_healt_specialty)
print('FECHA: Junio/' + user_date + '/' + '2024')

print('-' * 70)

print('▒' * 70)

end = 'Gracias por tomar nuestros servicios'.center(70)

print(f'\n{end}\n')

print('▒' * 70)