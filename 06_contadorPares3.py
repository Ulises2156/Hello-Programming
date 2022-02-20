inicio = int(input("Ingrese el numero de incio: "))
fin = int(input("Ingrese el numero de fin: "))

for i in range(inicio,fin):#Iterativa para
    if(i%2==0):
        print(str(i) + " es un numero par")
    else:
        print(str(i) + " es un numero impar")

print("Teremion")