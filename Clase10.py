print("Sistema para calcular el Promedio Académico")

print("BIENVENIDO")
print("----------------------------------------------------------------------")

nombre = (input("Cuál es tu nombre ?  "))
matematicas = float(input(nombre+" Cuál es tu calificación en matemáticas? "))
quimica = float(input(nombre+" Cuál es tu calificación en química? "))
fisica = float(input(nombre+" Cuál es tu calificación en física? "))

Prome = (matematicas+quimica+fisica)/3

print(nombre + " Tu promedio es :" + str(round(Prome,3)))

if Prome >= 7:
    print ("Felicitaciones !!!!" + nombre + " Aprobaste con un promedio de: " + str(round(Prome,2)))

else:

    print ("Estudia un poco mas.")

print("Fin")
