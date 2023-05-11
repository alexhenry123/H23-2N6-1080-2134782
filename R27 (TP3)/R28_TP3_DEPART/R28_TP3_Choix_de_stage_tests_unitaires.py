import R28_TP3_Choix_de_stages_DEPART as Cs
import unittest



class Test_enregistrer_choix(unittest.TestCase ):
    # Les méthodes setUpClass et tearDownClass sont appeler automatiquement au début et à la fin de chaque test.
    # vous pouvez appeler l'instance _unChoix à partir de chaque méthode test en utilisant self._unChoix
    @classmethod
    def setUpClass(cls):
        cls._unChoix = Cs.Choix()
    @classmethod
    def tearDownClass(cls):
        cls._unChoix.destroy()
                            
    def test_enregistrer_choix_pas_de_choix_1(self):
        # Tester ce qui ce passe lorsqu'il n'y a pas de choix effectuer
        self._unChoix.choix_1.set(value='PREMIER CHOIX')
        
        
        # Appeler la méthode enregistrer_choix() de _unChoix
        # Vérifier que la valeur lbl_message est bien "Tu dois faire 3 choix."
        pass

    def test_enregistrer_choix_pas_de_choix_2(self):
        # Effectuer le même test que le test précédant.
        # Cette fois-ci vérifier que le message est le bon lorsque
        # self._unChoix.choix_2 a comme valeur 'DEUXIÈME CHOIX'
        pass

    def test_enregistrer_choix_pas_de_matricule(self):
        # Donner des bonne valeurs aux menus à option choix_1, choix_2, et choix_3
        # puis appeler la méthode enregistrer_choix()
        # le lbl_message devrait contenir un texte "Tu dois entrer ton matricule."
        pass

    def test_enregistrer_choix_2_choix_pareils_cas1(self):
        # Donner la même valeur aux menus à option choix_1 et choix_2
        # donner une valeur différente au menu à option choix_3
        # donner une valeur au matricule
        # appeler la méthode enregistrer_choix()
        # le lbl_message devrait contenir un texte "Tu dois faire 3 choix."
        pass

    def test_enregistrer_choix_2_choix_pareils_cas2(self):
        # effectuer le même test que le précédant mais avec les menu choix_1 et choix_3 ayant les mêmes valeurs
        pass

    def test_enregistrer_choix_2_choix_pareils_cas3(self):
        # effectuer le même test que le précédant mais avec les menu choix_2 et choix_3 ayant les mêmes valeurs
        pass
    
    def test_enregistrer_choix_message_OK(self):
        # Donner des valeurs valides à tous les choix et au matricule.
        # appeler la méthode enregirster_choix()
        # vérifier le message dans lbl_message.
        pass
    
    #EXTRA +1% :
    #Vérifier la création du fichier choix.txt ainsi que son contenue.
    def Extra():
        pass


# Puisque l'interface qu'on utilise inclus des les éléments graphiques, 
# il faut s'assurer de supprimer les instances crée à chaque test.
# Pour cela, on crée deux méthodes ; setUpClass et TearDownClass.
# Ces méthodes seront appelé avant et après chaque test afin d'avoir une nouvelle instance et de ne pas utiliser toutes les ressources de l'ordinateur.
def suite():
    # VOUS N'AVEZ RIEN À CHANGER ICI
    suite = unittest.TestSuite()
    suite.addTest(Test_enregistrer_choix('test_enregistrer_choix_pas_de_choix_1'))
    suite.addTest(Test_enregistrer_choix('test_enregistrer_choix_pas_de_choix_2'))
    suite.addTest(Test_enregistrer_choix('test_enregistrer_choix_pas_de_matricule'))
    suite.addTest(Test_enregistrer_choix('test_enregistrer_choix_2_choix_pareils_cas1'))
    suite.addTest(Test_enregistrer_choix('test_enregistrer_choix_2_choix_pareils_cas2'))
    suite.addTest(Test_enregistrer_choix('test_enregistrer_choix_2_choix_pareils_cas3'))
    suite.addTest(Test_enregistrer_choix('test_enregistrer_choix_message_OK'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
        
