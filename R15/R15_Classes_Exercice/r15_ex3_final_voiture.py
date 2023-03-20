class Voiture:
    def __init__(self,modele,marque,annee,couleur,kilometrage,prix,etat) -> None:
        self.modele = modele
        self.marque = marque
        self.annee = annee
        self.couleur = couleur
        self.kilometrage = kilometrage
        self.prix = prix
        self.etat = etat
        self.etat_df = "Neuf"
    def imprimer_infos(voiture):
        print(f'''{voiture.marque} {voiture.modele} {voiture.annee} de couleur {voiture.couleur}, avec seulement {voiture.kilometrage} km. 
Pour un prix raisonnable de {voiture.prix}$ (payable en 12 versements de {voiture.prix / 12}$) dans un état {voiture.etat}!''')

#Instanciation d'objets
voiture_1 = Voiture(modele='Tercel',marque='Toyota',annee='1972',couleur='rouge',kilometrage='12888888',prix=123,etat='superbe')
voiture_2 = Voiture(modele='E-Class',marque='Mercedes-Benz',annee='2023',couleur='grise',kilometrage='23000',prix=54600,etat='usagé')

#Tests
Voiture.imprimer_infos(voiture_1)
Voiture.imprimer_infos(voiture_2)
