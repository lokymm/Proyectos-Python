print("###################################################")
print("Sistema de cálculo de Dias de Vacaciones RAPPI")
print("################################################### \n")

nombre= input("¿Ingrese su nombre y Apellido?: ")

Area= int(input("¿Ingrese Clave de area a la que pertenece?: \n Clave 1 = Atención al Cliente\n Clave 2 = Logística \n Clave 3 = Gerencia \n"))
print("---------------------------------- \n")
antiguedad = float(input("¿Ingrese su antiguedad en Años?:" ))
print("---------------------------------- \n")

if Area==1:
    print("Area Atención al Cliente. \n")

    if antiguedad ==1:
            print("al Sr:", nombre ,"Corresponden 6 dias de Vacaciones. \n")
    if antiguedad >1 and antiguedad <= 6:
            print("al Sr:", nombre ,"Corresponden 14 dias de Vacaciones. \n")
    if antiguedad > 6:
            print("al Sr:", nombre ,"Corresponden 20 dias de Vacaciones. \n")
    if antiguedad < 1:
            print("al Sr:", nombre ,"NO Corresponden Vacaciones. \n")

elif Area==2:
    print("Area Logística. \n")

    if antiguedad ==1:
            print("Corresponden 7 dias de Vacaciones. \n")
    if antiguedad > 1 and antiguedad <= 6:
            print("Corresponden 15 dias de Vacaciones. \n")
    if antiguedad > 6:
            print("Corresponden 22 dias de Vacaiones. \n")
    if antiguedad < 1:
            print("al Sr:", nombre ,"NO Corresponden Vacaciones. \n")

elif Area==3:
    print("Area Gerencia.\n")

    if antiguedad ==1:
            print("Corresponden 10 dias de Vacaciones. \n")
    if antiguedad > 1 and antiguedad <= 6:
            print("Corresponden 20 dias de Vacaciones. \n")
    if antiguedad > 6:
            print("Corresponden 30 dias de Vacaciones. \n")
    if antiguedad < 1:
            print("al Sr:", nombre ,"NO Corresponden Vacaciones. \n")

else:
    print("La Clave ingresada " ,Area, "es Incorrecta. Por favor Ingrese nuevamente")


print("FIN")
