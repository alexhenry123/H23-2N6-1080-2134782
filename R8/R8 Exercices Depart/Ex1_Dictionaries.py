# Les dictionnaires permettent d'associer des valeurs à des données-clés
# L'équivalent des HashMap  ou Associative Arrays dans d'autres languages

# Nous avons ici un dictionnaire qui contient des données sur un étudiant
etudiant = {'nom':'Pierre', 'age':28, 'cours': ['Reseau 1', 'Prog 2 en Python']}
print(f"Q0: le dictionnaire étudiant est au départ: {etudiant}")

print(80*'_')
# C'est vraiment comme un dictionnaire dans la vraie vie
# Les clés nous permettent de rechercher une valeur

print(f"{80*'_'}")
# Q1:  on veut savoir la valeur du nom de l'étudiant en utilisant les f string
#      Dans le terminal on aura: "Q1 Le nom de l'étudiant est : Pierre"  
nom = etudiant['nom']
print(f"Le nom de l'étudiant est {nom}.")

print(f"{80*'_'}")
# Q2: Ajoutez une nouvelle paire clé:valeur dans notre dictionnaire
#  Ajoutez le courriel comme clé et '2112344@cegepmontpetit.ca'
#  Dans le terminal on veut avoir: Q2: Voici le courriel de l'étudiant qui a été ajouté: 2112344@cegepmontpetit.ca
etudiant.update({"courriel": "2112344@cegepmontpetit.ca"})
courriel = etudiant.get("courriel")
print(f"Q2 : Voici le courriel de l'étudiant qui a été ajouté : {courriel}")

print(f"{80*'_'}")
# Q3: donnez la nouvelle valeur '2000000@cegepmontpetit.ca'  au courriel de l'étudiant
#  Dans le terminal on veut avoir: Q3: Voici le nouveau courriel de l'étudiant: 2000000@cegepmontpetit.ca
etudiant.update({"courriel": "2000000@cegepmontpetit.ca"})
nouveau_courriel = etudiant.get("courriel")
print(f"Q3: Voici le nouveau courriel de l'étudiant : {nouveau_courriel}")

print(f"{80*'_'}")
# Q4: Changer/ajouter plusieurs paires de clés-valeurs en une seule instruction
# Changez le nom pour 'nom':'Lucie', l'âge pour 17 et ajoutez le numéro de téléphone (Tel) avec la valeur '514-321-1234'
# Ici, on change le nom, l'âge et on ajoute le no de téléphone.
# À la fin, imprimez le dictionnaire dans le terminal. 
# Vous devriez avoir le résultat suivant: 
#           Q4: le dictionnaire étudiant est maintenant: {'nom': 'Lucie', 'age': 17, 'cours': ['Reseau 1', 'Prog 2 en Python'], 'courriel': #'2000000@cegepmontpetit.ca', 'Tel': '514-321-1234'}
etudiant.update({"nom": "Lucie",
                 "age": 17,
                 "tel": "514-321-1234"})
print(f"Q4: le dictionnaire étudiant est maintenant: {etudiant}")

print(f"{80*'_'}")
# Q5:  Enlevez la clé 'courriel', ce qui enlèvera alors sa valeur
# Résultat attendu dans le terminal: Q5: Quel est le courriel de l'étudiant: None
del etudiant["courriel"]
courriel_retire = etudiant.get("courriel")
print(f"Q5: Le courriel de l'étudiant est : {courriel_retire}")

print(f"{80*'_'}")
# On peut aussi utiliser la méthode pop et en plus d'enlever la clé, on obtient la valeur qu'on enlève
# Q6: Enlevez la clé 'age' de l'étudiant mais imprimez la valeur qu'elle avait
#      Dans le terminal on veut: Q6: on a enlevé l'âge de l'étudiant, sa valeur était: 17
age_retiree = etudiant.pop("age")
print(f"Q6: on a enlevé l'âge de l'étudiant, sa valeur était : {age_retiree}")

print(f"{80*'_'}")
# On peut obtenir le nombre de paires clés:valeurs dans notre dictionnaire avec la méthode len
# Q7: Combient de paires clés:valeurs avons-nous maintenant dans notre dictionnaire?
#      Dans le terminal: Q7: Nous avons maintenant 3 paires clés valeurs.
long_etudiant = len(etudiant)
print(f"Q7: Nous avons maintenant {long_etudiant} paires clés valeurs.")

print(f"{80*'_'}")
# Q8: Imprimez toutes les clés de notre dictionnaire 
#     Dans le terminal: Q8: Nous avons les clés suivantes: dict_keys(['nom', 'cours', 'Tel'])
clefs_etudiant = etudiant.keys()
print(f"Q8: Nous avons les clés suivantes: {clefs_etudiant}")

print(f"{80*'_'}")
# Q9: Imprimez toutes les valeurs de notre dictionnaire 
#  Dans le terminal: Q9: Nous avons toutes les valeurs suivantes: dict_values(['Lucie', ['Reseau 1', 'Prog 2 en Python'], '514-321-1234'])
valeurs_etudiant = etudiant.values()
print(f"Q9: Nous avons toutes les valeurs suivantes : {valeurs_etudiant}")

print(f"{80*'_'}")
# Q10: Imprimez toutes les clés:valeurs de notre dictionnaire 
#  Dans le terminal: Q10: Nous avons toutes clés:valeurs suivantes: dict_items([('nom', 'Lucie'), ('cours', ['Reseau 1', 'Prog 2 en Python']), #('Tel', '514-321-1234')])
items_etudiant = etudiant.items()
print(f"Q10: Nous avons toutes clés:valeurs suivantes : {items_etudiant}")

print(f"Q11{80*'_'}")
# Q11: Faites une boucle for pour passer à travers toutes les paires clés:valeurs de notre dictionnaire
# Le résultat attendu est :
#           nom Lucie
#           cours ['Reseau 1', 'Prog 2 en Python']
#           Tel 514-321-1234
for keys, values in etudiant.items():
    print(keys,values)