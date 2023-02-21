# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 

from subprocess import check_output

exercice_sep = "___________________________________"
# Pour chaque question ci-dessous, faites le code demandé puis imprimez toujours exercice_sep ensuite afin de séparer les questions


# Q1 Demandez à l'usager d'entrer un nombre entre 1 à 10 #
#    Faites une structure de code conditionnelle pour vérifier si le nombre entré est entre 1 et 10
#    Si oui, affichez "Exellent vous avez entré un nombre entre 1 et 10"
#    Sinon, affichez "Erreur, vous n'avez pas entré un nombre entre 1 et 10"
#    

#Note au lecteur: Écrivez un nombre entre 1 et 10
nombre = 5
if nombre <= 10 and nombre >= 1:
    print("Exellent vous avez entré un nombre entre 1 et 10")
else:
    print ("Erreur, vous n'avez pas entré un nombre entre 1 et 10")

print(exercice_sep)

# Q2 Demandez à l'usager d'entrer un mot#
#    Faites un test pour vérifier si la longueur du mot entré est plus petite ou égale à 5
#    Si oui, affichez "Bien, vous avez utilisé un mot de vocabulaire court"
#    Sinon, faites un autre test pour vérifier si la longueur du mot entré est entre 6 et 10
#          , affichez "Très bien, vous avez utilisé un mot de vocabulaire plus élaboré"
#    Sinon, (pas besoin de test mais dans ce cas la longueur du mot sera supérieure à 10)
#            affichez "Excellent, vous avez un vocabulaire élaboré"

#Note au lecteur: Entrez un mot d'au moins 5 lettres ci-dessous
mot = 'train'
if len(mot) <= 5:
    print("Bien, vous avez utilisé un mot de vocabulaire court")
elif len(mot) >= 6 and len(mot) <= 10:
    print("Très bien, vous avez utilisé un mot de vocabulaire plus élaboré")
elif len(mot) >= 10:
    print("Excellent, vous avez un vocabulaire élaboré")
else:
    print("Vous n'avez pas réussi à écrire un  mot d'au moins 5 caractères")
    
print (exercice_sep)

# Q3 Comme dans l'exercice précédent, mais dans le message, incluez le mot entré et la longueur du mot.
# Par exemple, si le mot entré est "patato", le message affiché sera: 
# "Bien, vous avez entré le mot 'patato', soit un mot de 6 lettres. Vous avez utilisé un mot de vocabulaire plus élaboré"
if len(mot) <= 5:
    print(f"Bien, vous avez entré le mot {mot}, soit un mot de moin utilisé un mot de vocabulaire court")
elif len(mot) >= 6 and len(mot) <= 10:
    print(f"Très bien, vous avez entré le mot {mot}, soit un mot de plus de 6 caractères d'un vocabulaire plus élaboré")
elif len(mot) >= 10:
    print(f"Excellent, vous avez entré le mot {mot}, soit un mot de plus de 10 lettres. Vous avez un vocabulaire élaboré")
else:
    print(f"Votre mot, {mot}, ne possède pas suffisament de caractères")
