#Parent
class Personne:
    def __init__(self, nom, prenom, date_naissance) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
#Enfant
class Employe(Personne):
    def __init__(self, nom, prenom, date_naissance, nas, poste, salaire):
        super().__init__(nom, prenom, date_naissance)
        self.nas = nas
        self.poste = poste
        self.salaire = salaire
class Film:
    def __init__(self, nom_film, date_sortie):
        self.nom_film = nom_film
        self.liste_employes = []
        self.date_sortie = date_sortie
class Realisateur(Employe):
    def __init__(self, Bonus):
        self.bonus = Bonus
class Acteur(Employe):
    def __init__(self, role):
        self.role = role

#Instanciations
film_titanic = Film("Titanic","Le 19 décembre 1997")
film_abyss = Film("Abyss","Le 9 août 1989")
film_avatar = Film("Avatar","Le 18 décembre 2009")
realisateur_james_cameroun = Realisateur()