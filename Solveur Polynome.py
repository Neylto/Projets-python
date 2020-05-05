from math import sqrt

while True: #Tant qu'il y a une erreur la boucle nous fera recommencer la saisie
  try: #Nous vérifions si il y a une erreur sur les entrées
    a = int(input("a :")) # Nous définissons la variable A
    b = int(input("b :")) # Nous définissons la variable B
    c = int(input("c :")) # Nous définissons la variable C
    if a==0: # Si A = 0 alors ce n'est plus un polynome donc nous vérifions que A est différents de 0
      raise Exception #Déclenche une erreure si A est nul.
    break # Stop le While True et nous fait passer à la suite.
  except: #Si il y a une erreur alors se message s'affiche.
    print("A,B et C doivent être des valeurs entières et A différents de 0 ! Recommencer votre saisie :") #Message d'erreur

print(f"\nVoici notre trinome {a}x² + {b}x + {c}") # Nous affichons le trinome

D = b*b-(4*a*c) # Nous Calculons le delta.
print("Le Delta est égale à", D,"\n") # Nous affichons la valeur de delta

if D > 0: # Si D plus grand que 0
  print("Sachant que delta est positif nous calculons les deux racines x1 et x2")
  x1 = round((-b+sqrt(D))/(2*a),2) # Nous calculons x1
  print("La valeur de x1 est égal à", x1) # Nous affichons x1
   
  x2 = round((-b-sqrt(D))/(2*a),2) # Nous calculons x2
  print("La valeur de x2 est égal à", x2) # Nous affichons x2
    
  print(f"La forme factorisable est :, {a},(x - {x1}=,)(x - {x2})") # Nous affichons la forme factorisé

if D == 0: # Si D est égale à 0
  print("Sachant que le delta est égale à 0, l'équation à une racine unique") 
  x0 = round((-b)/(2*a),2) # Nous calculons x0
  print("La valeur de x0 est égale à", x0) # Nous affichons x0
  
if D < 0: # Nous vérifions que le Delta n'est pas inférieur à 0, si il l'est alors il n'y a pas de solution dans les réels.
  print("L'équation n'a pas de solution dans le domaine des réels")
