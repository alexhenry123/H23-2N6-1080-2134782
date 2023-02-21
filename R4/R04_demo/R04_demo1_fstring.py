prenom = input("Entrez votre prenom : ")
nom = input("Entrez votre nom : ")
personne_rendez_vous = input("Avec qui avez-vous rendez-vous ? : ")
print()

print("Bonjour Mr." + prenom.capitalize() + " " + nom + ", bienvenue." +
      "\nDr." + personne_rendez_vous + " à été informé de votre arriver.")
print()



print(f"""Bonjour Mr.{prenom.capitalize()} {nom}, bienvenue.
Dr.{personne_rendez_vous} à été informé de votre arriver.""" )
print()