import random

Relancer = True
while Relancer:
    l = random.randint(10000,50000) # On prends une valeur aléatoire entre 10 000 et 50 0000 qui nous servira de fourchette de prix
    Victoire = 0 # Nous permettra de calculer le nombre de victoire
    Defaite = 0 # Nous permettra de calculer le nombre de défaite
    
    while True: # Tant qu'il y aura une erreur la boucle nous fera recommencer la saisie
        try: # Nous vérifions s'il y a une erreur sur les entrées
            o = int(input("Insérez le nombre d'essais visé :")) # On insert le nombre d'essais que l'on souhaite avoir pour la partie
            break # Stop le While True et nous fait passer à la suite.
        except: # Si il y a une erreur alors se message s'affiche.
            print("\nVeuillez entrer une valeur numérique !") # Message d'erreur
    
    for m in range (0, o): # Relance la boucle fort tant qu'on a d'essais (Valeur défini précédemment)
        m = m + 1 # Incrémente la variable m à chaque essais
        
        while True: # Tant qu'il y aura une erreur la boucle nous fera recommencer la saisie
            try: # Nous vérifions s'il y a une erreur sur les entrées
                n = int(input("\nEssaie numéro " + str(m) + ":")) # On entre le prix
                break # Stop le While True et nous fait passer à la suite.
            except: # Si il y a une erreur alors se message s'affiche.
                print("\nVeuillez entrer une valeur numérique !") # Message d'erreur

        if n > l: # Vérifie si le prix donné est plus grand que le prix annoncé
            print("Au dessus du prix") 

        if n < l: # Vérifie si le prix donné est plus petit que le prix annoncé
            print("En dessous du prix")

        if n == l: # Vérifie si il y a un juste prix
            print("Bravo vous avez trouvé le juste prix qui était de ", l, "€ en ", m, "essais !")
            Victoire = Victoire + 1 # Incrémente 1 point de victoire
            break # Stop la boucle for
        
    if m == o: # Si m == 0 alors vous n'avez plus d'essais
        print("Vous avez perdu la valeur à trouver était de :", l, "€")
        Defaite = Defaite + 1 # Incrémente un point de défaite
    
    quitter = input("Voulez vous relancer une partie? (o/n) : ") # Permet de relancer une partie   
    if quitter == "n": # Si n alors on quitte le programme
        print(f"Merci d'avoir joué ! Tu as obtenu {Victoire} victoire(s) contre {Defaite} défaite(s) sur cette session") # Annonce le nombre de victoire et de défaite
        Relancer = False # Permet de couper la boucle While