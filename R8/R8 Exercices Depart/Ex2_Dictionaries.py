# Supposons que vous avez ces informations sur un de vos clients:
info_client = {"id":0,"prenom":"Hélène","nom":"Boucher","solde":831600}

print(f"{80*'_'}")
# Q1: Affichez le prenom et le nom dans le terminal
#     Résultat attendu dans le terminal : Q1: Bonjour Hélène Boucher ! 
nom_complet = f'{info_client["prenom"]} {info_client["nom"]}'
print(f"Q1: Bonjour {nom_complet} !")

# Lorsque nous faisons une requête à un API, on sait qu'on obtient des données dans un format JSON
# Supposons que vous avez obtenu de FakerAPI les données suivantes
donnees_json=[
    {"id":0,"prenom":"Hélène","nom":"Boucher","solde":8160},
    {"id":1,"prenom":"Thérèse","nom":"Tessier","solde":7038},
    {"id":2,"prenom":"Benjamin","nom":"Savard","solde":3163},
    {"id":3,"prenom":"Jean","nom":"Tremblay","solde":411},
    {"id":4,"prenom":"Hugues","nom":"Pelletier","solde":96}
]
# Ce sont des données qui sont dans des dictionnaires qui sont dans une liste

print(f"{80*'_'}")
# Q2: Pour aller chercher la liste de tous les "prenom", "nom" de cette liste, il faudra faire une boucle
#     Regardez ce que vous avez appris sur les listes pour changer la liste en un str
#     Résultat attendu dans le terminal : Q2: Voici la liste des clients: Hélène Boucher, Thérèse Tessier, Benjamin Savard, Jean Tremblay, Hugues Pelletier
nom_complet = ""
for client in donnees_json:
    nom_complet += f'{client["prenom"]} {client["nom"]}, '
print(f"Q2: Voici la liste des clients : {nom_complet}")

print(f"{80*'_'}")
# Q3: Je veux avoir le solde moyen de mes clients
# Maintenant, disons qu'on veut avoir le nombre de clients, on sait qu'on l'a avec len
# Si je veux avoir le solde moyen de tous mes clients, je vais devoir en premier calculer le solde total
# Et après, diviser le solde total par le nombre de clients
#       Résultat attendu dans le terminal:  Q3 Le solde moyen de mes clients est : 3773.6
total = 0
nb_soldes = len(donnees_json)
for client in donnees_json:
    total += client["solde"]
print(f"Q3: Le solde moyen de mes clients est : {total / nb_soldes}")

#Test
nombre = "patate"


pass


