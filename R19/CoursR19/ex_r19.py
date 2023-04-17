import datetime
class Employe:
    def __init__(self, id_employe, prenom, nom, role, salaire) -> None:
        self.id_employe = id_employe
        self.prenom = prenom
        self.nom = nom
        self.role = role
        self.salaire = salaire
class Programmeur(Employe):
    def __init__(self, id_employe, prenom, nom, role, salaire, liste_fonctions) -> None:
        super().__init__(id_employe, prenom, nom, role, salaire)
        liste_fonctions = []
        self.liste_fonctions = liste_fonctions
    def coder(fonction):
        Programmeur.liste_fonctions.append(fonction)
class Designer(Employe):
    def __init__(self, id_employe, prenom, nom, role, salaire, liste_artefacts) -> None:
        super().__init__(id_employe, prenom, nom, role, salaire)
        liste_artefacts = []
        self.liste_artefacts = liste_artefacts
    def dessiner(artefact):
        Designer.liste_artefacts.append(artefact)
class Tech_Reseau(Employe):
    def __init__(self, id_employe, prenom, nom, role, salaire, liste_interventions) -> None:
        super().__init__(id_employe, prenom, nom, role, salaire)
        liste_interventions = []
        self.liste_interventions = liste_interventions
    def intervenir(intervention):
        Tech_Reseau.liste_interventions.append(intervention)

class Equipe:
    def __init__(self, nom, liste_employes, compteur_employes_actifs=0) -> None:
        self.nom = nom
        liste_employes = []
        self.liste_employes = liste_employes
        self.compteur_employes_actifs = compteur_employes_actifs

    def ajouter_employe(self, un_employe):
        un_employe.date_debut = datetime.date.today()
        un_employe.date_fin = None
    #Instanciation d'un dictionnaire avec les valeur du paramètre de la méthode
        dict_employe_ajoute = {"Employé":un_employe,
                              "Date de début":un_employe.date_debut,
                              "Date de fin":un_employe.date_fin}
        liste_employes.append(dict_employe_ajoute)
    #Incrémentation du compteur des employés actifs
        for un_employe in self.liste_employes:
            if un_employe.date_fin == None:
                compteur_employes_actifs +=1 
    #Impression du dictionnaire 
        print(f"L'employé suivant a été ajouté : {dict_employe_ajoute}")
    def enlever_employe(self, un_employe):
        un_employe.date_fin = datetime.date.today()
    def imprimer_employes(self, nom_equipe):
        nom_equipe.liste_employes

class Logiciel:
    def __init__(self, nom, etat, liste_equipes) -> None:
        self.nom = nom
        self.etat = etat
        liste_equipes = []
        self.liste_equipes = liste_equipes
    def ajouter_quipe(self, nom_equipe):
        Logiciel.liste_equipes.append(nom_equipe)