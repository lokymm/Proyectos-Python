print ("Hola Mundo, Esta es la clase 9 - Tipos de Datos")

#Tipo de dato entero o largo

numero = 15
print(numero, type(numero))


#Tipo de dato flotante

numero_flot = 15.4
print(numero_flot, type(numero_flot))


#Tipo de dato Complejo

numero_compl = 6 + 2j
print(numero_compl, type(numero_compl))

#Tipo de dato String

var = "6 + 2j"
print(var, type(var))

#Tipo de dato Boolean

verdadero_falso = 3 == 4
print(verdadero_falso, type(verdadero_falso))

print("----------------------------------------------------------------------")

palab = str(input("ingresa una palabra :"))
num_ente = int(input("ingresa un número entero :"))
num_flota = float(input("ingresa un número con decimales :"))
num_complx = complex(input("ingresa un número complejo :"))

print(palab, type(palab))
print(num_ente, type(num_ente))
print(num_flota, type(num_flota))
print(num_complx, type(num_complx))
