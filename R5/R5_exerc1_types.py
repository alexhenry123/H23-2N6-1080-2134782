import utilitaire_gen_Q as util_r5
# Q1 Ce petit script demande l'âge de la personne et imprime sa date de naissance.
# La fonction input() retourne une valeur en string.
# Ajouter un test conditionnel sur l'input qui :
#                      -imprime "ERREUR - âge non-valide" si la valeur d'entrée n'est pas un chiffre entier 
#                      -et qui convertie l'input en int si possible. 
# Indice : pour pouvez utiliser la fonction  dir(str)  pour obtenir toutes les méthodes
# des objets str... une de ces méthodes devrait vous aider... vous ne trouverez pas la méthode exacte dans vos notes de cours. 
print(f"Q1{80*'_'}")

#Fonctionne pour int mais pas pour string
#
# age = int(input("Entrez votre âge : "))
# if type(age) == int:
#     print(util_r5.annee_de_naissance(age))
# else:
#     print("ERREUR - âge non-valide")

#Façon #2 pour int (plante toujours lorsque la valeur d'entrée du input est un string)

age = input("Entrez votre âge : ")
if age == str.isalpha:
    print("ERREUR - âge non-valide")
else:
    print(util_r5.annee_de_naissance(int(age)))


# # Q2 Des variables sont générées par une fonction dans un module utilitaire.
# # Imprivez la valeur de chaque variable et son type
print(f"Q2{80*'_'}")

#Ne compile pas (message d'erreur : "TypeError: 'type' object is not iterable")
#
# var1,var2,var3,var4,var5,var6 = util_r5.generation_variable()
# types_variables = []
# valeurs_variables = []
# for variable in util_r5.generation_variable():
#     types_variables += type(variable)
#     valeurs_variables += variable
# print(f"""Voici les types des variables {types_variables}
# Et voici les valeurs des variables {valeurs_variables}""")