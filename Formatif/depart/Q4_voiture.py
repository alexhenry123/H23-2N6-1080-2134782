class Voiture:
    def __init__(self,marque,model,annee,prix,kilometrage) -> None:
        self.marque = marque
        self.model = model
        self.annee = annee
        self.prix = prix
        self.kilometrage = kilometrage





truck = Voiture("Ford","Edge",2018,24500,11400)
print()
print(f'Un {truck.marque} {truck.model} au prix de base de {truck.prix}$, mais seulement {truck.obtenir_prix()}$ avec le rabais.')
# Vous devriez obtenir la ligne suivante dans le terminal :
#       Un Ford Edge au prix de base de 24500$, mais seulement 23930.0$ avec le rabais.
print()