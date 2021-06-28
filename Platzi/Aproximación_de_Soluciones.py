#Este código sirve para encontrar si el número ingresado
#tiene una raíz cuadrada.En caso que no tenga una raiz exacta
#nos devolverá una aproximación.

objetivo=int(input("Ingresa un número entero: "))
epsilon = 0.01  # es que tan cerca queremos llegar de la respuesta
paso = epsilon**2 # que tanto nos vamos a ir acercando en cada iteración a la respuesta
resultado=0.0 #funciona como contador

while abs(resultado**2 - objetivo)>=epsilon and resultado<=objetivo:
    resultado +=paso

if abs(resultado**2 -objetivo)>= epsilon:
    print(f'No se encontró la raiz cuadarda de {objetivo}')

else:
    print(f'La raiz cuadrada de {objetivo} es {resultado}')