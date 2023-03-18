# Ce script sert à corriger des listes de noms ayant des espaces superflus.
# On répète les mêmes lignes de code pour chaque groupe.
# Écrivez une fonction qui permettra d'enlever la duplication de code.
# La structure de la fonction est déjà amorcée.
# L'exécution de votre script devra donner le même résultat que l'exécution du script original
#       c'est-à-dire 3 nouvelles listes de groupes contenant les mêmes noms mais sans espaces superflus.


liste_noms_groupe1 = [" Anna Jacobs","Bertand Dupier ", "Catherine Deschamps", "   William Dupont", "     Loise Vilmar  ", " Toca Lombe"]
liste_noms_groupe2 = [" Mienne Lambert", " Justin Tremblay", " Pok Holmes", "Gertrude Dupé", "Harry Potter   ", "   Garry Smother"]
liste_noms_groupe3 = ["Gard Longe ", " Untel Aknom ", "William Dupont III ", " Steven Stevenson  "]

def correction_espaces_supp(liste):
    liste_corrigee = []
    for nom in liste:
        nom_corrige = nom.strip()
        liste_corrigee.append(nom_corrige)
    return liste_corrigee

#Correction:
#..."" pour les trois listes
liste_groupe1_stripped = correction_espaces_supp(liste_noms_groupe1)
liste_groupe2_stripped = correction_espaces_supp(liste_noms_groupe2)
liste_groupe3_stripped = correction_espaces_supp(liste_noms_groupe3)

#..."" pour les trois listes
print(liste_groupe1_stripped)
print(liste_groupe2_stripped)
print(liste_groupe3_stripped)


#Moi:

#Appel
#correction_espaces_supp(liste_noms_groupe1)

#Imprimer résultat
#print(correction_espaces_supp(liste_noms_groupe1))