#TIPOS DE CADENAS
# textovariado = "palabra, 1, 2 3, #%&"
# print(type("texto variado"))

# print("""Funcionamiento de
# programa (opciones):
# -1 para acceder a opciones
# -2 para salir
#  """)

###############################################################
# Subscripting e indexado (los numeros negativos es que inicia contando de lado izq. P=0 -1=n que es la última)

texto = "Python"
# print(texto[0])
# print(texto[1])
# print(texto[4])
# print(texto[-1])
# print(texto[-2])
# print(texto[-6])

# print(texto[6]) # Error no podemos acceder a una posición de la letra que no existe
# print(texto[-7]) #Error, no podemos accedera a una posicón de la letra que no existe en la palabra

# letra = texto[0]
# print(letra)

# texto[0] = "p" # Error, no se puede invertir la asignación ya que lo tiene de origen, no se pude modificar la cadena

# letra = "p"
# print(letra)

#################################################

# Concatenación, cuando ejecutamos sumas con cadenas de texto
# texto_compuesto = letra + texto[1] # la letra <p> mas la letra <y>. Esto es una CONCATENACIÓN
# print(texto_compuesto) 


# SLICING O SUBSTRINGING
# texto = "Python"
# print(texto[0:3])
# print(texto[0:-3]) # la impresión deja fuera hasta el -3 o sea desde la h
# print(texto[0:-2]) # la impresión deja fuera hasta el 12 osea de la o en adelante
# print(texto[2:])
# print(texto[:3])

# print(texto[-3::-1])
# print(texto[::-1]) # del principio <:> al final <:>, en orden de -1 o sea de atras para adelante

# print(texto[0:50]) # en este caso usando el slicing no importa que se usen mas numeros, ya que se incluyen las posiciones de la palabra
# print(texto[2:2]) # en este caso sale nada al imprimir, porque aunque se inicia en la posicón 2, la ultima posición no se considera, por lo que queda en blanco.

##########################################################

#CADENAS Y FORMATOS
# texto = "Hola mundo! Buenastardes"
# print(texto.lower()) # todas minusculas
# print(texto.upper()) # todas mayusculas
# print(texto.capitalize()) # Solo la primera letra de la frase es mayuscula
# print(texto.title()) # Le da formato de titulo, a cada palabra le da mayuscula a la primera letra
# print(texto.swapcase()) # cambia la primera letra a miniscula y las demas a mayuscula en cada palabra

# texto = texto.upper()
# print(texto)

print("{} + {} = {}".format(2, 3, 2+3))
print("{} + {} = {}".format("Hola", "mundo", "Hola mundo"))
print("{:.3f} + {:.4f} = {}".format(2, 3, 2+3)) # <.f> y el numero indica los decimales es .float
print("{1} + {0} = {2}".format(2, 3, 2+3)) # los números entre los corchetes indican la posición de las variables en la formula
print("{2} + {0} = {1}".format("Hola", "mundo", "Hola mundo"))
print("{:d} = {:o} = {:x}".format(15, 15, 15))

