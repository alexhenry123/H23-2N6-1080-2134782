#Parent
class Personne:
    def __init__(self,nom,prenom,date_naissance) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
#Enfant
class Joueur(Personne):
    def __init__(self,nom,prenom,date_naissance, no_chandail,position):
        super().__init__(nom, prenom, date_naissance)
        self.no_chandail = no_chandail
        self.position = position

class Attaquant(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position, nb_tirs_au_but,nb_assistance):
        super().__init__(nom, prenom, date_naissance, no_chandail, position)
        self.nb_tirs_au_but = nb_tirs_au_but
        self.nb_assistance = nb_assistance
    def compter_but():
        total_buts = 0
        total_buts += Attaquant.nb_tirs_au_but + Attaquant.nb_assistance
        return total_buts
class Defenseur(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position, nb_interceptions,nb_passes):
        super().__init__(nom, prenom, date_naissance, no_chandail, position)
        self.nb_interceptions = nb_interceptions
        self.nb_passes = nb_passes
class Gardien(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position, nb_arrets,nb_tirs_essuyes):
        super().__init__(nom, prenom, date_naissance, no_chandail, position)
        self.nb_arrets = nb_arrets
        self.nb_tirs_essuyes = nb_tirs_essuyes