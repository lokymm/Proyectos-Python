def divisors(num):
    divisors=[]
    for i in range (1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors



def run():
    """En esta pieza de código manejaremos excepciones
    """
    try:
        num = int(input("Ingresa un numero:"))
        print(divisors(num))
        print ("Fin del Programa\n")
    
    except ValueError:
        print("Debes ingresar un número entero"
    
       







if __name__ == '__main__':
    run()