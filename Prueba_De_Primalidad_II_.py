def es_primo(numero):
    if numero !=2 and numero % 2 == 0 or numero !=3 and numero % 3 == 0 or numero !=5 and numero % 5 ==0 or numero !=7 and numero % 7 == 0:
       return False
    
    else:
        return True
    



def run():
    titulo = """Bienvenidos al verificador de PRIMALIDAD\n"""
    print(titulo)
    
    numero = int(input('Ingresa un número: '))
    if es_primo(numero):
        print('Es primo.\n')
    else:
        print("No es primo.\n")
                 




if __name__ == '__main__':
    run()