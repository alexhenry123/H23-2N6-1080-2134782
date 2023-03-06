import csv
import os
os.chdir(os.path.dirname(__file__))

# Q3
# Ouvrez le ficher en lecture
# Utilisez le module csv pour lire le contenu du fichier
# Sautez la première ligne contenant les en-têtes
# Ajoutez chaque ligne à la variable list_client
# Finalement, imprimer la variable list_client

nom_fichier = "fichier_a_lire.csv"
list_client = []

with open(nom_fichier, 'r', encoding='utf-8') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv)
    next(lecteur_csv)
    for rangee in lecteur_csv:
        list_client.append(rangee)
print(list_client)



