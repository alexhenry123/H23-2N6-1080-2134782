from operator import ge
import R26_Ex2_Groupes_etudiants as Ge
import unittest
from constant import *

class Test_ajouter_etudiant(unittest.TestCase):

    def test_ajouter_1_etudiant_depasse_max(self):
        # Instanciez 3 étudiants
        marcel = Ge.Etudiant("2223334","Marcel","16")
        jean = Ge.Etudiant("3478214","Jean","14")
        juan = Ge.Etudiant("2224442","Juan","15")
        # Instanciez un groupe avec une liste de 3 etudiants
        grp1_ls_etudiants = [marcel,jean,juan]
        groupe_1 = Ge.Groupe(grp1_ls_etudiants) 
        # Instanciez un autre étudiant
        autre_etudiant = Ge.Etudiant("2341563","Autre Étudiant","70")
        # Vérifiez que vous obtenez une erreur quand vous testez l'ajout de cet autre étudiant
        with self.assertRaises(ValueError):
            self.assertFalse(groupe_1.ajouter_etudiant(autre_etudiant))       

    def test_ajouter_1_etudiant_ok(self):
        # Instanciez un etudiant
        pablo = Ge.Etudiant("1234567","Pablo","42")
        # Instanciez un groupe avec cet etudiant
        grp2_ls_etudiants = [pablo]
        groupe_2 = Ge.Groupe(grp2_ls_etudiants)
        # Instanciez un autre étudiant
        marco = Ge.Etudiant("7654321","Marco","23")
        # Testez l'ajout de cet autre étudiant
        groupe_2.ajouter_etudiant(marco)
        self.assertEqual(groupe_2.ls_etudiants[len(groupe_2.ls_etudiants)-1], marco)
        # Vérifiez que le dernier étudiant du groupe est celui que vous avez ajouté
        self.assertTrue(groupe_2.ls_etudiants[len(groupe_2.ls_etudiants)-1] == marco)
        # Vérifiez que le nombre d'étudiants du groupe est maintenant de 2
        self.assertTrue(len(groupe_2.ls_etudiants) == 2)



if __name__ == '__main__':
    unittest.main(verbosity=2)