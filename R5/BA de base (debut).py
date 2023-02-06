# On veut une liste de chiffres
list_chiffres = [0, 8, 16, 19, 20]

# On veut une liste de fruits
list_fruits = ['ananas', 'orange', 'kiwi', 'clémentine', 'pomme']

# Pour imprimer chaque élément de la liste de chiffres




# Pour imprimer chaque élément de la liste de fruits



    
# Pour avoir le total de tous les chiffres de la liste de chiffres
long = len(list_chiffres)


# Pour avoir le nombre de chiffres dans la liste de chiffres
total = 0
for chiffre in list_chiffres:
    total += chiffre
print(f"Le total est : {total}")


# Pour avoir la moyenne de tous les chiffres de la liste de chiffres
moyenne = total / len(list_chiffres)-1
print(moyenne)


# Pour imprimer seulement les chiffres qui sont supérieurs à 50


 # Pour compter le nombre de chiffres qui sont supérieurs à 50   
 #      AVANT la boucle: Il me faut penser à créer une variable compteur qui va commencer à 0 
 #      DANS la boucle, si la condition est vraie, je vais augmenter le compteur de 1
 #      APRÈS la boucle, on imprime le résultat





 

 # Pour avoir le total des chiffres qui sont supérieurs à 50   
 #      AVANT la boucle: Il me faut penser à créer une variable total qui va commencer à 0 
 #      DANS la boucle, si la condition est vraie, je vais augmenter ce total de la valeur du chiffre
 #      APRÈS la boucle, on imprime le résultat

compteur = 0
for chiffre in list_chiffres:
    if chiffre > 50:
        compteur+=1
print(compteur)


 # Pour avoir la moyenne des chiffres qui sont supérieurs à 50   
 #      AVANT la boucle: 
 #                  Il me faut penser à créer une variable compteur qui va commencer à 0 
 #                  Il me faut penser à créer une variable total qui va commencer à 0 
 #      DANS la boucle, si la condition est vraie,
 #                  je vais augmenter le compteur de 1
 #                  je vais augmenter ce total de la valeur du chiffre
 #      APRÈS la boucle, 
 #                  on calule la moyenne et on imprime le résultat
total = 0
compteur = 0
for chiffre in list_chiffres:
    if chiffre > 50:
        total+=chiffre
        compteur+=1
moyenne = total / compteur
print(f"Voici la moyenne des nombres supérieurs à 50 : {moyenne}")



  

# Maintenant les f-string sont utiles pour avoir un résultat plus clair.
# On commence par écrire le texte qu'on veut imprimer
# Il y a X chiffres dans la liste et le total est Y
#                            print(f"Il y a X chiffres dans la liste et le total est Y")
# Ensuite on remplace le X par {compteur}  et le Y par {total}

