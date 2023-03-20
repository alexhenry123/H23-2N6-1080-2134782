import datetime
import random
class Inscription:
    def __init__(self,alias,role) -> None:
        self.alias = alias
        self.role = role
        self.date_inscription = datetime.date.today()
        self.cout = 45
        self.no_confirmation = random.randint(1,100000)
    def confirmer(inscription):
        print(f"Félicitation {inscription.alias}! Vous êtes inscrit dans le rôle de {inscription.role}. Voici votre numéro de confirmation : {inscription.no_confirmation}")
    def canceller(inscription):
        print(f"Votre inscription au numéro de confirmation : {inscription.no_confirmation} a bien été annulée.")
        inscription.no_confirmation = 0
    
#Étape 2 : Tests et instanciations
inscription_1 = Inscription('Gandalf le magnifique','Magicien')
inscription_2 = Inscription('Thornal le ténébreux','Guerrier')
#Tests
Inscription.confirmer(inscription_1)
Inscription.canceller(inscription_1)
Inscription.canceller(inscription_2)
print(f"Numéro de confirmation de la deuxième inscription (après annulation) : {inscription_2.no_confirmation}")