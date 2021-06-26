'''
Este código es para realizar menús en Python.
'''

menu = """Bienvenidos al registro de usuarios, llene los campos que usted prefiera
a continuación seleccionando un número del 1 al 3:

[1] Digitar su nombre
[2] Digitar su edad
[3] Digitar su e-mail

"""
print(menu)

opcion = int(input("Ingrese la opción: "))

if opcion==1:
    nombre=input("Ingrese su nombre:")
    if nombre.isalpha()==True:
        print("Tu nombre es {}". format(nombre))
    else:
        print("Has digitado un nombre inválido.")
        
elif opcion==2:
    edad=input("Ingrese su edad:")
    if edad.isnumeric()==True:
        print("Tu edad es {}", format(edad))
    else:
        print("Has digitado un número inválido.")

elif opcion==3:
    mail=input("Ingrese su e-mail:")
    if mail.find("@")>=1 and mail.find(".")>=1:
        print("Tu mail es {}", format(mail))
    else:
        print("Has digitado un mail inválido.")

else:
    print("Opción incorrecta")

print("\nFin del programa\n")