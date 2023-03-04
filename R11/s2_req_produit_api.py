import os
import csv
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

# Maintenant que nous avons un script capable de lire et décoder le fichier csv.
# Nous voulons ajouter des informations à liste de produits de chaque client :
# le prix de chaque produit et sa catégorie.

# Les informations sur les produits proviennent du site du magasin.
# Vous devez aller chercher les informations à l'aide du module requests.
url = "https://fakestoreapi.com"

import s1_lire_csv_ventes
import json
import requests as rq
ls_client = s1_lire_csv_ventes.ls_clients

res = rq.get(f"{url}/products")
donnees_json = res.json()

ls_commandes = []
for i in range(len(donnees_json)):
    prix = donnees_json[i]["price"]
    categorie = donnees_json[i]["category"]
    dict_prixcategorie = {"Prix":prix,"Catégorie":categorie}
    ls_commandes += dict_prixcategorie.items()
ls_client.append(ls_commandes)
print(ls_client)
