
print("###################################################")
print("Convertidor")
print("###################################################")
#Sentencias condicionales compuestas
print ("                                     ")
print("Menu de opciones")
print ("                                     ")

print("Presiona 1 para convertir de NUMERO a PALABRA")
print("Presiona 2 para convertir de PALABRA a NUMERO")

opcion = int(input("¿cuál es la opción deseada?  "))
print ("                                     ")

if opcion ==1:
    print("Convertir de NUMERO a PALABRA")
    print ("                                     ")
    numero = int(input("Que número deseas convertir: ?  "))
    print ("                                     ")
    if numero==1:
            print("El número es UNO ")
    elif numero==2:
            print("El número es DOS ")
    elif numero==3:
            print("El número es TRES ")
    elif numero==4:
            print("El número es CUATRO ")
    elif numero==5:
            print("El número es CINCO ")

    else:

            print ("Solo se puede convertir hasta el número CINCO")
            print ("                                     ")

if opcion ==2:
    print("Convertir de PALABRA a NUMERO")
    print ("                                     ")
    numero_nom = str(input("Que número deseas convertir: ? Escribe el nombre  "))
    print ("                                     ")
    if numero_nom=="uno":
            print("El número es 1 ")
    elif numero_nom=="dos":
            print("El número es 2 ")
    elif numero_nom=="tres":
            print("El número es 3 ")
    elif numero_nom=="cuatro":
            print("El número es 4 ")
    elif numero_nom=="cinco":
            print("El número es 5 ")

    else:

            print ("Solo se puede convertir hasta el número CINCO")
            print ("                                     ")
print ("                                     ")
print("Fin")
