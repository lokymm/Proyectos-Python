import random



def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Ingresa un número entre 1: "))
    
    for i in range(1, 100):
        if numero_aleatorio == numero_elegido:
            print("Ganaste !!!")
            break
        if numero_elegido > numero_aleatorio:
           numero_elegido = int(input("Ingresa un número mas pequeño: ")) 
        else:
            numero_elegido = int(input("Ingresa un número mas grande: "))
    






if __name__ == '__main__':
    run()