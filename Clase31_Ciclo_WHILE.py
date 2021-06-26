'''
Este código es para probar BUCLES en Python.
Acá probaremos el Bucle WHILE

'''

contador=0
repeticiones = int(input("Indique el número de repeticiones que necesita: "))

stop =input("Desea frenar el Bucle?  Y / N :")
if stop == "Y":
    numero = int(input("Ingrese en que numero de vuelta desea frenar:"))
else:
    print("Continuamos...")


while contador<=repeticiones:
    print("El valor del contador es:", contador)
    if contador==numero:
        break
    contador = contador+1

print("\nEl bucle ha finalizado\n")