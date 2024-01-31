def Nombre_premier(nombre):
    for i in range (2,nombre):
        if (nombre%i==0):
            print("NON PREMIER")
            break
    else :
        print("PREMIER")
a=int(input("Entrez le nombre"))
Nombre_premier(a)