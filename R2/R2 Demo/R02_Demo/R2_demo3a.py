#list copy

cours = ['Programmation 1', 'Math', 'Bureautique', 'Réseau 1','Math']
cours2 = cours.copy()
print("\n\n")

print("liste original")
for valeur in cours:
    print(f"ID: {id(valeur)}  Cours: {valeur}")
print("\n\n")
    
print("seconde liste")
for valeur in cours2:
    print(f"ID: {id(valeur)}  Cours: {valeur}")
print("\n\n")
    
cours2[0] = cours2[0]+"01"
print(cours2[0])
print("\n\n")

print("seconde liste")
for valeur in cours2:
    print(f"ID: {id(valeur)}  Cours: {valeur}")
print("\n\n")