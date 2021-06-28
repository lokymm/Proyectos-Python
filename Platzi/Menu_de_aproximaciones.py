

def EnumeracionExhaustiva(objetivo):
    resultado=0 #funciona como contador

    while resultado**2 < objetivo:
        resultado +=1
        
        
    if resultado**2 == objetivo:
        print(f"la raiz cuadrada de {objetivo} es '{resultado}'\n")

    else:
        print(f"la raiz cuadrada de {objetivo} no es un número entero\n")


def AproximacionDeSoluciones(objetivo):
    epsilon = 0.01  # es que tan cerca queremos llegar de la respuesta
    paso = epsilon**2 # que tanto nos vamos a ir acercando en cada iteración a la respuesta
    resultado=0.0 #funciona como contador

    while abs(resultado**2 - objetivo)>=epsilon and resultado<=objetivo:
        resultado +=paso

    if abs(resultado**2 -objetivo)>= epsilon:
        print(f'No se encontró la raiz cuadarda de {objetivo}')

    else:
        print(f'La raiz cuadrada de {objetivo} es {resultado}')
        

def BusquedaBinaria(objetivo):
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


def run():
    menu = """ Métodos de solución!!

            [1] Enumeración Exhaustiva
            [2] Aproximación de Soluciones
            [3] Busqueda Binaria


            Elige una opción: """


    opcion = input(menu)
    objetivo = int(input('\nIngresa un número entero: '))

    if opcion == '1':
        EnumeracionExhaustiva(objetivo)
    elif opcion == '2':
        AproximacionDeSoluciones(objetivo)
    else:
        BusquedaBinaria(objetivo)


if __name__=='__main__':
    run()