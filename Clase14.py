
print("###################################################")
print("Comparador de Números")
print("################################################### \n")
#Operadores Relacionales


numero_1 = int(input("Ingresa el primer número a comparar: "))
numero_2 = int(input("\n Ingresa el segundo número a comparar: "))


if numero_1 == numero_2:
    print("\nSon Iguales\n")

else:
    print ("\nSon distintos \n")

if numero_1 < numero_2:
    print( str(numero_1) + " es menor que "+ str(numero_2) + "\n")

else:
    print ( str(numero_1) + " es mayor que "+ str(numero_2) + "\n")



print("\n Fin")
