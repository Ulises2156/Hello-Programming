nota = int(input("Ingrese la nota: "))

if(nota>=0 and nota<=100):
    if(nota <= 39):
        print("Desaprobado")
    else:
        if(nota<=79):
            print("Aprobado")
        else:
            print("Promocionado")
else:
    print("Ingrese una nota valida")
