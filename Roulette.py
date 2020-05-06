import random as r

Banque = 100 # Solde du compte
Continuer = True # Variable permettant de  continuer ou non une partie

while Continuer: # Boucle permettant de relancer une partie
  print(f"Vous avez {Banque}€ en banque !") # Affiche l'argent en banque
  
  while True: # Vérifie s'il y a une erreur
    try:
      Mise = int(input("Combien souhaitez vous miser ? ")) # Somme misé
      Numero = int(input("Sur quel numéro vous souhaitez miser ?")) # Numéro sur lequel le joueur mise
      if Numero > 49: # Sur une roulette les numéros vont de 0 à 49
        raise Exception
      if Mise > Banque: # Lance une erreur si l'on mise plus que ce que l'on possède
        raise Exception  
      break 
    except:
      print("La mise et le numéro joué doivent être des nombres entiers. La mise ne doit pas être plus grande que l'argent que vous avez en banque") # Message d'erreur

  Gagnant = r.randrange(50) # Prend aléatoirement un numéro entre 0 et 49
  Banque = Banque - Mise # Soustrait l'argent misé

  print(f"\nIl vous reste {Banque}")
  print(f"Le numéro gagnant est le {Gagnant}\n")

  if Numero == Gagnant: # Si le numéro joué est égal au numéro gagnant alors on triple l'argent misé
    Banque = Banque + (Mise * 3) # Reversement des gains
    print (f"Vous avez trouvé le bon numéro gagnant. Vous gagnez {Mise*3}€.")

  elif Mise % 2 == Gagnant % 2: # Vérifie si le numéro joué est de la même couleur (Pair / Impair) que le numéro gagnant. On double alors l'argent misé
    Banque = Banque + (Mise * 2) # Reversement des gains
    print(f"Vous avez misé sur la bonne couleur. Vous gagnez {Mise*2}.")
  
  else: # Si le numéro gagnant n'est pas de la même couleur ou égal au numéro sur lequel le joueur mise alors il n'y a pas de gain
    print("Vous n'avez rien gagné.")

  if Banque <= 0: # Si le solde en banque atteint 0 alors la partie se termine
    print("Votre solde en banque est nul. Vous ne pouvez plus jouer.")
    Continuer = False # Termine la partie
  
  else: # Si il reste de l'argent sur le compte on demande au joueur s'il veut continuer
    print(f"Votre solde est de : {Banque} ! ")
    Left = input("\nSouhaitez vous quitter ? o/n :")
    
    if Left == "o" or Left == "O": # Si il tape o alors la partie s'arrête
      print(f"Vous quittez la partie avec un total de {Banque}€ !") # Annonce des gains
      Continuer = False # Stop la partie

