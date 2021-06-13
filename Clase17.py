print("******************************************************")
print("* Programa que determina si el número es par o impar *")
print("******************************************************\n")

numero = int(input("Por favor introduce un número entero:"))
print("")
resultado = numero % 2

if resultado == 0:
    print("El número", numero , "es PAR \n")

else:
    print("El número", numero , "es IMPAR \n")


print("FIN\n")