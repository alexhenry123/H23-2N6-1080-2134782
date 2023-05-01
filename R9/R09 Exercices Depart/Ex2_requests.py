# Comment installer un module qu'on n'a pas déjà installé dans python
# https://www.freecodecamp.org/news/how-to-interact-with-web-services-using-python/
# Dans le terminal              pip install requests

# fakerapi.it/en
import requests
import json

BASE_URL = 'https://fakerapi.it/api/v1'

#  Le but est d'obtenir le 'price' moyen des produits de moins de 100000 qui sont dans la catégorie 3.

### - Q1) Faites une demande de 25 produits 
res = requests.get(f'{BASE_URL}/products?limit=25')
 
##  Q2) Utilisez json.dumps() et son paramètre indent pour imprimer 
# la réponse de façon lisible pour l'humain.
donnees_json = json.dumps(res.json(),indent=4)
print(donnees_json)

# Q3)  Obtenez la liste des produits à partir de la clé 'data' du dictionnaire obtenue en Q3
donnees_jsondata = res.json()["data"]

# Q4) On veut faire la moyenne des produits qui sont dans la catégorie 3
#        ET dont le prix est moins de 100 000$
#
# Pour cela: 
#      Créez vous deux variables initialisées à 0 au départ. 
#      Une pour accumuler le total des prix et l'autre pour compter le nombre de produits.
#      Faites une boucle pour passer à travers la liste des produits obtenue en Q4
#           Dans la boucle, vous obtenez le prix du produit et castez-le en float
#           Si le produit a la catégorie 3 et que le prix est inférieur à 100000
#                   ajoutez-le au total des prix
#                   augmenter votre compteur de produit qui satisfont le test précédent
#      Après la boucle calculez la moyenne
#      Finalement imprimez le résultat, qui pourrait ressembler à ceci: 
#            "Parmi les 25 produits que j'ai obtenus, il y a 6 produits dans la catégorie 3 et leur prix moyen est de 12 328,94$"
#
total_des_prix = 0
nombre_de_produits = 0
for produits in donnees_jsondata:
    prix_produit = float(produits["price"])
    if produits["categories"] == 3 and prix_produit < 100000:
        total_des_prix += produits["categories"]
        nombre_de_produits+=1
moyenne = total_des_prix / nombre_de_produits
print(f"Q4: Parmi les 25 produits que j'ai obtenus, il y a {nombre_de_produits} produits dans la catégorie 3 et leur prix moyen est de {moyenne}")