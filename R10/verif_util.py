import os

#Vérifier l'utilisateur courant
user = os.getenv("USERNAME")

#Appel d'une méthode
def verification():
    if user == "2134782":
        print(f"Bienvenue {user}")  
    else:
        print("Utilisateur non-attendu")