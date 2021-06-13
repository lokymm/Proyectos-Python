print("###################################################")
print("Uso de operadores Lógicos")
print("################################################### \n")
#Operadores Lógicos-

#Conjunción
print("Conjunción AND \n")

num1 = int(input("Ingrese un número mayor a 2 y menor a 5: "))

if num1>2 and num1<5:
    print("El número" ,num1, "cumple la condición \n")

else:
    print("El número" ,num1, "NO cumple la condición \n")

print("FIN \n")


#Disyunción
print("Disyunción OR \n")

palabra = input("Ingrese la palabra SI o YES : ")

if palabra =="si" or palabra=="yes":
    print("La palabra " ,palabra, "cumple la condición \n")

else:
    print("La palabra " ,palabra, "NO cumple la condición \n")

print("FIN \n")


#Negación
print("Negación NOT \n")

num2 = int(input("Ingrese un número IGUAL a 5: "))

if not num2==5:
    print("El número" ,num2, "es diferente de 5 y cumple la condición \n")

else:
    print("El número" ,num2, "es igual a 5 y NO cumple la condición \n")

print("FIN \n")
