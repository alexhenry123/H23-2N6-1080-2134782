class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, couleur, prix, etat="neuf") -> None:
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.couleur = couleur
        self.prix = prix
        self.etat = etat
    def imprimer_infos():
        print(f'{Voiture.marque} {Voiture.modele} {Voiture.annee} de couleur {Voiture.couleur}, avec seulement {Voiture.kilometrage} km. Pour un prix raisonnable de {Voiture.prix}$ (payable en 12 versements de {Voiture.prix / 12}$) dans un état {Voiture.etat}!')
class Voiture_electrique(Voiture):
    def __init__(self, marque, modele, annee, kilometrage, couleur, prix, autonomie_max,autonomie_actuelle,type_recharge, etat="neuf"):
        super().__init__(marque, modele, annee, kilometrage, couleur, prix, etat)
        self.autonomie_max = autonomie_max
        self.autonomie_actuelle = autonomie_actuelle
        self.type_recharge = type_recharge
    def recharger(temps):
        if Voiture_electrique.autonomie_actuelle (temps / 2) * 40 <= Voiture_electrique.autonomie_max:
            Voiture_electrique.autonomie_actuelle += (temps / 2) * 40
