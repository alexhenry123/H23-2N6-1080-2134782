# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 


exercice_sep = "___________________________________"
# Pour chaque question ci-dessous, faites le code demandé puis imprimez toujours exercice_sep ensuite afin de séparer les questions


nom_fichier = "Liste étudiants gr. 1010"
#  Sachez que le groupe est toujours les 4 derniers caractères du nom de fichier#
# Q1 Faites le code nécessaire pour obtenir ces 4 derniers caractères en utilisant le slicing à partir de la fin #
for i in range(len(nom_fichier),len(nom_fichier)-4):
    print(nom_fichier[i])

print(exercice_sep)

# Q2 Imprimez chacun des caractères du nom_fichier en utilisant for, len et range #
for i in range(len(nom_fichier)):
    print(nom_fichier[i])
    
print(exercice_sep)
    
# Q3 Imprimez chacun des caractères du nom_fichier de façon INVERSÉE en utilisant for, len et range et un indice #
# que vous modifierez dans la boucle for#
for i in range(len(nom_fichier),0):
    print(nom_fichier[i])
    
print(exercice_sep)

# Q4 Vérifiez si le mot un_mot est un palindrome  
# Vous pouvez commencer par inverser un_mot dans un_autre_mot
# Puis comparez les deux mots
# Faites ensuite la structure if...else... pour afficher les messages suivants:
#    Si la condition est vraie, affichez un message comme quoi le mot est un palindrome
#    Si la contition est fausse, affichez un message comme quoi le mot trouvé n'est pas un palindrom

# Ainsi, avec le mot "kayak" le résultat attendu est "Le mot kayak est un palindrome"
un_mot = 'ananas'
for i in range(len(un_mot),0):
    un_autre_mot = print(un_mot[i])
if (un_mot == un_autre_mot):
    print("En effet, ce mot est un palindrome.")
else:
    print("Ce mot n'est pas un palindrome.")

print(exercice_sep)

# Q5 Changez la question précédente pour obtenir un mot de l'usager 
# Faire en sorte que ce code fonctionne en boucle tant que le mot entré n'est pas 'stop' #
while un_mot != 'stop':
    print(un_mot)

print (exercice_sep)