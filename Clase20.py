print("###################################################")
print("Calculadora con una sola variable")
print("################################################### \n")

print("####################")
print("* Menu de opciones *")
print("#################### \n")

print("1 - Suma.")
print("2 - Resta.")
print("3 - Multiplicación.")
print("4 - Division.")
print("5 - División entera.")
print("6 - Potenciación.")
print("7 - Módulo o Resto.\n")

opcion = int(input("Elige una opción para realizar el cálculo:"))
print("")

if opcion == 1:
    print("Has seleccionado realizar una suma")
    numero1 = int(input("Ingresa el primer número a sumar: "))
    numero2 = int(input("Ingresa el segundo número a sumar: "))
    numero1 += numero2
    print("\nEl resultado es: ", numero1, "\n")

elif opcion == 2:
    print("Has seleccionado realizar una resta")
    numero1 = int(input("Ingresa el primer número a Restar: 'debe ser el mas grande' "))
    numero2 = int(input("Ingresa el segundo número a Restar: "))
    numero1 -= numero2
    print("\nEl resultado es: ", numero1, "\n")

elif opcion == 3:
    print("Has seleccionado realizar una multiplicación")
    numero1 = int(input("Ingresa el primer número a multiplicar: "))
    numero2 = int(input("Ingresa el segundo número a multiplicar: "))
    numero1 *= numero2
    print("\nEl resultado es: ", numero1, "\n")

elif opcion == 4:
    print("Has seleccionado realizar una división")
    numero1 = int(input("Ingresa el primer número a Dividir: 'Debe ser el mayor' "))
    numero2 = int(input("Ingresa el segundo número a Dividir: "))
    numero1 /= numero2
    print("\nEl resultado es: ", numero1, "\n")

elif opcion == 5:
    print("Has seleccionado realizar una división Entera")
    numero1 = int(input("Ingresa el primer número a Dividir: 'Debe ser el mayor' "))
    numero2 = int(input("Ingresa el segundo número a Dividir: "))
    numero1 //= numero2
    print("\nEl resultado es: ", numero1, "\n")

elif opcion == 6:
    print("Has seleccionado realizar una potencia")
    numero1 = int(input("Ingresa el primer número  - Base: "))
    numero2 = int(input("Ingresa el segundo número  - Exponente: "))
    numero1 **= numero2
    print("\nEl resultado es: ", numero1, "\n")

elif opcion == 7:
    print("Has seleccionado realizar el módulo o resto")
    numero1 = int(input("Ingresa el primer número  - Dividendo: "))
    numero2 = int(input("Ingresa el segundo número  - Divisor: "))
    numero1 %= numero2
    print("\nEl resultado es: ", numero1, "\n")

else :
    print("La opción elegida no está disponible.\n")

print("FIN\n")