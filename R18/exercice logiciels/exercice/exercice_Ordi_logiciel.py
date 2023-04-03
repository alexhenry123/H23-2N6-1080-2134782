class Ordinateur:
    processeur = "Intel 8 core"
    memoire_vive = "16 Go"
    def __init__(self,ID, adresseIP, processeur=None, memoire_vive=None) -> None:
        self.ID = ID
        self.adresseIP = adresseIP
        self.processeur = processeur
        self.memoire_vive = memoire_vive
    def __str__(self) -> str:
        return f"La valeur passée de la classe Ordinateur est : {self}"
    @classmethod
    def upgrader_processeur(cls, nouveau_processeur) -> None:
        Ordinateur.processeur = nouveau_processeur
    @classmethod
    def upgrader_memoire(cls, nouvelle_norme) -> None:
        Ordinateur.memoire_vive = nouvelle_norme
    
class Poste_de_travail(Ordinateur):
    def __init__(self,ID, adresseIP, utilisation,processeur=None, memoire_vive=None) -> None:
        pass
    def installer_logiciel(self,logiciel,version) -> None:
        pass 
    def desinstaller_logiciel(self,logiciel,version) -> None:
        pass 
    def imprimer_liste_logiciels(self) -> None:
        pass
    

