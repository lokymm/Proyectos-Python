print("*********************************")
print("* While con la sentencia Breack *")
print("*********************************\n")

contador=0

while contador< 10:
    contador += 1

    if contador== 5:
        break

    print("Valor actual de la variable", contador)

print("Fin del programa. La sentencia Breack se ha ejecutado.\n")

#Ejemplo para la sentencia Continue
print("***********************************")
print("* While con la sentencia Continue *")
print("***********************************\n")

contador = 0

while contador< 10:
    contador += 1

    if contador== 5:
        continue

    print("Valor actual de la variable", contador)

print("Fin del programa. La sentencia Breack se ha ejecutado.\n")