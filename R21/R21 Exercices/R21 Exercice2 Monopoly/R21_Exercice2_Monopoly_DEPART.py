
# Maintenant que nous sommes plus expérimentés, 
# nous allons mieux encapsuler les attributs de nos classes.

# Voyez l'énoncé pour voir ce que vous devez faire
class Terrain:
    def __init__(self,nom,couleur,est_a_vendre,prix) -> None:
        self._nom = nom
        self._couleur = couleur
        self._prix = prix
        # @nom.setter
        # def nom(self, nom):
        #     return "Il est impossible de changer le nom."
        # @couleur.setter
        # def couleur(self):
        #     return "Il est impossible de changer la couleur."
        @prix.setter
        def prix(self,nvx_prix):
            try:
                if nvx_prix > self._prix:
                    self._prix = nvx_prix
            except ValueError:
                print("La nouvelle valeur doit être supérieure à l'ancienne.")                
    def __str__(self) -> str:
        return self.nom
class Banque:
    def __init__(self,montant_cash,liste_terrains, montant_parc_immobilier) -> None:
        self._montant_cash = montant_cash
        self.liste_terrains = liste_terrains
        self._montant_parc_immobilier = montant_parc_immobilier
        @montant_cash.setter
        def montant_cash(self,nvx_montant_cash):
            try:
                if isinstance(nvx_montant_cash, float):
                    self._montant_cash == nvx_montant_cash
                    print(f"Le montant a été changé pour {self._montant_cash}")
            except ValueError:
                print("Le montant cash doit être une valeur décimale (00.0).")
    @staticmethod
    def calculer_montant_immobilier(liste_terrains):
        somme_terrains = 0
        for terrain in liste_terrains:
            somme_terrains += terrain
        return somme_terrains
class Joueur:
    def __init__(self,montant_cash,list_terrains) -> None:
        self._montant_cash = montant_cash
        self.list_terrains = list_terrains

    def acheter(self,proprietaire,terrain:Terrain): 
        if self.montant_cash >= terrain.prix:
            if (terrain in proprietaire.list_terrains):
                proprietaire.list_terrains.remove(terrain)
                self.list_terrains.append(terrain)
                proprietaire.montant_cash += terrain.prix
                self.montant_cash -= terrain.prix
            else:
                print("Désolé, je n'ai pas ce terrain à vendre")
        else:
            print("Vous n'avez pas suffisament d'argent.")

# -----Tests et instanciations------

#-	‘Avenue Kentucky’, rouge, 220000
#-	‘Avenue Pennsylvanie’, vert, 320000
#-	‘Promenade’, bleu, 400000
#Instanciez la banque, avec 22 millions de cash, et la liste de ces 3 terrains
#Instanciez un joueur qui a 1 million et une liste vide de terrains.
kentucky = Terrain('Avenue Kentucky','rouge',True,220000)
pennsylvanie = Terrain('Avenue Pensylvanie','vert',True,320000)
promenade = Terrain('Promenade','bleu',True,400000)

banque = Banque(22000000,[kentucky,pennsylvanie,promenade])

joueur1 = Joueur(1000000,[])
joueur2 = Joueur(1000000,[])

liste_terrains = []
liste_terrains.append(kentucky.prix, pennsylvanie.prix, promenade.prix)

Banque.calculer_montant_immobilier(liste_terrains)

promenade._couleur


































# print("joueur1 essaie d'acheter à la banque le terrain promenade")
# joueur1.acheter(banque,promenade)

# print('infos du joueur 1')
# print(joueur1.montant_cash)
# for terrain in joueur1.list_terrains:
#     print(terrain)
# #print(joueur1.list_terrains)

# print('infos de la banque')
# print(banque.montant_cash)
# for terrain in banque.list_terrains:
#     print(terrain)
# #print(banque.list_terrains)


# print("joueur2 essaie d'acheter au joueur1 le terrain promenade")
# joueur2.acheter(joueur1,promenade)
# print('infos du joueur 2')
# print(joueur2.montant_cash)
# for terrain in joueur2.list_terrains:
#     print(terrain)
    
# print('infos du joueur 1')
# print(joueur1.montant_cash)
# for terrain in joueur1.list_terrains:
#     print(terrain)
    
# print('infos de la banque')
# print(banque.montant_cash)
# for terrain in banque.list_terrains:
#     print(terrain)    

# print("joueur2 essaie d'acheter au joueur1 un terrain que le joueur1 n'a pas")
# # joueur2 essaie d'acheter au joueur1 un terrain que le joueur1 n'a pas
# joueur2.acheter(joueur1,kentucky)
# print('infos du joueur 1')
# print(joueur1.montant_cash)
# for terrain in joueur1.list_terrains:
#     print(terrain)
    
# print('infos du joueur 2')
# print(joueur2.montant_cash)
# for terrain in joueur2.list_terrains:
#     print(terrain)
    
# print('infos de la banque')
# print(banque.montant_cash)
# for terrain in banque.list_terrains:
#     print(terrain)   