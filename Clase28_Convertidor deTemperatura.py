'''
Este código es para usar funciones en Python.
'''

print("*" *31)
print("* Convertidor de Temperaturas *")
print("*" *31, "\n")

def convertirCelsius(temp, unidad):
    if unidad == "K":
         return temp/9.8112
    elif unidad =="C":
         return temp*9.8112
    
    else:
        print("Debe ingresar la unidad de temperatura en grados Kelvin 'K' o Celsuis 'C'")

temp=int(input("Ingrese la temperatura:"))
unidad=input("""Ingrese la unidad de medida
 [K] = Kelvin a Celsius
 [C] = Celsius a Kelvin
 """)

c = convertirCelsius(temp, unidad)
print("Temperatura =", c)
