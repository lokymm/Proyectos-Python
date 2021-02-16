
print ("Hola Mundo, soy Marcelo y estoy aprendiendo Python")

#Soy un comentario de línea

"""
Esto es texto que no se va a interpretar
Esto es texto que no se va a interpretar
Esto es texto que no se va a interpretar
Esto es texto que no se va a interpretar
"""

texto = "Estoy aprendiendo Python"
nombre = "Marcelo"
edad = 45
año=2021

print(texto) #estoy imprimiendo la variable

#Entrada de datos por parte del usuario
webpage= input("¿Cuál es tu página web? :" )

print("tu página es" + " " + webpage)

#Condicionales
"""
altura= int(input("Cuál es tu altura? introduce el valor en cm.  "))



if altura >= 180:
    print("Eres una persona alta.")
else:
    print("Eres bajito.")
"""

#Funciones
def mostrarAltura():
    altura= int(input("Cuál es tu altura? introduce el valor en centímetros.  "))



    if altura >= 180:
        print("Eres una persona alta.")
    else:
        print("Eres bajito.")


mostrarAltura()

#Listas

Personas = ["paco","Pepe","Victor"]

print(Personas[2])

for persona in Personas:
    print("-" + persona)

#prueba
