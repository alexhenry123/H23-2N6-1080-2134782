import os
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

# On cherche ici à produire un fichier texte avec une courte analyse des données de ventes.
# Pour chaque valeur produite, vous devez écrire une phrase indiquant à quoi correspond cette valeur.

# Globalement :
#   Nombre total d'articles vendus
#   Montant total des ventes
#   Prix moyen des commandes

#   Personne ayant fait la commande la plus élevée avec le montant de la commande
#   Personne ayant fait la commande la moins élevée avec le montant de la commande

#Pour des points supplémentaires, vous pouvez aussi extraire les informations suivantes :
# Par catégorie :
#   Nombre total d'articles vendus
#   Montant total des ventes
import s1_lire_csv_ventes
import s2_req_produit_api
ls_client_s2 = s2_req_produit_api.ls_client
dict_client_s2 = s2_req_produit_api.dict_prixcategorie

#Variables
total_articles_vendus = 0
montant_total_ventes = 0
prix_moyen_ventes = 0
prix_moyen_ventes = 0
plus_grand_prix = 0
plus_petit_prix = 0

#Nombre d'articles vendus
for articles in ls_client_s2:
    if articles == "id":
        total_articles_vendus+=1

#Montant total des ventes
prix = 0
for prix in dict_client_s2.values:
    prix += dict_client_s2["price"]

#Prix moyen des commandes
prix_moyen_ventes = montant_total_ventes / total_articles_vendus


