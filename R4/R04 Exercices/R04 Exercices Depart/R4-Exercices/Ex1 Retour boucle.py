import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script


# Vous avez mis des vidéos sur youtube et vous avez noté, pour chaque vidéo, le nombre de likes des 7 premiers jours de chacun des vidéos
# Ces données sont dans le fichier Ex1_youtube_Nb_Likes.txt


# Vous voulez calculez le total des likes de tous vos vidéos (le dernier de chaque ligne)
# Et imprimer dans le terminal le résultat ainsi "J'ai eu un total de 788502 likes pour mes 3 vidéos"
# Naturellement, le nombre de likes total et le nombre de vidéos sont des données calculées


# Observez le contenu du fichier txt et notez le caractère spécial qui sépare les données
# Si vous êtes fort en programmation, faites le code maintenant
# Si vous avez besoin de plus d'explications, vous pourrez les trouver plus bas dans cet exercice



#Essai #1
#
# with open ("Ex1_youtube_Nb_Likes.txt", "r") as ligne:
#         compteur = 0
#         while ligne != 4:
#              compteur += ligne.seek(8)
# print(f"Mon nombre total de likes pour mes trois vidéos est : {compteur}")




#Essai avec explications supplémentaires
#
nb_likes = 0
nb_videos = 0
with open ("Ex1_youtube_Nb_Likes.txt", "r") as fichier:
       liste_lignes = fichier.readlines()      
       for lignes in liste_lignes:
              ligne_lue = lignes.split('|')
              nb_likes += int(ligne_lue[len(ligne_lue)-1])
              nb_videos += 1
print(f"Le nombre total de likes est : {nb_likes}")


# EXPLICATIONS SUPPLÉMENTAIRES
# Créez des variables:
#           pour additionner le dernier nb de likes de chaque vidéo (total_likes), initialisez-la à 0
#           pour le nombre de vidéos que vous avez (nb_videos) et initialez-la à 0
#           pour contenir les parties de chaque ligne (après le split sur le caractère séparant les données) et initialisez-le à []

# Pour y arriver, utlisant with, ouvrez en lecture le fichier Ex1_youtub_Nb_Likes.txt

# Lisez tout le contenu du fichier dans une variable
# Faites une boucle pour lire chacune des lignes de cette variable contenu
#       Dans la boucle, faites un split de la ligne sur le caractère '|'
#       Prenez le dernier élément de la liste obtenue, transformez le en un entier et ajoutez ce nombre à votre total_likes
#       Augmenter aussi de 1 votre variable nb_videos
# Après la boucle, imprimez le résultat demandé dans le terminal 



