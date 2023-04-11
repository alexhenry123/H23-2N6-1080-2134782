import csv
import os
class Ordinateur:
    processeur = "Ryzen 3600"
    memoire_vive = "16 Go"
    def __init__(self,ID, adresseIP, processeur=None, memoire_vive=None) -> None:
        self.ID = ID
        self.adresseIP = adresseIP
        self.processeur = processeur
        self.memoire_vive = memoire_vive
    def __str__(self) -> str:
        return self
    @classmethod
    def upgrader_processeur(cls, nouveau_processeur) -> None:
        Ordinateur.processeur = nouveau_processeur
    @classmethod
    def upgrader_memoire(cls, nouvelle_norme) -> None:
        Ordinateur.memoire_vive = nouvelle_norme
    
class Poste_de_travail(Ordinateur):
    def __init__(self,ID, adresseIP, utilisation, liste_logiciels, processeur=None, memoire_vive=None) -> None:
        super().__init__(ID,adresseIP,processeur,memoire_vive)     
        self.utilisation = utilisation
        self.liste_logiciels = liste_logiciels 
    def installer_logiciel(self,logiciel,version) -> None:
        self.liste_logiciels += logiciel
        self.liste_logiciels += version 
    def desinstaller_logiciel(self,logiciel,version) -> None:
        self.liste_logiciels -= logiciel
        self.liste_logiciels -= version 
    def imprimer_liste_logiciels(liste_logiciels) -> None:
        print(liste_logiciels)  

#Charger logiciels avec lecture du fichier texte (appel d'une méthode et utilisation d'un Dictionnaire)
<<<<<<< HEAD
    def charger_logiciels(poste_de_travail):
     with open('logiciels2022_2023.csv','r',encoding='utf-8') as fichier_csv:
=======
    def methode_poste_de_travail(poste_de_travail):
     with open("logiciels2022_2023.csv","r",encoding="utf-8") as fichier_csv:
>>>>>>> 97aeae4a1671f97dda08a7d1793e2f5b1673bac1
        ligne_csv = csv.reader(fichier_csv)
        next(ligne_csv)
        dict_logiciels = {"Logiciel","Version"}
        for ligne in fichier_csv:
            #Si le poste est celui d'un(e) professeur(e)
            if ligne[2] == "info":          
<<<<<<< HEAD
                ajout_prof = {"Logiciel":ligne[0],"Version":ligne[1]}          
                dict_logiciels_prof.update(ajout_prof)
            #Si le poste est celui d'un étudiant en programmation
            elif ligne[2] == "info-prog":
                ajout_prog = {"Logiciel":ligne[0],"Version":ligne[1]}          
                dict_logiciels_prog.update(ajout_prog)
            #Si le poste est celui d'un étudiant en réseau
            elif ligne[2] == "info-réseau":
                ajout_réseau = {"Logiciel":ligne[0],"Version":ligne[1]}          
                dict_logiciels_réseau.update(ajout_réseau)     
    # def charger_logiciels(poste_de_travail):
    #     if poste_de_travail.utilisation == "info":
    #         print("Logiciels du prof :")
    #         for logiciel in poste_de_travail.logiciel:
    #             return logiciel
    #     elif poste_de_travail.utilisation == "info-prog":
    #         print("Logiciels de prog :")
    #         for logiciel in poste_de_travail.logiciel:
    #             return logiciel
    #     elif poste_de_travail.utilisation == "info-réseau":
    #         print("Logiciels de réseau :")
    #         for logiciel in poste_de_travail.logiciel:
    #             return logiciel
=======
                ajout_prof = {"Logiciel":poste_de_travail.logiciel,"Version":poste_de_travail.version}          
                dict_logiciels.update(ajout_prof)
                poste_de_travail.logiciel += dict_logiciels
            #Si le poste est celui d'un étudiant en programmation
            elif ligne[2] == "info-prog":
                ajout_prog = {"Logiciel":poste_de_travail.logiciel,"Version":poste_de_travail.version}          
                dict_logiciels.update(ajout_prog)
                poste_de_travail.logiciel += dict_logiciels
            #Si le poste est celui d'un étudiant en réseau
            elif ligne[2] == "info-réseau":
                ajout_réseau = {"Logiciel":poste_de_travail.logiciel,"Version":poste_de_travail.version}          
                dict_logiciels.update(ajout_réseau)
                poste_de_travail.logiciel += dict_logiciels
            
    def charger_logiciels(poste_de_travail):
        if poste_de_travail.utilisation == "info":
            print("Logiciels du prof :")
            for logiciel in poste_de_travail.logiciel:
                print(logiciel)
        elif poste_de_travail.utilisation == "info-prog":
            print("Logiciels de prog :")
            for logiciel in poste_de_travail.logiciel:
                print(logiciel)
        elif poste_de_travail.utilisation == "info-réseau":
            print("Logiciels de réseau :")
            for logiciel in poste_de_travail.logiciel:
                print(logiciel)
>>>>>>> 97aeae4a1671f97dda08a7d1793e2f5b1673bac1
                                
#Instancier les 3 postes de travail
poste_prof = Poste_de_travail("LPFINFOPORT001","192.168.221.21","info","par défaut","32 Go")
poste_réseau = Poste_de_travail("LLBINFO060208","192.168.219.21","info-réseau","par défaut","par défaut")
poste_prog = Poste_de_travail("LLBINFO060505","192.168.220.17","info-prog","par défaut","par défaut")

#Test 1 :
Poste_de_travail.charger_logiciels(poste_prof)