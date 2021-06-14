print("*******************************************************")
print("* Programa para determina que número es el mas grande *")
print("*******************************************************\n")

numero1 = int(input("Por favor introduce el primer número entero:"))
print("")
numero2 = int(input("Por favor introduce el segundo número entero:"))
print("")
numero3 = int(input("Por favor introduce el tercer número entero:"))
print("")

if numero1>numero2 and numero1>numero3:
 print("El número", numero1, "es el mas grande.\n")

elif numero2>numero1 and numero2>numero3:
    print("El número", numero2, "es el mas grande.\n")

else:
    print("El número", numero3, "es el mas grande.\n")

print("FIN\n")