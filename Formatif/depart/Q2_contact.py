import email
from sys import settrace


class Contact:
    def __init__(self, nom, prenom, adresse, email, num_telephone) -> None:
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.email = email
        self.num_telephone = num_telephone
    @property
    def email(self):
        if self.email or self.num_telephone == "":
            raise ValueError("Vous devez fournir une adresse email et/ou un numéro de télephone.")
    def mettre_a_jour_info():
        pass
    
contact_complet = Contact("Anastazie","Nisha","165 rue Pieux", "nisha.A@gmail","5142-111-7272")
contact_valide = Contact("Miklos","Warner",email="nisha.A@gmail")
#contact_invalide = Contact("Erkan","Severie","165 rue Pieux") doit causer une erreur lorsque cette ligne est exécutée.