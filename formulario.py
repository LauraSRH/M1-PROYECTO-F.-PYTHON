

# ============================================
# FORMULARIO DE INSCRIPCIÓN A CURSO
# ============================================

print("\n")
print("╔" + "═" * 48 + "╗")
print("║" + " " * 10 + "FORMULARIO DE INSCRIPCIÓN AL CURSO" + " " * 4 + "║")
print("╚" + "═" * 48 + "╝")
print()

# Captura de información del estudiante
nombres = input("Ingrese sus nombre(s): ").title()
apellidos = input("Ingrese sus apellido(s): ").title()
edad = input("Ingrese su edad: ")
pais = input("Ingrese su país: ").title()
curso = input("Ingrese el nombre del curso: ").title()

with open("inscripciones.txt", "a") as archivo:
    archivo.write(f"Nombre: {nombres}, Apellidos: {apellidos}, Edad: {edad}, País: {pais}, Curso: {curso}\n")

# Mostrar resumen de inscripción
print("\n")
print("╔" + "═" * 48 + "╗")
print("║" + " " * 15 + "✓ INSCRIPCIÓN COMPLETADA" + " " * 9 + "║")
print("╚" + "═" * 48 + "╝")
print()
print(f"Estudiante: {nombres.title()} {apellidos.title()}")
print(f"Edad: {edad} años")
print(f"País: {pais.title()}")
print(f"Curso: {curso.title()}")