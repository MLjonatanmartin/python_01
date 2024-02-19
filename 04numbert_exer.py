'''
Programa para hacer promedio de gastos trimestral.
Input: 
    -meses a evaluar.
    -gastos totales de cada mes.
    -cantidad de ingresos totales por mes.
Output:
    -Promedio de gastos totales.
    -Analisis de déficit o superávit.
    -Recomendaciones.
'''

print('▒' * 70)

greeting_message = 'Bienvenido a FinasAPP Tu app'.center(67)

print(f'\n{greeting_message}\n')

print('▒' * 70)

print('-' * 70)

print('Para hacer el calculo trimestral, ingrese los siguiente datos ↓↓↓')

print('-' * 70)

print('▒' * 70)

# Input de meses a calcular

month_1 = input('Por favor, digite el primer mes =>: ')
month_2 = input('Por favor, digite el segundo mes =>: ')
month_3 = input('Por favor, digite el tercer mes =>: ')

print('▒' * 70)

# Input de gastos a calcular

mont_expenses_1 = int(input(f'Por favor, digite los gastos totales de {month_1} =>: '))
mont_expenses_2 = int(input(f'Por favor, digite los gastos totales de {month_2} =>: '))
mont_expenses_3 = int(input(f'Por favor, digite los gastos totales de {month_3} =>: '))

print('-' * 70)

# Input de ingresos a calcular

mont_income_1 = int(input(f'Por favor, digite los ingresos totales de {month_1} =>: '))
mont_income_2 = int(input(f'Por favor, digite los ingresos totales de {month_2} =>: '))
mont_income_3 = int(input(f'Por favor, digite los ingresos totales de {month_3} =>: '))

print('-' * 70)

print('▒' * 70)

print('-' * 70)

load = 'CALCULANDO'.center(67)

print(load)

print('-' * 70)

print('▒' * 70)

# Promedio de gastos 
total_expenses = mont_expenses_1 + mont_expenses_2 + mont_expenses_3
average_total = total_expenses / 3

# Promedio de gastos
total_income = mont_income_1 + mont_income_2 + mont_income_3
average_income = total_income / 3

print('⌂' * 70)

print(f'En los tres meses has tenido un gasto total de {total_expenses}\nCon un promedio mensual de gastos {average_total}')

print('⌂' * 70)

print(f'En los tres meses has tenido un ingreso total de {total_income}\nCon un promedio mensual de ingresos {average_income}')

print('⌂' * 70)

print('▒' * 70)

# Logica para analisis de deficit o superavit ↓↓↓

if total_expenses == total_income:
    print('Actualmente, gastas tanto como ganas al mes.\nSugerimos explorar nuevas fuentes de ingresos para poder ahorrar.')
elif total_expenses > total_income:
    print(f'Actualmente tienes un déficit de {total_expenses - total_income},\nSugerimos recortar gastos y buscar nuevas fuentes de ingresos.')
else:
    print(f'En Buena Hora, actualmente tienes un superávit de {total_income - total_expenses},\nAconsejamos ahorrar e invertir tu dinero en beneficiosas oportunidades.')

print('▒' * 70)

end = 'Gracias por tomar nuestros servicios'.center(70)

print(f'\n{end}\n')

print('▒' * 70)