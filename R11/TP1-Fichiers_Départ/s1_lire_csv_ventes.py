import os
import csv
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

# Vous devez lire et extraire les informations du csv "data_ventes.csv"
# Le format de ce csv ne permet pas d'extraire les données très facilement.
# Regardez-le avant de commencer.

# Pour chaque client, il y la quantité de chacun des produits qu'ils ont achetés. 
# Les ids des produits sont dans l'en-tête et en ordre. 
# Donc les valeurs dans la colonne prodID1 correspondent à la quantité du produit dont l'ID est 1.
# Il en est ainsi pour chacun des 20 produits disponibles.

# Le but ultime de ce script est d'arriver à une liste, contenant pour chaque client


#Avec dictionnaire
with open('data_ventes.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    #next(csv_reader)
    liste_client = {"ID client",
                "Nom client",
                "Prenom client",
                "Commande client"}
    for line in csv_reader:
        liste_client.update(line)
    print(liste_client)


#Avec liste vide
liste_client = []
with open('data_ventes.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        liste_client += line
    #print(liste_client)