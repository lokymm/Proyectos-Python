def conversion(moneda):
    pesos = float(input(moneda))
    cotiz_dolar = float(input("ingrese la cotización del DOLAR :"))

    conversion=pesos/cotiz_dolar

    print("La cantidad de dólares equivalente es: U$S", conversion,"\n")




print("*" *28) 
print("*   Conversor de MONEDAS   *")
print("*" *28)

menu = """Bienvenidos al conversor de monedas a DOLARES, 
a continuación seleccione una opción:

[1] Pesos Argentinos
[2] Pesos Mexicanos
[3] Pesos Colombianos

"""
print(menu)

opcion=int(input("Ingrese la opción:"))

if opcion == 1:
    conversion("Ingrese la cantidad de dinero en PESOS ARGENTINOS: ")
    
    
elif opcion ==2:
   conversion("Ingrese la cantidad de dinero en PESOS MEXICANOS: ")
    

elif opcion == 3:
    conversion("Ingrese la cantidad de dinero en PESOS COLOMBIANOS: ")
    

else:
    print("Ha ingresado una opción NO VALIDA.\n")

print("FIN DEL PROGRAMA. \n")