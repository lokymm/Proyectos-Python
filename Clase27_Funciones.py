'''
Este código es para usar funciones en Python.
'''

def saludo(nombre):
    print("Hola {}".format(nombre))
    print("Bienvenidos amigos a esta prueba genial")
    print("Probaremos funciones en Python\n")


saludo("Marcelo")
print("\n")
saludo("Pedro")
print("\n")

nombre = input("Ingresa tu nombre: ")
print("\n")
saludo(nombre)

#--------------------------------------------
def resta(a,b):
    return a-b

resultado = resta(10,5)
print("El resultado es {}".format(resultado), "\n")