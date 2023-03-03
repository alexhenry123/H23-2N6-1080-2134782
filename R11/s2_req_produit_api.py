import os
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

# Maintenant que nous avons un script capable de lire et décoder le fichier csv.
# Nous voulons ajouter des informations à liste de produits de chaque client :
# le prix de chaque produit et sa catégorie.

# Les informations sur les produits proviennent du site du magasin.
# Vous devez aller chercher les informations à l'aide du module requests.
url = "https://fakestoreapi.com"

import echantillon_data
import s1_lire_csv_ventes
import json
import requests as rq
ls_client_s1 = echantillon_data.liste_clients_s1
ls_client_s2 = echantillon_data.liste_clients_s2
ls_s1 = s1_lire_csv_ventes

res = rq.get(f"{url}/products")
data = json.loads(res.text)
donnees_json = res.json()
#json_lisible = json.dumps(res.json(),indent=4)

index = 0
ls_commandes = []
for commandes in donnees_json:
    for commandes in donnees_json:
        prix = donnees_json[index]["price"]
        catégorie = donnees_json[index]["category"]
    ls_commandes += prix, catégorie
    index+=1
dict_produits = {"Prix":ls_commandes,"Catégorie":ls_commandes}

print(f"{dict_produits}")

