#list copy
def impression_liste (texte,liste):
    print(texte)
    for valeur in liste:
        print(f"ID: {id(valeur)}  Cours: {valeur}")
    print("")


cours_info_S2 = [['Programmation 2', 'Math', 'Réseaux locaux', 'Services Intranet'],['Philosophie', 'Francais', 'Anglais']]
amy_liste_cours = cours_info_S2.copy()
print("\n\n")

impression_liste("liste de cours",cours_info_S2 )
    
impression_liste("liste de cours d'Amy",amy_liste_cours )

#On ajoute le cours d'éducation physique "volley-ball" à Amy
print("\n\n")
amy_liste_cours[1].append("Volley-ball")

impression_liste("liste de cours d'Amy avec volley-ball",amy_liste_cours )

impression_liste("liste de cours original",cours_info_S2 )
    
# liste de cours de Steve
print("\n\n")
steve_liste_cours = cours_info_S2.copy()
impression_liste("liste de cours de Steve",steve_liste_cours )
