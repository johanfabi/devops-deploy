# AWS Python Lambda Function Hello World Example
import random

def mezclar_nombre(nombre):
    """Mezcla aleatoriamente las letras de un nombre."""
    letras = list(nombre)  # Convierte el nombre en una lista de letras
    random.shuffle(letras)  # Reordena la lista de forma aleatoria
    nombre_mezclado = "".join(letras)  # Une las letras en un nuevo string
    return nombre_mezclado

# Ejemplo de uso:
nombre_original = input("Ingresa un nombre: ")
nombre_mezclado = mezclar_nombre(nombre_original)
print("Nombre mezclado:", nombre_mezclado)
