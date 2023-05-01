# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 

exercice_sep = "___________________________________"
# Pour chaque question ci-dessous, faites le code demandé puis imprimez toujours exercice_sep ensuite afin de séparer les questions

salutation = "Bonjour"

# Q1 Imprimez chacun des caractères de la variable salutation en utilisant for, len et range #
for i in range(0,len(salutation)):
    print(salutation[i])
    
print(exercice_sep)
    
# Q2 Demandez à l'usager d'entrer un chiffre pair en boucle
# Si le chiffre entré est pair, affichez "Merci, vous avez entré le chiffre X, soit un chiffre pair."  où X est le chiffre entré"
# Si l'usager entre un chiffre impair vous sortez de la boucle et affichez "Non, vous avez entré le chiffre X, et ce n'est pas un chiffre pair." #
chiffre = int
for i in range(0,10):
    chiffre+=2
if chiffre % 2 == 0:
    print(f"Merci, vous avez entré le chiffre {chiffre}, soit un chiffre pair.")
elif chiffre % 2 == 1:
    print(f"Non, vous avez entré le chiffre {chiffre} et ce n'est pas un chiffre pair.")

print (exercice_sep)