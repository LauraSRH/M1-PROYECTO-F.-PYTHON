# Operadores aritméticos - Control k c para hcer comentario de la selección Control k u para quitar la selección de comentarios
print (2 + 2)
print (4 - 2)
print (7 * 3)
print (15 / 2)
print (11 % 4) # operador módulo, nos da el residuo de la división, es lo que sobra de la división
print (11 // 4) # operador división de piso, nos da el numero de veces que cabe el 4 en el 11, que es 2
print (2 ** 3) # operador potencia, dos signos de multiplicación seguido de la potencia, en este caso es al cubo por eso es 3

# Operadores en cadenas de texto
print("Hola" + "mundo") # Concatenación cuando sumas cadenas de textos
print("Hola" * 3) # Repetición cuando es multipliación de adena de textos
print("Hola" + "mundo" * 3) # Concatenación y repetición

print("Hola " + "mundo")

# Operadores de comparación Son de tipo booleano
# print("Hola" == "hola") # == igual que
# print("Hola" != "hola") # != distinto que
# print(3 > 11) # Mayor que, menor que
# print(10 >= 11) # Mayor o igual que
# print(10 <= 10) # Mwenor o igual que

# Operadores de existencia
# print("ola" in "Hola") # in de existencia
# print("ola" not in "Hola") # not in de inexistencia

# Operadores booleanos
# print(True or False) # or verifica se cumple sólo una de las dos condiciones, da verdadero, porque una se cumple
# print(True and False) # and verifica que se cumplen las dos, da falso porque no se pueden cumplir ambas

# Operadores de asignación, se pueden asignar a cualquier operador aritmético
# x = 1 # Operador de asignación estándar
# x += 2 # operador de asingación suma de asignación estándar
# x *= 3 # Operador de asignación multiplicación, en este caso multiplica el resultado anterio por el 3
# x %= 4 # Operador de asignación módulo
# print(x)

x = 6 * 5 + 8 / 2 ** 4
print(x)