#Voyez l'énoncé R20 Exercice 2 Calculer_paie.docx

#On veut calculer la paie des employes
#Mais on a des employés payés à la semaine pour un montant fixe
#On a aussi des employés payés à la semaine pour un montant fixe ET qui ont aussi une commission 
#On a aussi des employés payés à l'heure

from abc import ABC,abstractmethod

class Systeme_de_paie:
    pass
    @staticmethod
    def afficher_paie():
        pass
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
        pass
class Employe_heure(Employe):  
    def __init__(self, id_employe, nom, heures_travaillees, taux_horaire):
       super().__init__(id_employe, nom)
       self.heures_travaillees = heures_travaillees
       self.taux_horaire = taux_horaire
    def calculer_paie(self):
        pass
    
class Employe_Commission(Employe_salaire):  
    def __init__(self, id_employe, nom, salaire_par_semaine, commission):
        super().__init__(id_employe, nom, salaire_par_semaine)
        self.commission = commission
    def calculer_paie(self):
        pass 

#Instanciation des objets 


 