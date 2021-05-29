
print("###################################################")
print("Convertidor")
print("################################################### \n")
#Sentencias condicionales anidadas

print("Menu de opciones \n")


print("Presiona 1 para convertir de NUMERO a PALABRA \n")
print("Presiona 2 para convertir de PALABRA a NUMERO \n")

opcion = int(input("¿cuál es la opción deseada? "))


if opcion ==1:
    print("\nConvertir de NUMERO a PALABRA \n")

    numero = int(input("Que número deseas convertir: ?  "))

    if numero==1:
            print("\n El número es UNO ")
    elif numero==2:
            print("\n El número es DOS ")
    elif numero==3:
            print("\n El número es TRES ")
    elif numero==4:
            print("\n El número es CUATRO ")
    elif numero==5:
            print("\n El número es CINCO ")

    else:

            print ("Solo se puede convertir hasta el número CINCO \n")


elif opcion ==2:
    print("\n Convertir de PALABRA a NUMERO \n")

    numero_nom = str(input("\n Que número deseas convertir: ? Escribe el nombre: "))
    numero_nom=numero_nom.lower()
    if numero_nom=="uno":
            print("\n El número es 1 ")
    elif numero_nom=="dos":
            print("\n El número es 2 ")
    elif numero_nom=="tres":
            print("\n El número es 3 ")
    elif numero_nom=="cuatro":
            print("\n El número es 4 ")
    elif numero_nom=="cinco":
            print("\n El número es 5 ")

    else:

            print ("Solo se puede convertir hasta el número CINCO \n")

else:
     print ("\n La opción no está disponible \n ")

print("\n Fin")
