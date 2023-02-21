# Boucle for untilisant l'index d'une liste. 
# Utilisez le débogueur pour voir les valeurs prise par les différentes variables lors de l'exécution.


liste_cours = ["Prog 1", "Math", "Bureautique"]
print(liste_cours)

longueur_liste_cours = len(liste_cours)
print(longueur_liste_cours)

liste_de_positions_itérable = range(longueur_liste_cours)
print(liste_de_positions_itérable)


for index in range(len(liste_cours)) :
    print(f"Bienvenue au cours {index} : ")
    print(liste_cours[index])