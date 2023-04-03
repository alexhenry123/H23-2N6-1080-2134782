#Création des classes
class Departement:
    def __init__(self, id, nom, budget_annuel) -> None:
        self.id = id
        self.nom = nom
        self.budget_annuel = budget_annuel
    def achat_equipement():
        pass
class Achat:
    def __init__(self, budget, liste_achats, est_paye=False) -> None:
        self.budget = budget
        self.est_paye = est_paye
        self.liste_achats = liste_achats
        liste_achats = []
    #A terminer
    def calculer_total_estime():
        pass
    def payer():
        Achat.est_paye = True
        #Écrire nouvelle liste (...)
class Equipement:
    montant_equipement = 0
    def __init__(self, id, nom_equipement, cie, modele, qty, prix_unitaire) -> None:
        self.id = id
        self.nom_equipement = nom_equipement
        self.cie = cie
        self.modele = modele
        self.qty = qty
        self.prix_unitaire = prix_unitaire
        Equipement.montant_equipement = qty * prix_unitaire
    def from_string(self, id, nom_equipement, cie, modele, qty, prix):
        pass