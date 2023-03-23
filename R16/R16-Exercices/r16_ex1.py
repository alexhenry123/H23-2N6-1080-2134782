#Parent
class Personne:
    def __init__(self,nom,prenom,date_naissance) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
#Enfant
class Joueur(Personne):
    def __init__(self,nom,prenom,date_naissance, no_chandail,position):
        super().__init__(nom, prenom, date_naissance)
        self.no_chandail = no_chandail
        self.position = position

class Attaquant(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position, nb_tirs_au_but,nb_assistances):
        super().__init__(nom, prenom, date_naissance, no_chandail, position)
        self.nb_tirs_au_but = nb_tirs_au_but
        self.nb_assistances = nb_assistances
    def compter_but():
        Attaquant.nb_tirs_au_but+=1
class Defenseur(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position, nb_interceptions,nb_passes):
        super().__init__(nom, prenom, date_naissance, no_chandail, position)
        self.nb_interceptions = nb_interceptions
        self.nb_passes = nb_passes
class Gardien(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position, nb_arrets,nb_tirs_essuyes):
        super().__init__(nom, prenom, date_naissance, no_chandail, position)
        self.nb_arrets = nb_arrets
        self.nb_tirs_essuyes = nb_tirs_essuyes
    def arreter_tir():
            Gardien.nb_arrets+=1
class Equipe(Joueur):
    def __init__(self, nom_equipe, liste_joueurs) -> None:
        self.nom_equipe = nom_equipe
        self.liste_joueurs = liste_joueurs
        liste_joueurs = []
    def engager_joueur(joueur):
        liste_joueurs += joueur
    def ejecter_joueur(joueur):
        liste_joueurs -= joueur

#Instanciations:

#Joueurs
gardien_Logan_Ketterer = Gardien("Ketterer","Logan","9 novembre 1993","#1","gardien",128,208)
defenseur_Zachary_Brault_Guillard = Defenseur("Brault-Guillard","Zachary","5 mars 1991","#15","défenseur",32,44)
attaquant_Sunusi_Ibrahim = Attaquant("Ibrahim","Sunusi","1 octobre 2002","#14","attaquant",23,44)
liste_joueurs_equipe1 = gardien_Logan_Ketterer, defenseur_Zachary_Brault_Guillard, attaquant_Sunusi_Ibrahim
#Equipe
equipe_CF_Montreal = Equipe("Équipe 1",liste_joueurs_equipe1)

 
#Test 1
print(f"""Test 1 : {gardien_Logan_Ketterer.date_naissance}, {defenseur_Zachary_Brault_Guillard.date_naissance}, {attaquant_Sunusi_Ibrahim.date_naissance}
""")
#Test 2
print(f"""Test 2 : 
No chandail : 
{gardien_Logan_Ketterer.no_chandail}, {defenseur_Zachary_Brault_Guillard.no_chandail}, {attaquant_Sunusi_Ibrahim.no_chandail}
Positions :
{gardien_Logan_Ketterer.position}, {defenseur_Zachary_Brault_Guillard.position}, {attaquant_Sunusi_Ibrahim.position}
""")
#Test 3 
print(f"""Test 3 : 
Valeurs propres à chaque joueur :
Attaquant : {attaquant_Sunusi_Ibrahim.nb_tirs_au_but}, {attaquant_Sunusi_Ibrahim.nb_assistances}
Défenseur : {defenseur_Zachary_Brault_Guillard.nb_interceptions}, {defenseur_Zachary_Brault_Guillard.nb_passes}
Gardien : {gardien_Logan_Ketterer.nb_arrets}, {gardien_Logan_Ketterer.nb_tirs_essuyes}
""")
#Test 4
print(f"Test 4 :")
for joueur in equipe_CF_Montreal.liste_joueurs:
    print(joueur.nom)