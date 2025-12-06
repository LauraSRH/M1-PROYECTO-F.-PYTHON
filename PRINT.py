# # Ejemplos de la función print()
# print("Hola mundo")
# print("Hola mundo", "otra vez")
# print("Son las", 9, "de la mañana")
# print("el resultado de 3 * 4 es:", 3*4)

# Ejemplo de cadenas formateadas (%d se imprime un valor en el sistema decimal, el % representa el valor, en este ejemplo es 15)
print("el número 15 en el sistema decimal %d es, en el sistema octal %o es, en el sistema hexadecimal %x es" % (15, 15, 15))

# pi = 3.1416
# r = 5
# print(f"el radio de una circulo es {r} y su área es {pi * r ** 2 : .2f}") #.2f es para redondeado a dos decimales

# Impresión de carácteres especiales
print("La letra beta es: \n\t \u03B2") #\n es para pasar a otro renglon, \t para formato de tabla y u03B2 es el codigo asckii de beta

# Carácter de escape (para dar espacios , end = " ")
print("Hola mundo", end = " ")
print("otra vez", end = "\t")
print("y otra vez")

