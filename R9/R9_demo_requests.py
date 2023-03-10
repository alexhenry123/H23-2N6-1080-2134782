# comment intaller un module qu'on n'a pas déjà installé dans python
# https://www.freecodecamp.org/news/how-to-interact-with-web-services-using-python/
# Dans le terminal              pip install requests

# Fake Store REST API
from math import prod
import requests
import json

BASE_URL = 'https://fakestoreapi.com'
# lien vers la doc :  https://fakestoreapi.com/docs


# faire une demande de tous les produits (GET)

# res = requests.get(f'{BASE_URL}/products')
# print(res)
# print(res.text)


#######################################################################
# pour avoir seulement quelques produits
# l'API nous offre /products?limit=x

# faire une demande de 3 produits (GET/products?limit=3)

res = requests.get(f'{BASE_URL}/products?limit=3')
donnees_req = res.json()
print(json.dumps(donnees_req[0],indent=4))



######################################################################
# pour avoir un produit précis
# l'API nous offre /products/productID

# faire une demande pour le produit dont l'id est 18 (GET/products?18)


res = requests.get(f'{BASE_URL}/products/18')
donnees_req = res.json()
print(json.dumps(donnees_req,indent=4))

######################################################################
# Une fois la réponse obtenue, on peut convertir la réponse en objet python et les utilisés
# si on veut trier les produits selon leurs catégories


res = requests.get(f'{BASE_URL}/products/18')
donnees_req = res.json()

for produit in donnees_req:
    print(produit["price"])

ls_aubaine = []
for produit in donnees_req:
    if produit["price"] <= 20:
        ls_aubaine.append(produit["id"])
print(ls_aubaine)

######################################################################
# Ou bien si on veut extraire les noms de tous les clients et les mettre dans une liste.


res = requests.get(f'{BASE_URL}/users/1')
donnees_json = res.json()
ls_aubaine = []
for users in donnees_json:
    if users["price"] <= 20:
        ls_aubaine.append(users["id"])
print(ls_aubaine)



######################################################################
# Ou encore, on peut aller chercher les produits dans un panier puis aller chercher chacun de ces produits










######################################################################
######################################################################
# Si on fait une requête à un autre API, il faut regarder la doc
# https://fakerapi.it/en


BASE_URL = "https://fakerapi.it/api/v1/"



# donc si on veut obtenir les 10 premières adresses

# res = requests.get(f'{BASE_URL}addresses?_quantity=10')
# donnees_req = res.json()["data"]
# print(json.dumps(res.json(),indent=4))


# Avec cette API, les résultats sont aléatoires par défaut.
# Allons chercher les mêmes trois livres de facon reproduisable

# res = requests.get(f'{BASE_URL}addresses?_quantity=2&_seed=1')
# donnees_req = res.json()["data"]
# print(json.dumps(res.json(),indent=4))