# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 

# Pour chaque question ci-dessous, faites le code demandé puis imprimez toujours 80*'_' de séparer les questions.      #
# Imprimez le résultat en utilisant f-string pour afficher le numéro de la question et les infos demandées             #
# CHOISISSEZ LA MÉTHODE QUI VOUS SEMBLE LA MIEUX POUR FAIRE CE QUI EST DEMANDÉ                                         # 


# Q1                                                                                                                   #
# Créez une liste de 3 modèles de cartes graphiques. Voici une liste de cartes graphiques. Vous pouvez construire votre liste en choisissant parmi les suivantes:                                                          #
#          GeForce RTX 3090Ti, GeForce RTX 3080Ti, GeForce RTX 3070Ti, Radeon RX 6950 XT, Radeon RX 6900 XT, Radeon RX 6800 XT             
# Vous pouvez aussi mettre un autre modèle de carte graphique si vous voulez.#
# imprimez la liste                                                                                                    #
liste_de_cartes_graphiques = ['GeForce RTX 3090Ti', 'GeForce RTX 3080Ti', 'GeForce RTX 3070Ti']
print(f"Voici la liste de cartes graphiques : {liste_de_cartes_graphiques}")

print(80*'_')

#Q2                                                                                                                   #
#  Obtenez la carte graphique à l'index 1 de la liste de vos cartes graphiques                                        #
#  Enlevez-la de la liste                                                                                             #
#  Imprimez la liste en spécifiant l'item enlevé                                                                      #
liste_de_cartes_graphiques.remove(liste_de_cartes_graphiques[1])
print(f"Voici la liste avec l'item enlevé ({liste_de_cartes_graphiques[1]}) : {liste_de_cartes_graphiques}")

print(80*'_')

# Q3                                                                                                                   #
# Ajoutez un nouvel item à la fin de la liste                                                                          #
# et affichez la dernière carte graphique que vous avez maintenant dans la liste                                       #
liste_de_cartes_graphiques.append('Radeon RX 6900 XT')
print(f"Voici le nouvel item au dernier index dans la liste : {liste_de_cartes_graphiques[len(liste_de_cartes_graphiques)-1]}")

# Q4                                                                                                                 #
# Inversez les items de votre liste                                                                                  #
liste_de_cartes_graphiques.reverse()

print(80*'_')

# Q5                                                                                                                 #
# Créez une petite liste de deux nouvelles cartes graphiques                                                         #
# Imprimez cette nouvelle petite liste                                                                               #
# Ajoutez cette nouvelle petite liste à la fin de votre première liste                                               #
# Imprimez votre liste initale telle qu'elle est rendue                                                              #
liste_cartes_graphiques_2 = ['Radeon RX 6950 XT','Radeon RX 6800 XT']
print(f"Voici une deuxième liste de cartes graphiques : {liste_cartes_graphiques_2}")
liste_de_cartes_graphiques.extend(liste_cartes_graphiques_2)
print(f"Voici maintenant la liste originelle avec la nouvelle liste : {liste_de_cartes_graphiques}")

print(80*'_')

# Q6                                                                                                                  #
# Ordonnez la liste en ordre croissant de façon à créer une nouvelle liste                                            #
# et imprimez cette nouvelle liste    
liste_ordonnée = sorted(liste_de_cartes_graphiques)
print(f"Voici maintenant la liste ordonnée : {liste_ordonnée}")