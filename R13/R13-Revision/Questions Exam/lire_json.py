import json
import os
os.chdir(os.path.dirname(__file__))


# Q4
# Le fichier json_a_lire.json contient une liste de tous les produits disponibles en magasin.
# On veut générer une nouvelle liste ne contenant que les produits dans la catégorie "electronics"
# Vous devez ouvrir le fichier json et extraire son contenu 
# Vous devez ensuite ajouter uniquement les produits de la catégorie "electronics" à la nouvelle liste.
# Vous devez finalement imprimer cette nouvelle liste dans le terminal. 
# Cette liste n'a pas besoin d'être formatée de facon à être lisible facilement pour l'humain

nom_fichier = "json_a_lire.json"
liste_produits_electronics = []

with open(nom_fichier, 'r') as fichier_json:
    texte = fichier_json.read()
    donnee_json = json.loads(texte)
for produit in donnee_json:
    if produit["category"] == "electronics":
        liste_produits_electronics.append(produit)
print(liste_produits_electronics)