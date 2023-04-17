from abc import ABC, abstractmethod

class OBNL:
    def __init__(self, liste_donateurs) -> None:
        self.liste_donateurs = liste_donateurs
    @staticmethod
    def afficher_dons(liste_donateurs):
        print("""Dons publiques des donateurs : 
==============================""")
        for info in liste_donateurs:
            if info.estPublique == True:
                print(f"""Don de : {info.nom}
 - montant net de : {info.donner()}""")
class Donateur(ABC):
    @abstractmethod
    def donner(self):
        pass
    def __init__(self, nom, estPublique) -> None:
        self.nom = nom
        self.estPublique = estPublique
class Donateur_Riche(Donateur):
    def __init__(self, nom, estPublique, contribution) -> None:
        super().__init__(nom, estPublique)
        self.contribution = contribution
    def donner(self):
        return self.contribution
class Donateur_Expert(Donateur):
    def __init__(self, nom, estPublique, contribution, expertise) -> None:
        super().__init__(nom, estPublique)
        self.contribution = contribution
        self.expertise = expertise
    def donner(self):
        return self.contribution * 120
    
#Instanciations et tests
don1 = Donateur_Riche("Marc Tremblay",False,120000)
don2 = Donateur_Riche("Jean Tremblay",True,1200000)
don3 = Donateur_Expert("Pierre Johnson",True,120,"comptabilité")

OBNL.liste_donateurs = []
def ajouter_donateur(donateur):
    if OBNL.liste_donateurs != donateur:
        OBNL.liste_donateurs.append(donateur)
ajouter_donateur(don1)
ajouter_donateur(don2)
ajouter_donateur(don3)

obnl1 = OBNL.afficher_dons(OBNL.liste_donateurs)