# comment intaller un module qu'on n'a pas déjà installé dans python
# https://www.freecodecamp.org/news/how-to-interact-with-web-services-using-python/
# Dans le terminal              pip install requests
# Fermez et réouvrez Code si nécéssaire

# fakerapi.it/en
import requests
import json

BASE_URL = 'https://fakerapi.it/api/v1'


# pour avoir seulement X produits
# l'API nous offre /products?_quantity=X

# Q1) faire une demande de 1 produit1 (GET/products?_quantity=1) et conservez le résultat dans une variable

res = requests.get(f"{BASE_URL}/products?_quantity=1")
print(f"Q1: {json.dumps(res.json(),indent=4)}")



# Q2) Pour travailler avec le résultat de la réponse, il faut le convertir en objet python.
# L'objet de la classe <Respsonse> retourné par la requests.get() possède la méthode json() pour faire cela.
# Transformer la réponse et imprimer le résultat.

# res = requests.get(f"{BASE_URL}/products?_quantity=1")
# donnees_json = res.json()
# print(f"Q2: {donnees_json}")



# Q3) Le résultat obtenu à la question 2 n'est pas très clair.
# La fonction json.dumps() prend un objet python en paramètre et retourne une chaîne de caractères.
# Cette fonction peut aussi prendre une valeur pour l'argument "indent" qui sert à spécifier le niveau
# d'indentation de la chaîne de caractères. Avec le paramètre indent, le string devient lisible pour l'être humain.
# Utilisez json.dumps() pour imprimer la réponse sous un format lisible par l'humain.

# res = requests.get(f"{BASE_URL}/products?_quantity=1")
# donnees_json = json.dumps(res.json(),indent=4)
# print(f"Q3: {donnees_json}")



#Si on regarde le résultat obtenue à la question 3, on peut voir la structure de la réponse obtenu.
# La réponse devrait être similaire à ceci :
{
    "status": "OK",
    "code": 200,
    "total": 1,
    "data": [
        {
            "id": 1,
            "name": "Ut magni et voluptatem est.",
            "description": "Quaerat voluptate vel quae. Repudiandae nobis et labore vitae id id placeat.",
            "ean": "5258822017705",
            "upc": "446534029075"
        },
        {
            "id": 2,
            "name": "Hic sunt sed iusto quia.",
            "description": "Iste dolorum sed pariatur placeat amet atque. Et ex incidunt quam voluptatem voluptatibus iusto. Deserunt ducimus voluptate earum id soluta nesciunt.",
            "ean": "8151906598244",
            "upc": "238309185512"
        }
    ]
}
# On peut constater que l'objet obtenu par la fonction .json() est dans ce cas un dictionnaire.
# Ce dictionnaire contient seulement 4 paires clefs ; "status","code","total", et "data"
# C'est la clef "data" qui contient la liste des produits en réponse à notre requête.

# Q4)  Obtenez le premier élément du dictionnaire avec la clé 'data' dans une variable et imprimez-le
#  Donc on obtient quelque chose comme
# {'id': 1, 'name': 'Blanditiis aut in quia omnis.', 'net_price': 2.15, 'taxes': 22, 'price': '2.62', 'categories': [2, 3, 5]}

res = requests.get(f'{BASE_URL}/products')
donnees_jsondata = res.json()["data"][0]
print(json.dumps(donnees_jsondata,indent=4))



#  Q5) Obtenez le prix et changez-le en un float
donnees_jsonprix = donnees_jsondata["price"]
float(donnees_jsonprix)



#  Q6)  Utilisez l'instruction << in >> pour vérifier si 3 fait partie des valeurs dans la liste categories du produit
donnees_jsoncategories = donnees_jsondata["categories"]
bool_categorie = False
print(donnees_jsoncategories)
# for categorie in donnees_jsoncategories:
#     if donnees_jsoncategories[categorie] == 3:
#         bool_categorie = True
#         break


#  Q7)  Imprimez le prix et si le produit est dans la catégorie 3 ou non
#       Quelque chose comme: "Le produit a le prix de 3945.01 et on peut savoir s'il est dans la catégorie 3: False"
print(f"Le produit a le prix de {donnees_jsonprix} et on peut savoir s'il est dans la catégorie 3 : {bool_categorie}")
