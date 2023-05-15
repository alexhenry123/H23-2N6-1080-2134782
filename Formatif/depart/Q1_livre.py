class Livre:
    def __init__(self, titre, auteur, date_de_publication) -> None:
        self.titre = titre
        self.auteur = auteur
        self.date_de_publication = date_de_publication
    def obtenir_info(self):
        return f"{self.titre} par {self.auteur} publié en {self.date_de_publication}"

livre_exemple = Livre("L'Alchimiste","Paulo Coelho","1988")
print(livre_exemple.obtenir_info()) 

# devrait imprimer "L'Alchimiste par Paulo Coelho publié en 1988." dans le terminal


