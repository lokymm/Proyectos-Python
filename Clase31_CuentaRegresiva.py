'''
Este código es para realizar una cuenta regresiva.
'''




for contador in range(10,-1,-1):
    print (contador)

print("\nFUEGO !!! \n")

#Desafio 2 - Acá está el ciclo para encontrar los mñutiplos de 4 y su suma

      #Acá definímos los límites del rango
inf=int(input("Indicar el límite inferior del rango: "))
supe=int(input("Indicar el límite superir del rango: "))

     #Acumulado sumará los número múltiplos de 4 que hay en el rango
acumulado = 0
     #Acumulado contará los número múltiplos de 4 que hay en el rango
cuenta = 0 


for contador in range(inf,supe):
    if contador%4 == 0:
        acumulado = acumulado + contador
        cuenta = cuenta+1

print("\nLa suma de los",cuenta, "mútiplos de 4 es:",acumulado,"\n")

#Desafio 3 - Acá está el ciclo para encontrar el factorial de un número

base = int(input("Ingrese un número entero para calcular su factorial: "))
# Base2 decrementa la base para armar el factorial
factorial = base

print(str(base),"! =", str(base),"X ", end ='')

while base>1:
    base = base-1
    
    factorial=factorial*base

    print (str(base),end= '')
    
    if base > 1:
        print(" X ", end='')


print(" = ",factorial,"\n")