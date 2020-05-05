import random
Relancer = True

while Relancer:
    l = random.randint(10000,50000)
    Victoire = 0
    Defaite = 0
    o = int(input("Insérez le nombre d'essais visé :"))
    for m in range (0, o):
        m = m + 1
        while True:

            try:
                n = int(input("Essaie numéro " + str(m) + ":"))
                break
            except: 
                print("\nVeuillez entrer une valeur numérique !")

        if n > l:
            print("Au dessus du prix")

        if n < l:
            print("En dessous du prix")

        if n == l:
            print("Bravo vous avez trouvé le juste prix qui était de ", l, "€ en ", m, "essais !")
            Victoire = Victoire + 1
            break
        
    if m == o:
        print("Vous avez perdu la valeur à trouver était de :", l, "€")
        Defaite = Defaite + 1
    
    quitter = input("Voulez vous relancer une partie? (o/n)")
    if quitter == "n":
        print(f"Merci d'avoir joué ! Tu as obtenu {Victoire} victoire(s) contre {Defaite} défaite(s) sur cette session")
        Relancer = False