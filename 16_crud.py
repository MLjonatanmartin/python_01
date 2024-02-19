'''
Lo más importante para trabajar con una lista, es saber manejar y usar el acronimo de CRUD

CRUD: Create, Read, Update and Delete 

Métodos de las listas:

    1-.append(value): Agrega elementos en la ultima posición de la lista.
    2-.insert(indexing, value): resive dos argumentos, el primero es la posición donde se va a 
        colocar el nuevo valor, que es el segundo argumento. 
    3-.index(value): Nos dice la posición indexada del valor.
    4-.remove(value): Nos sirve para eliminar elementos especificos de la lista.
    5-.pop(): Por defecto elimina el ultimo elemento de la lista, también se le puede enviar 
        un argumento de posicion para que elimine esa posicion especifica.
    6-.reverse(): reordena la lista desde el punto final al comienzo.
    7-.sort(): ordena los valores int de la lista de menor a mayor, los string en el orden del abecedario,
        da un error cuando intentas mesclar una lista con tipos de datos variados.
'''
print('▒' * 50)

# Metodos de las Listas
topic = '↓↓↓ Metodos de Las Listas ↓↓↓'.center(50) # metodo para centrar texto en consola
print(f'\n{topic}\n')

print('▒' * 50)

# ejemplo de una lista 

numbers = [1, 2, 3, 4, 5]
print(numbers[1])

print('▒' * 50)

# update una lista
print()
numbers[-1] = 10
print(f"Lista update {numbers}")

print('▒' * 50)

# método de .append(value)
numbers.append(700)
print(f'Metodo .append(700) con numbers =>: {numbers}')

print('▒' * 50)

# método de .istert(indexing, value)
numbers.insert(0, 'hola')
print(f'Merodo .insert(0,\'hola\') con numbers =>: {numbers}')

numbers.insert(3, 'change')
print(f'Merodo .insert(3,\'hola\') con numbers =>: {numbers}')

print('▒' * 50)

# unir lista, uso de operador =

task = ['todo1', 'todo2', 'todo3']
new_list = numbers + task

print(f'Nueva lista =>: {new_list}')

print('▒' * 50)

# Uso del metodo index
index = new_list.index('todo2')

# update de la lista
new_list[index] = 'todo changed'

print(new_list)
print(new_list[9])

print('▒' * 50)

# metodo para eliminar .remove(value)

print(new_list)
new_list.remove('todo1')
print(new_list)

print('▒' * 50)

print(new_list)
new_list.pop()
print(new_list)
new_list.pop(0)
print(new_list)

print('▒' * 50)

# uso de .reverse

print(new_list)
new_list.reverse()
print(new_list)

print('▒' * 50)

# uso de sort()

numbers_a = [1, 4, 6, 3]
print(numbers_a)
numbers_a.sort()
print(numbers_a)

print('▒' * 50)

# uso de sort() con strigs

string = ['re', 'ab', 'ed']
print(string)
string.sort()
print(string)

print('▒' * 50)
