import csv
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
        super().__init__(ID,adresseIP,utilisation,processeur,memoire_vive)
    def installer_logiciel(self,logiciel,version) -> None:
        Poste_de_travail.logiciel = logiciel
        Poste_de_travail.version = version 
    def desinstaller_logiciel(self,logiciel,version) -> None:
        Poste_de_travail.logiciel -= logiciel
        Poste_de_travail.version -= version 
    def imprimer_liste_logiciels(self) -> None:
        print(f"{self}")
        
#Lecture du fichier csv
with open("logiciels2022_2023.csv","r",encoding="utf-8") as fichier_csv:
    ligne_csv = csv.reader(fichier_csv)
    next(ligne_csv)
    for ligne in fichier_csv:
        if ligne[2] == "info":
            pass
        elif ligne[2] == "info-prog":
            pass
        elif ligne[2] == "info-réseau":
            pass

