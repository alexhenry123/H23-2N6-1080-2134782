# On peut faire une invitation générale comme cela, mais c'est un peu froid
# Nous avons ici une simple invitation, sans nom précis #
# Si on envoie cette invitation à nos amis, ils pourraient être fachés car c'est un peu impersonnel.#
from gettext import find


print("Bonjour \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")

# Nous avons ici la même invitation lancée à plusieurs de nos amis, avec leurs noms.                       #
print("Bonjour Marc,\n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Pierre,\n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Lucie, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Achraf, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Claude, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Ilyan, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Maria, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
print("Bonjour Thomas, \n Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?")
# C'est mieux mais c'est de la répétition.  Et si je voulais inviter 30 personnes....

# Q1 A:  Faites une fonction pour inviter tout le monde, sans duplication du code.
#        Cette fonction prendra une liste d'amis en paramètres                                      #
liste_amis = ["Marc", "Pierre", "Lucie", "Achraf", "Claude", "Ilyan", "Maria", "Thomas"]
def invitation(liste_amis):
    for i in liste_amis:
        print(f"""Bonjour {i}, 
Je veux t'inviter à venir chez moi demain vers 18h00. Cela t'intéresse?""")

# Q1 B:   Appel de la fonction avec la liste d'amis qu'on veut inviter. 
#         Il faudra créer une liste qui comprendra les noms de nos amis, "Marc","Pierre", etc.
#         Puis faites l'appel de la fonction en lui passant en paramètre votre liste d'amis
invitation(liste_amis)

# Q2 A:   Fonction pour inviter tout le monde, dans un lieu, un jour et une heure qui varient, sans duplication du code
#         Appelez cette fonction invitation2
lieu = ""
jour = ""
heure = ""
nom = ""
def invitation2(nom, lieu, jour, heure):
    print(f"""Bonjour {nom}, 
Je veux t'inviter au {lieu}, {jour}, vers {heure}""")

# Q2 B:  Appel de la fonction invitation2 pour inviter Sylvain et Nathalie au café étudiant, vendredi, vers 13h00
invitation2("Sylvain", "café étudiant", "vendredi", "13:00")
invitation2("Nathalie", "café étudiant", "vendredi", "13:00")

# Q2 C:  Appel de la fonction invitation2 pour inviter Sylvain, Nathalie et Paul chez moi pour souper, samedi vers 17h00
invitation2("Nathalie", "domicile, chez moi pour souper", "samedi", "17:00")
invitation2("Sylvain", "domicile, chez moi pour souper", "samedi", "17:00")
invitation2("Paul", "domicile, chez moi pour souper", "samedi", "17:00")