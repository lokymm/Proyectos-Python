'''
Este código es para probar métodos de cadenas String en Python.
'''

frase = ("Curso de Python")

frase[9]

lon = len(frase)

print(lon)
# Acá estoy transformado la cadena de caracteres

print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.replace("Python", "Control"))
print(frase.split())
print("\n")

# Desafio

nombre = input("Ingresa un nombre y apellido:")
print(nombre.upper(),"\n")
print(nombre.lower())

lista=(nombre.split())
union = "".join(lista)
print(union)
print("La cantidad de caracters de tu nombre es:",len(union), "\n")
