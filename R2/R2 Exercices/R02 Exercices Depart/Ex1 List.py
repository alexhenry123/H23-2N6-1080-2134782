# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 


# Pour chaque question ci-dessous, faites le code demandé puis imprimez toujours 80*'_' de séparer les questions. 

# Q1                                                                                                            #
# créez une liste de 4 à 5 sports  et imprimez la liste                                                         #
R2_Alex_Henry = ['hockey', 'football', 'basketball', 'tennis', 'course à pieds']
print(R2_Alex_Henry)

print(80*'_')
# Q2                                                                                                             #
# affichez le premier sport de votre liste                                                                       #
print(R2_Alex_Henry[0])

print(80*'_')
# Q3                                                                                                             #
# ajoutez un item à la fin de la liste avec append                                                               #
# et affichez le dernier sport que vous avez dans la liste                                                       #
R2_Alex_Henry.append('ping pong')
print(R2_Alex_Henry[len(R2_Alex_Henry)-1])

print(80*'_')
# Q4                                                                                                                #
#    ajoutez un item après le 1er sport de votre liste avec insert                                                  #
#    créez une liste d'autres sports que vous n'avez jamais fait                                                    #
#    imprimez la liste telle qu'elle est rendue                                                                     # 
#    ajoutez votre autre liste de sports à la première liste avec extend                                            #
#    imprimez la liste telle qu'elle est rendue                                                                     # 
R2_Alex_Henry.insert(1, "ballon chasseur")
liste_sports_non_joués = ['rugby','tennis','quidditch','boxe']
print(liste_sports_non_joués)
R2_Alex_Henry.extend(liste_sports_non_joués)
print(R2_Alex_Henry)

print(80*'_')
#  Q5                                                                                                               #
#  Imprimez le nom d'un sport que vous enleverez ensuite de la liste                                                #
#  Enlevez un sport de la liste avec remove                                                                         #
#  Imprimez la liste et voyez que le sport que vous avez enlevé avec remove est bel et bien enlevé                  #
#  Enlever le dernier sport de la liste avec pop. Le sport enlevé est retourné par pop Affichez-le                  #
#  Imprimez la liste en spécifiant le sport enlevé et utilisant f-string                                            #
print(R2_Alex_Henry[2])
R2_Alex_Henry.remove(R2_Alex_Henry[2])
print(R2_Alex_Henry)

sport_retiré = R2_Alex_Henry.pop(len(R2_Alex_Henry)-1)
print(R2_Alex_Henry)
print(sport_retiré)

print(f"Sport que je compte enlever avec remove : basketball")
print(f"J'ai enlevé le sport 'boxe' avec pop, voici maintenant la liste : {R2_Alex_Henry}")

print(80*'_')
# Q6                                                                                                             #
# Utilisez une boucle for pour passer à travers chaque sport dans la liste avec une boucle for                   #
# et affichez le sport sur différentes lignes                                                                    #
for i in range(0, len(R2_Alex_Henry)-1):
    print(R2_Alex_Henry[i])

print(80*'_')  
# Q7                                                                                                             #
# Ordonner la liste en ordre croissant avec la méthode sort et imprimez-la                                       #
R2_Alex_Henry.sort()
print(R2_Alex_Henry)

print(80*'_')  
# Q8                                                                                                                 #
# changez la liste en un string séparé par une virgule et affichez ce str                                            #
liste_en_str = input(R2_Alex_Henry)
print(f"Voici la liste en str : {liste_en_str}")

print(80*'_')  
# Q9                                                                                                                 #
# Imprimez une sous-liste des deux premiers sports, en utilisant le slicing                                          #
print(R2_Alex_Henry[0:len(R2_Alex_Henry-1)])

print(80*'_')