# Función input sirve para capturar datos ingresados desde la terminal Python
# nombre = input("¿Cómo te llamas?")
# print("Hola" + nombre) 

# edad = input("¿Cuántos años tienes?")
# print(type (edad))
# print(f"{nombre} tiene {edad} años") 

# Programa que pide dos números al usuario y los suma (esto es para hacerle a una cadena <str> un cast)
numero1 = int(input("Introduce un número por favor: ")) # hay que poner <int> para que sume los numeros y los haga enteros
numero2 = int(input("Introduce otro número por favor: "))
numero3 = numero1 + numero2
print(f"El resultado de la suma es: {numero3}")

numero1 = (input("Introduce un número por favor: ")) # aqui va sin <int> y los junta
numero2 = (input("Introduce otro número por favor: "))
numero3 = numero1 + numero2
print(f"El resultado de la suma es: {numero3}")