# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 

# Pour chaque question ci-dessous, faites le code demandé puis imprimez toujours 80*'_' pour séparer les questions.      #
# Imprimez le résultat en utilisant f-string pour afficher le numéro de la question et les infos demandées             # 

# Q1                                                                                                                   #
# Créez une liste de 3 barrettes de RAM parmis les suivantes:                                                          #
#          G.SKILL Trident Z5, CORSAIR Dominator, CORSAIR Vengeance, G.SKILL Ripjaws V, G.SKILL Ripjaws X              #
# imprimez la liste                                                                                                    #
liste_de_barrettes_RAM = ['G.SKILL Trident Z5', 'CORSAIR Dominator', 'CORSAIR Vengeance']
print(liste_de_barrettes_RAM)

print(80*'_')

# Q2                                                                                                                   #
# Ajoutez un item à la fin de la liste avec append                                                                     #
# et affichez la dernière barrette RAM que vous avez dans la liste                                                     #
liste_de_barrettes_RAM.append('G.SKILL Ripjaws X')
print(f"L'item ajouté est : G.SKILL Ripjaws X, voici le dernier item de la liste maintenant : {liste_de_barrettes_RAM[len(liste_de_barrettes_RAM)-1]}")

print(80*'_')

#  Q3                                                                                                               #
#  Observez quelle est la deuxième barrette de RAM de votre liste                                                   #
#  Enlevez-la de la liste avec remove                                                                               #
#  Imprimez la liste en spécifiant la barrette de RAM enlevée                                                       #
print(f"La deuxième barrette de RAM de la liste qui sera enlevée est : {liste_de_barrettes_RAM[1]}")
liste_de_barrettes_RAM.remove(liste_de_barrettes_RAM[1])
print(f"Voici maintenant la liste après avoir enlevé le deuxième item : {liste_de_barrettes_RAM}")

print(80*'_')

# Q4                                                                                                             #
# Ordonner la liste en ordre croissant avec la méthode sort et imprimez-la                                       #
liste_de_barrettes_RAM.sort()
print(f"Voici la liste en ordre croissant : {liste_de_barrettes_RAM}")

print(80*'_')

# Q5                                                                                                             #
# Ordonner la liste en ordre décroissant avec la méthode sorted (qui crée une nouvelle liste)                    #
# et imprimez-la                                                                                                 
liste_de_barrettes_RAM_décroissant = sorted(liste_de_barrettes_RAM.sorted)
print(f"Voici la liste en ordre décroissant : {liste_de_barrettes_RAM_décroissant}")

print(80*'_')

# Q6                                                                                                                 #
# Imprimez le nombre d'éléments qu'il y a dans votre liste présentement                                              #
print(f"Voici le nombre d'éléments présentement dans la liste : {len(liste_de_barrettes_RAM)}")

print(80*'_')

# Q7                                                                                                                 #
# Imprimez une sous-liste des deux dernières barrettes RAMS de votre liste, en utilisant le slicing                  #
print(f"Voici une sous-liste des deux dernières barrettes RAM de la liste : {liste_de_barrettes_RAM[len(liste_de_barrettes_RAM)-1:len(liste_de_barrettes_RAM)-2]}")