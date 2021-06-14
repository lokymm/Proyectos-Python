print("###################################################")
print("Operadores de Asignación")
print("################################################### \n")
#Uso de los operadores de asignación

mensaje = "Buen dia "
nombre = input("Ingresa tu nombre: ")

nacimiento = int(input("Ingresa el año de tu nacimiento: "))
años = 2021 - nacimiento


mensaje+= nombre
print()
print(mensaje, "tu edad es ", años, "años.\n")
print()
print("END\n")