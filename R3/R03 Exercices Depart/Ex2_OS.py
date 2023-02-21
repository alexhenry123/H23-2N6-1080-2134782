from cgi import print_directory
import os
from datetime import datetime

# Q1  imprimez le répertoire courant
print(os.getcwd())

print(80*'_')
# Q2   ATTENTION sous windows, la variable d'environnement équivalente à HOME de Linux est USERPROFILE
#      MALGRÉ CELA, on va toujours parler de votre HOME
#   Imprimez la variable d'environnement USERPROFILE
print()

print(80*'_' )
# Q3 Déplacez-vous sur le répertoire 'Desktop' de votre HOME                            #
# Et imprimez le répertoire courant                                                     #
desk = "C:\\Users\\2134782\\Desktop"
os.chdir(desk)
print(f"Voici le répertoire courant : {os.getcwd()}")

print(80*'_' )
# Q4   Imprimez la liste des répertoires et des fichiers qu'il y a dans votre Desktop   #

#Test commit / push


print(80*'_' )
# Q5   Créez un répertoire OS-DemoQ5                                               #
# Et réimprimez les répertoires et les fichiers dans votre Desktop                      #



print(80*'_' )
# Q6   création des répertoires  OS-DemoQ6/Subdir1 avec une seule instruction
# Et réimprimez les répertoires et les fichiers dans votre Desktop                      #



print(80*'_' )
#Q7   Renommez le répertoire Subdir1 pour qu'il s'appelle Sous_repertoire



print(80*'_' )
# Q8   suppression du répertoire OS-DemoQ6 et de son contenu
# Et réimprimez les répertoires et les fichiers dans votre bureau#





print(80*'_' )
