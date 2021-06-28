#Este código sirve para encontrar si el número ingresado
#tiene una raíz cuadrada entera

objetivo=int(input("Ingresa un número entero: "))
resultado=0 #funciona como contador

while resultado**2 < objetivo:
    resultado +=1
    
    
if resultado**2 == objetivo:
    print(f"la raiz cuadrada de {objetivo} es '{resultado}'\n")

else:
    print(f"la raiz cuadrada de {objetivo} no es un número entero\n")