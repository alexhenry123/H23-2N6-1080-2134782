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
    def recharger(voiture,temps):
        if voiture.type_recharge == "Niveau 2":
            if voiture.autonomie_actuelle + (temps / 120) * 40 <= voiture.autonomie_max:
                voiture.autonomie_actuelle += (temps / 120) * 40
        elif voiture.type_recharge == "Rapide(100kw)":
            if voiture.autonomie_actuelle + (temps / 8) * 40 <= voiture.autonomie_max:
                voiture.autonomie_actuelle += (temps / 8) * 40
        elif voiture.type_recharge == "Rapide(300kw)":
            if voiture.autonomie_actuelle + (temps / 2) * 40 <= voiture.autonomie_max:
                voiture.autonomie_actuelle += (temps / 2) * 40

#Instanciations
auto_Paul = Voiture_electrique("Audi","Q8",2001,10,"jaune",68000,400,30,"Rapide(100kw)")
auto_Lucie = Voiture_electrique("Chevrolet","Silverado",2023,10,"argent",86000,640,30,"Rapide(300kw)")

#Tests
print(f"Autonomie actuelle de l'auto : {auto_Lucie.autonomie_actuelle}")
Voiture_electrique.recharger(auto_Lucie,10)
print(f"Autonomie actuelle de l'auto après rechargement : {auto_Lucie.autonomie_actuelle}")