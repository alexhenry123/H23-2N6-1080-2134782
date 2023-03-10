from operator import index
import requests
import json


base_url="https://fakestoreapi.com"

# Q1 Écrivez une fonction appelée request_carts qui aura 1 paramètre
#   soit le nombre de carts que vous voulez aller chercher
#   Le nombre de cart doit être donné lors de l'appel de la fonction 
#           mais s'il n'est pas donné il faut que cela ne cause pas d'erreur
#   Si le nombre de cart n'est pas donné lors de l'appel, 
#           donnez un message comme quoi il faut préciser le nombre de carts 
#           et arrêter l'exécution de la fonction
#   Vérifiez que le nombre donné lors de l'appel est entre 1 et 10
#   Si ce n'est pas le cas, 
#          donnez un message comme quoi il faut demander entre 1 et 10 carts, 
#          en précisant le nombre de carts qui avait été demandé
#   Si on passe autre chose qu'un nombre entier en paramètre 
#          faites un message comme quoi il faut entrer un nombre entre 1 et 10
#   La fonction doit retourner le nombre de carts demandés, si le nombre est entre 1 et 10

#Requête json des carts
res = requests.get(f'{base_url}/carts')
donnees_json = json.dumps(res.json(),indent=4)
for carts in res:
    compteur = 0
    if carts == '"id"':
        compteur+=1
nb_de_carts_json = compteur

#print(donnees_json)

#Création de la méthode
def request_carts(nb_de_carts=None):
    
    #S'il n'y a pas de paramètre entré
    if nb_de_carts is None:
        return print("Veuillez entrer un paramètre, soit le nombre de carts")
        
    #Si le paramètre n'est pas entre 1 et 10
    if nb_de_carts <= 0 or nb_de_carts >= 11:
        print(f"Votre nombre entré, soit {nb_de_carts}, ne correspond pas. Veuillez entrer un nombre entre 1 et 10 pour le nombre de carts")
        
    #(Valide) Si le paramètre donné est un entier entre 1 et 10
    elif nb_de_carts >= 1 and nb_de_carts <= 10:
        print(f"Voici le nombre de carts demandés : {nb_de_carts}")
        
    #Dans les autres cas
    else:
        print(f"Veuillez entrer un nombre entier entre 1 et 10")

request_carts(nb_de_carts_json)


# Q2 Écrivez une fonction appelée request_products qui aura 1 paramètre
#   soit le nombre de produits que vous voulez aller chercher
#   Le nombre de produit doit soit être donné lors de l'appel de la fonction
#                             soit être demandé à l'usager s'il n'est pas donné
#   Vérifiez que le nombre demandé est entre 1 et 10
#   Limitez cette valeur à 10 si l'usager en demande plus et donnez un message comme quoi vous avez cette limite
#   Si le nombre demandé est moins de 1, obtenez 1 produit tout simplement

#   La fonction doit retourner le nombre de produits demandés, si le nombre est entre 1 et 10

#Requête des "products" json
def request_products():
    pass




