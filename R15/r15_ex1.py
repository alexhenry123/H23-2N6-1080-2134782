#Création de la classe
class Compte:
    def __init__(self,no_compte,type_compte,nip_client):
        self.no_compte = no_compte
        self.type_compte = type_compte
        self.nip_client = nip_client
        self.solde = 0
    def deposer(self,montant_a_deposer):
        self.solde += montant_a_deposer
        return self.solde
    def retirer(self,montant_a_retirer):
        if montant_a_retirer <= montant_a_deposer:
            self.solde -= montant_a_retirer
        else:
            print(f'Votre solde est de {montant_a_deposer} : ce qui est inférieur au montant de {montant_a_retirer} que vous voulez retirer.')

#Variables (à modifier)
montant_a_retirer = 0
montant_a_deposer = 5000

#Comptes créés
compte_1 = Compte('12345678','chèque','888888888')
compte_2 = Compte('23456789','épargne','888888888')

#Étape 2 : Tests des propriétés et des méthodes
print(compte_1.solde)
compte_1.retirer(montant_a_retirer)
compte_2.deposer(montant_a_deposer)
print(f"Le solde du compte après dépôt : {compte_2.solde}")

