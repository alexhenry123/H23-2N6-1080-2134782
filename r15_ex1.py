class Compte:
    def __init__(self,no_compte,type_compte,nip_client,solde=0):
        self.no_compte = no_compte
        self.type_compte = type_compte
        self.nip_client = nip_client
        self.solde = solde
    def deposer(self,montant_a_deposer):
        solde += montant_a_deposer
        return montant_a_deposer
    def retirer(self,montant_a_retirer):
        if montant_a_retirer <= montant_a_deposer:
            solde -= montant_a_retirer
        else:
            print(f'Votre solde est de {montant_a_deposer} : ce qui est inférieur au montant de {montant_a_retirer} que vous voulez retirer.')

#Variables (à modifier)
montant_a_deposer = 50
montant_a_retirer = 3

#Comptes créés
compte_1 = Compte('12345678','chèque','888888888')
compte_2 = Compte('23456789','épargne','888888888')
#Méthodes appelées
compte_1.deposer(montant_a_deposer)
compte_1.retirer(montant_a_retirer)
