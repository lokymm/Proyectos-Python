def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
    

def run():
    palabra = input("Ingresa una palabra o una frase: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo==True:
        print("La palabra ingresada es palindromo.\n")
    else:
        print("La palabra ingresada NO es palindromo.\n")



if __name__ == '__main__':
    run()


