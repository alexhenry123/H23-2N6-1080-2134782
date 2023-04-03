import csv
class Ordinateur:
    processeur = "Ryzen 3600"
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
    def __init__(self,ID, adresseIP, utilisation, processeur=None, memoire_vive=None) -> None:
        super().__init__(ID,adresseIP,utilisation,processeur,memoire_vive)     
        self.utilisation = utilisation 
    def installer_logiciel(self,logiciel,version) -> None:
        Poste_de_travail.logiciel = logiciel
        Poste_de_travail.version = version 
    def desinstaller_logiciel(self,logiciel,version) -> None:
        Poste_de_travail.logiciel -= logiciel
        Poste_de_travail.version -= version 
    def imprimer_liste_logiciels(fichier_csv) -> None:
        print(f"{fichier_csv}")  

#Charger logiciels avec lecture du fichier texte (appel d'une méthode)
def charger_logiciels(poste_de_travail):
    with open("logiciels2022_2023.csv","r",encoding="utf-8") as fichier_csv:
        ligne_csv = csv.reader(fichier_csv)
        next(ligne_csv)
        for ligne in fichier_csv:
            #Si le poste est celui d'un(e) professeur(e)
            if ligne[2] == "info":                    
                return f"""Un ordi de prof, avec l’ID {poste_de_travail.ID}, l’adresse IP {poste_de_travail.adresseIP}, une utilisation {poste_de_travail.utilisation}, le processeur {poste_de_travail.processeur} et une mémoire vive de {poste_de_travail.memoire_vive}.
                
            L'utilisation {poste_de_travail.utilisation} veut dire que tous les logiciels seront installés sur le poste."""
            #Si le poste est celui d'un étudiant en programmation
            elif ligne[2] == "info-prog":
                return f"""Un ordi de prof, avec l’ID {poste_de_travail.ID}, l’adresse IP {poste_de_travail.adresseIP}, une utilisation {poste_de_travail.utilisation}, le processeur {poste_de_travail.processeur} et une mémoire vive de {poste_de_travail.memoire_vive}.
                
            L'utilisation {poste_de_travail.utilisation} veut dire que tous les logiciels seront installés sur le poste."""
            #Si le poste est celui d'un étudiant en réseau
            elif ligne[2] == "info-réseau":
                return f"""Un ordi de réseau, avec l’ID {poste_de_travail.ID}, l’adresse IP {poste_de_travail.adresseIP}, une utilisation {poste_de_travail.utilisation}, le processeur {poste_de_travail.processeur} et une mémoire vive de {poste_de_travail.memoire_vive}.
                
            L’utilisation {poste_de_travail.utilisation} veut dire que les logiciels'info' et 'info-réseau' seront installés sur le poste."""
                                
#Instancier les 3 postes de travail
poste_prof = Poste_de_travail("LPFINFOPORT001","192.168.221.21","info","par défaut","32 Go")
poste_réseau = Poste_de_travail("LLBINFO060208","192.168.219.21","info-réseau","par défaut","par défaut")
poste_prog = Poste_de_travail("LLBINFO060505","192.168.220.17","info-prog","par défaut","par défaut")

#Test 1 :
Poste_de_travail.charger_logiciels(poste_prof)