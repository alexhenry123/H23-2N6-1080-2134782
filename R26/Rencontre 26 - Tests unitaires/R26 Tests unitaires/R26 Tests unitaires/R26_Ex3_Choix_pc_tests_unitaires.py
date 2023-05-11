import customtkinter as ctk
import R26_Ex3_Choix_pc as Cpc
import unittest
from constant import *


class Test_estimer(unittest.TestCase):

    def test_estimer_sans_processeur(self):
        # Instanciez la classe Choix
        choix_1 = Cpc.Choix()
        # Testez que le choix du processeur est   "Choisis ton processeur    "
        self.assertEqual(choix_1.choix_processeur.get(), "Choisis ton processeur    ")
        # Faites l'appel de la méthode estimer()
        choix_1.estimer()
        # Vérifier que le texte du lbl_message est égal à "Tu dois choisir un processeur"
        self.assertEqual(choix_1.lbl_message._text, "Tu dois choisir un processeur")

    def test_estimer_sans_carte_graphique(self):
        # Cette fois-ci donnez un choix valide pour le processeur
        choix_2 = Cpc.Choix()
        choix_2.choix_processeur.set("AMD Ryzen 9 5950X         ")
        choix_2.estimer()
        self.assertEqual(choix_2.lbl_message._text, "Tu dois choisir une carte graphique")
    def test_estimer_sans_RAM(self):
        # Cette fois-ci donnez un choix valide pour le processeur et pour la carte graphique
        choix_3 = Cpc.Choix()
        choix_3.choix_processeur.set("Intel Core i9 12900 K     ")
        choix_3.choix_carte_graphique.set("GeForce RTX 3080Ti        ")
        choix_3.estimer()
        self.assertEqual(choix_3.lbl_message._text, "Tu dois choisir une barrette RAM")


    def test_estimer_les_3_choix(self):
        # Instanciez la classe Choix
        choix_4 = Cpc.Choix()
        # donner le choix de processeur "AMD Ryzen 9 5950X         "
        choix_4.choix_processeur.set("AMD Ryzen 9 5950X         ")
        # donner le choix de carte graphique "GeForce RTX 3090Ti        "
        choix_4.choix_carte_graphique.set("GeForce RTX 3090Ti        ")
        # donner le choix de barrette RAM  "G.SKILL Trident Z5        "
        choix_4.choix_RAM.set("G.SKILL Trident Z5        ")
        # appeler la méthode estimer()
        choix_4.estimer()
        # Vérifier que le texte du lbl_message est égal à "Pour tes choix, l'estimé est de 3720.26$."
        self.assertEqual(choix_4.lbl_message._text, "Pour tes choix, l'estimé est de 3720.26$.")
        
if __name__ == '__main__':
    unittest.main()