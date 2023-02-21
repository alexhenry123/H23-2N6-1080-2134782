#  Exemple de boucles for imprimant les valeurs et leur index d'une liste.


def boucle_input_noms():
    liste_noms = list()
    valeur_input = input("Insrérer un nom (x pour quitter) : ")
    while valeur_input.upper() != "X" :
        liste_noms.append(valeur_input)
        valeur_input = input("Insrérer un nom (x pour quitter) : ")
    print()
    return liste_noms


liste_noms = boucle_input_noms()

for index in range(len(liste_noms)) :
    print(f"Nom {int(index)+1} : {liste_noms[index]}")

print(80*"_")


for nom in liste_noms:
    print(f"Nom {liste_noms.index(nom)+1} : {nom}")

print(80*"_")

