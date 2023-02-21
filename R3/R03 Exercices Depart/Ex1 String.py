
# Pour chaque question ci-dessous, faites le code demandé puis imprimez toujours 80*'_' afin de séparer les questions.      #
# Imprimez le résultat en utilisant f-string pour afficher le numéro de la question et les infos demandées                  #

# Q1                                                                                                                   #
# Vous avez ici une liste de différents processeurs            
# Vous pouvez aussi mettre un autre modèle de carte graphique si vous voulez.#
# imprimez la liste                                                                                                    #
# Changez la liste en une chaine de caractères avec les cartes graphiques séparées par des virgules
liste_de_processeurs = "Intel® Core™ i3, Intel® Core™ i9, Intel® Core™ i7"
print(f"Voici la liste de processeurs : {liste_de_processeurs}")

print(80*'_')
#Q2                                                                                                                   #
#  Voici une chaine de caractères qui ressemble à une ligne de données que vous auriez extraite d'un fichier texte     #
ligne_donnees = " AMD Ryzen 9 5900X ;  AMD Ryzen 7 5800X3 ;  Intel Core i9 12900 K    "                               #
#  Vous devez dans un premier temps séparer les données sur le caractère qui les séparent
#  Vous voulez ensuite avoir une liste de chacun des processeurs sans les espaces avant et après chaque processeur                                                                                            #
#  Imprimez la liste maintenant                                                                    #
for i in range(len(ligne_donnees)):
    print(f"Voici la liste imprimée selon le numéro de son répertoire : {ligne_donnees[i]}")
    break
ligne_donnees.strip()
print(f"Voici maintenant la liste sans espaces avant ou après chaque caractère : {ligne_donnees}")

print(80*'_')
# Q3                                                                                                                   #
# Voici un nom de fichier dont chaque partie est séparée par un _                                                      #
nom_fichier_et_extension = "Python_Rencontre 3_Approfondissement str.docx"                                             
# Séparez nom_fichier_et_extension sur le '.' et gardez les parties dans des sous-chaines séparées                     #
# Séparez le nom de fichier de façon à récupérer le nom du cours, la rencontre et le sujet de la rencontre             #
# Imprimez le nom du cours, la rencontre et le sujet de la rencontre                                                   #
fichier1, fichier2 = nom_fichier_et_extension.split(".")
print(f"Voici le fichier avant le point : {fichier1}")
print(f"Voici le fichier après le point : {fichier2}")

print(80*'_')
#Q4
#  remplir un string pour qu'il fasse 2 caractères de long avec .zfill
#  Au départ, vous avez une chaine qui contient des nombres
str_nombres = "1,5,10,15,20,25"
#  transformez cette chaine en une liste
#  triez cette liste en nombres croissants tout en conservant la liste de nombres originale (avec sorted)
# Imprimez la liste. Qu'est-ce qui est étonnant?
# Pour pouvoir avoir la liste de string dans un ordre croissant numérique il faut remplacer les valeurs pour qu'ils soient tous 2 de long
# Une fois cela fait, imprimez la liste en ordre croissant de nouveau
liste_nombres = str_nombres.split(",")
print(f"Voici la chaîne transformée en liste : {liste_nombres}")

print(80*'_')