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
ls_clients = []
with open('data_ventes.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for i in range(5):
        next(csv_reader)
    #Saut des lignes
    for line in csv_reader:
        position = 0
        id_client, nom, prenom = line[0:3]
        for id in range(1,21):
            id_quantité = line[3:len(line)]
            ls_commandes = [position,line[id]]
            #id_quantité += ls_commandes
            position += 1
        dict_client = {
            "ID client": id_client,
            "Nom client": nom,
            "Prénom client": prenom,
            "Commande":{"ID produit": ls_commandes[0],"Quantité": ls_commandes[1]}}
        ls_clients += dict_client.items()
print(ls_clients)









