# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 


exercice_sep = "___________________________________"
# Pour chaque question ci-dessous, faites le code demandé puis imprimez toujours exercice_sep ensuite afin de séparer les questions


# Q1 Créez 3 amies (amie1, amie2, amie3) et donnez leur des prénoms différents (et différents de mes amies à moi) #
amie1 = "Simone"
amie2 = "Charlotte"
amie3 = "Bernadette"

print(exercice_sep)

# Q2 Pour l'amie1, affichez dans la console les 3 premières lettres de son prénom #
print(amie1[0,2])

print(exercice_sep)

# Q3 Pour l'amie2, affichez dans la console le nombre de lettres qu'il y a dans son nom #
print()

print(exercice_sep)

# Q4 Créez une variable appelée salutation avec la valeur 'Bonne année'  #
salutation = 'Bonne année'

print(exercice_sep)

# Q5 Affichez dans la console un message pour souhaiter 'Bonne année' à vos trois amies, en utilisant salutation et leurs prénoms et en utilisant f' #
print(f"{salutation} {amie1}, {amie2} et {amie3} !")

print(exercice_sep)

# Q6 Affichez dans la console un message pour souhaiter 'BONNE ANNÉE' à vos trois amies, en utilisant salutation et upper(), avec leurs prénoms et en utilisant f' #
print(f"{salutation.upper} {amie1}, {amie2}, {amie3} !")

print(exercice_sep)

# Q7 Affichez dans la console la dernière lettre du prénom de votre troisième amie' #
print(amie3[len(amie3)])
