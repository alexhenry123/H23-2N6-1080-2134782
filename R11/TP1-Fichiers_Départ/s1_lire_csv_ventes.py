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


#Avec dictionnaire et liste
ls_client = []
with open('data_ventes.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for i in range(5):
        next(csv_reader)
    #Sauter les lignes
    for line in csv_reader:
        ls_client += line
        for i in range(1,21):
            pass
print(ls_client)

# dict_client = {
#         "ID client":id,
#         "Nom client":nom,
#         "Prenom client":prenom}
#print(dict_client)

#Avec liste vide
# ls_client2 = []
# with open('data_ventes.csv', 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)
#     for line in csv_reader:
#         ls_client2 += line
    #print(liste_client)