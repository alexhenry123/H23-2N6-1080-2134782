#Voyez l'énoncé R20 Exercice 2 Calculer_paie.docx

#On veut calculer la paie des employes
#Mais on a des employés payés à la semaine pour un montant fixe
#On a aussi des employés payés à la semaine pour un montant fixe ET qui ont aussi une commission 
#On a aussi des employés payés à l'heure

from abc import ABC, abstractmethod

class Systeme_de_paie:
    @staticmethod
    def afficher_paies(ls_employes):
        print("Calcul de la paie des employés :")
        for employe in ls_employes:
            print(f"""Paie de : {employe.nom} - {employe.id_employe}
- montant net de : {employe.calculer_paie()}
                  """)
class Employe(ABC):
    @abstractmethod
    def calculer_paie(self):
        pass
    def __init__(self, id_employe, nom):
        self.id_employe = id_employe
        self.nom = nom
class Employe_salaire(Employe):
    def __init__(self, id_employe, nom, salaire_par_semaine):
        super().__init__(id_employe, nom)
        self.salaire_par_semaine = salaire_par_semaine
    def calculer_paie(self):
        return self.salaire_par_semaine
class Employe_heure(Employe):  
    def __init__(self, id_employe, nom, heures_travaillees, taux_horaire):
       super().__init__(id_employe, nom)
       self.heures_travaillees = heures_travaillees
       self.taux_horaire = taux_horaire
    def calculer_paie(self):
        return self.heures_travaillees * self.taux_horaire
class Employe_Commission(Employe_salaire):  
    def __init__(self, id_employe, nom, salaire_par_semaine, commission):
        super().__init__(id_employe, nom, salaire_par_semaine)
        self.commission = commission
    def calculer_paie(self):
        return self.salaire_par_semaine + self.commission

#Instanciation des objets 
ls_employes = []
employe1 = Employe_salaire(1, "Marc Tremblay", 2100)
employe2 = Employe_heure(2, "Pierre Johnson", 40, 22)
employe3 = Employe_Commission(3, "Luc Toupin", 1400, 600)

@staticmethod
def ajouter_employe(employe):
    if ls_employes != employe:
        ls_employes.append(employe)

ajouter_employe(employe1)
ajouter_employe(employe2)
ajouter_employe(employe3)

Systeme_de_paie.afficher_paies(ls_employes)


 