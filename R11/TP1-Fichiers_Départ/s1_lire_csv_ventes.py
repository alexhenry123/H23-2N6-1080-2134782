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


#Avec dictionnaire et liste vide
ls_client = []
with open('data_ventes.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    #Sauter les lignes
    for i in range(5):
        next(csv_reader)
    for line in csv_reader:
        ls_client += line
        id_client, nom, prenom = ls_client[0:3]
        for id in range(1,21):
            id_produit = ls_client[3:len(line)]
dict_client = {
        "ID client":id_client,
        "Nom client":nom,
        "Prenom client":prenom,
        "ID produit": id_produit}
print(dict_client)