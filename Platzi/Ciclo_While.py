def run():
    contador = 1
    
    numero = int(input("Ingresa la cantidad de números que elevarás al cuadrado: "))
    while contador<=numero:
        cuadrado=contador**2
        if cuadrado == 1024:
            break
        print("El cuadrado de "+str(contador)+" es "+str(cuadrado))
        contador+=1

if __name__ == '__main__':
    run()