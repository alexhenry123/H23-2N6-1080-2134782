import datetime


employe = {"prenom":"Ana","nom":"tremblay","departement":"informatique","id":732,"equipe":"Team C"}


# On veut obtenir le nom complet de l'employé
nom = employe["nom"]
nom_maj = nom.capitalize()
nom_complet = f'{employe["prenom"]} {nom_maj}'

# Déja, on se rend compte d'une erreur lorsque le nom a été entré
# on veut que le nom de famille commence par une majuscule.
print(nom_complet)

# Maintenant, on veut vérifier la date d'embauche de l'employé. 
# S'il n'y a pas de date c'est un nouvel employé dont le dossier n'est pas encore terminé.
if not employe.get("date_embauche"):
    print("Il n'y a pas de date d'embauche pour cet emplyé.")
else:
    employe["date_embauche"] = datetime.date.today().isoformat()

# On veut retirer la clef "equipe" du dictionnaire car il s'agit d'un vestige d'un ancien système dans la compagnie
# Pourquoi pop() plutot que del ?
#del employe["equipe"]
element_retire = employe.pop("equipe")
print(employe)
print(f"L'élément équipe avec une valeur de {element_retire} a été retiré.")

# Dans ces exemples nous travaillons avec un dictionnaire que nous connaissons.
# Si on travaille avec un dictionnaire qu'on a obtenu à partir d'une source externe...
# il faut d'abord connaitre les clefs.
for clef, valeurs in employe.items():
    print(clef,valeurs)

# On peut aussi travailler avec chacune des paires clef:valeur une après l'autre.


# # Maintenant, on veut ajouter une liste des langagues de programmation connus par l'employe pour savoir quel cours il pourrait donner.
competences = ["Python","C#","Pascal","Assembleur","Fortran","Magic the gathering"]




# # Si ensuite on veut extraire les langages pour une raison quelconque



# # La clef "languages" du dictionnaire "employe" correspond réellement à une liste.
# # Toutes les méthodes et particuliarité des listes sont utilisables.
# # Si on veut uniquement le premier language...




# # Si on veut ajouter un language






# Maintenant que nous avons fini de travailler sur le nouvel employe, 
# nous allons ajouter le dictionnaire contenant ses informations à une liste de tous les employées

liste_employés_2023 = [ {"prenom":"Bob","nom":"Uvoy","departement":"informatique","id":645,"languages":["C#","C++","C","Java"]},
                        {"prenom":"Chris","nom":"Volaire","departement":"informatique","id":987,"languages":["Ruby","Java","Perl"]},
                        {"prenom":"Edouard","nom":"Petit","departement":"multimédia","id":258,"languages":["C#"]}]





# print("Bienvenu aux nouveaux employés de 2023 :")
# for personne in liste_employés_2023:
#     print(f'\t{personne["prenom"]} {personne["nom"]}',end="")
#     if personne == liste_employés_2023[-1]:
#         print("  !")
#     else:
#         print(",")