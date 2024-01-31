def Calcul_Heure(h_supp,salaire):
    if (h_supp<=39):
        print("Desolee vous n'avez pas de surplus")
    if(h_supp>=40 and h_supp<=44):
        salaire =salaire + salaire*0.5
        print (f"Vous avez {salaire}")
    if(h_supp>=45 and h_supp<=49):
            salaire = salaire +salaire*0.75
            print (f"Vous avez {salaire}")
            
    if(h_supp>=50 and h_supp<=100):
            salaire = salaire + salaire*0.5
            print (f"Vous avez {salaire}")
            
a=float(input("Entrer le nombre d'heure supplémentaire"))
b=float(input("Entrer votre salaire"))
Calcul_Heure(a,b)