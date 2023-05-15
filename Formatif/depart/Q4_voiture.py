class Voiture:
    def __init__(self,marque,modele,annee,prix,kilometrage) -> None:
        self.marque = marque
        self.modele= modele
        self.annee = annee
        self.prix = prix
        self.kilometrage = kilometrage
    @staticmethod
    def __calculer_prix_vente(prix, kilometrage):
        rabais = kilometrage * 0.05
        if rabais > 7000:
            rabais = 7000
        prix_vente_final = prix - rabais
        return prix_vente_final
    def obtenir_prix(self):
        return self.__calculer_prix_vente(self.prix, self.kilometrage)


truck = Voiture("Ford","Edge",2018,24500,11400)

print(f'Un {truck.marque} {truck.modele} au prix de base de {truck.prix}$, mais seulement {truck.obtenir_prix()}$ avec le rabais.')
# Vous devriez obtenir la ligne suivante dans le terminal :
#       Un Ford Edge au prix de base de 24500$, mais seulement 23930.0$ avec le rabais.
