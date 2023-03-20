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
        Inscription.no_confirmation = 0
        print(f"Votre inscription au numéro de confirmation : {random.randint(1,100000)} a bien été annulée.")
    
#Étape 2 : Tests et instanciations
inscription_1 = Inscription('Gandalf le magnifique','Magicien')
inscription_2 = Inscription('Thornal le ténébreux','Guerrier')
#Tests
Inscription.confirmer(inscription_1)
Inscription.canceller(inscription_1)