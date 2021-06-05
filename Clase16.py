print("###################################################")
print("Sistema de clculo de Dias de Vacaciones RAPPI")
print("################################################### \n")

nombre= input("¿Ingrese su nombre y Apellido?: ")
Area= input("¿Ingrese Clave de area a la que pertenece?: \n Clave1 = Atención al Cliente\n Clave2 = Logística \n Clave3 = Gerencia \n")
antiguedad= int(input("¿Ingrese su antiguedad en Años?:" ))

if Area=="Clave1":
    print("Area Atención al Cliente.")

    if antiguedad ==1:
        print("Corresponden 6 dias de Vacaiones.")

print("FIN")
