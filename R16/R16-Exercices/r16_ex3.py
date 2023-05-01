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
    def __init__(self, nom_film, date_sortie, liste_employes=[]):
        self.nom_film = nom_film
        self.liste_employes = liste_employes
        self.date_sortie = date_sortie
        liste_employes = []
class Realisateur(Employe):
    def __init__(self, date_naissance, Bonus):
        self.date_naissance = date_naissance
        self.bonus = Bonus
class Acteur(Employe):
    def __init__(self, role):
        self.role = role

#Instanciations:
film_titanic = Film("Titanic","Le 19 décembre 1997")
film_abyss = Film("Abyss","Le 9 août 1989")
realisateur_james_cameroun = Realisateur("Le 16 août 1964","60 000$")
#Équipe Titanic
employe_titanic_1 = Employe("Leboeuf","Marcel","Le 14 juillet 1989","22445566","Figurant","3 000$")
employe_titanic_2 = Employe("Dufresne","Fabrice","Le 11 mars 1995","88997766","Assistant aux déguisements","1 300$")
acteur_titanic = Acteur("Pour Titanic, Leonardo Dicaprio : Jack")
#Employés Abyss
employe_abyss_1 = Employe("Wolfeschlegelsteinhausenbergerdorff","Bob","Le 1er avril 1990","12345678","Figurant","3 500$")
employe_abyss_2 = Employe("Turpis","Béatrice","Le 3 septembre 1999","87654321","Maquilleuse","20$")
acteur_abyss = Acteur("Pour Abyss, Mary Elizabeth Mastrantonio : Lindsey Brigman")
#Employés et Film Avatar
employe_avatar_1 = Employe("Thunderbolt","Zeus","Le 28 décembre 1978","34567890","Électricien","2 000$")
employe_avatar_2 = Employe("Bobette","Georgette","Le 12 mars 2002","34567890","Figurante","300$")
actrice_avatar = Acteur("Pour Avatar, Zoe Saldana : Naytiri")
liste_employes_avatar = [employe_avatar_1, employe_avatar_2, actrice_avatar]
film_avatar = Film("Avatar","Le 18 décembre 2009", liste_employes_avatar)

#Tests
print(f"Informations sur le réalisateur : {realisateur_james_cameroun.date_naissance}, {realisateur_james_cameroun.bonus}")
print(f"Acteurs jouant un rôle principal : {acteur_titanic.role}, {acteur_abyss.role}, {actrice_avatar.role}, ")
print(f"Informations sur le film Avatar : {film_avatar.date_sortie}, {film_avatar.nom_film}, ") 
for info in liste_employes_avatar:
    print(info)
