#Este código sirve para encontrar si el número ingresado
#tiene una raíz cuadrada.

objetivo=int(input("Ingresa un número entero: "))
epsilon = 0.01

bajo=0.0     #Límite inferior del espacio numérico
alto= max(1.0, objetivo) #Límite superior del espacio numérico

respuesta = (alto + bajo) / 2

while abs(respuesta**2-objetivo)>=epsilon:
    print(f'bajo = {bajo}, alto = {alto}, respuesta= {respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
        
    respuesta = (alto + bajo) /2
print(f'La raiz cuadrada de {objetivo} es {respuesta}')

