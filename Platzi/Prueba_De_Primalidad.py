def es_primo(numero): #El usuario ingresa el número.
    contador = 0
    
    for i in range(1,numero+1):
        if i == 1 or i == numero:
            continue        # Si la vuelta del ciclo = 1 o = numero; saltar la vuelta
        if numero % i == 0: # Si el número es divisible por otro que no sea 1 o si mismo, entonces no es primo
            contador +=1    # y aumentamos el contador en 1
    
    if contador == 0:
        return True
    else:
        return False

def run():
    titulo = """Bienvenidos al verificador de PRIMALIDAD\n"""
    print(titulo)
    
    numero = int(input("Ingresa un número: "))
    if es_primo(numero):
        print("Es primo\n")
    
    else:
        print("No es primo.\n")
   


if __name__ == '__main__':
    run()