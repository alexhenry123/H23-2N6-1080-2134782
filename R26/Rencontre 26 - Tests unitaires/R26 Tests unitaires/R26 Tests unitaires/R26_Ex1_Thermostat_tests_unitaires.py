import R26_Ex1_Thermostat as Ths
import unittest
from constant import *

class Test_initialisation(unittest.TestCase):

    def test_temperature_initial(self):
        nouveau_thermostat = Ths.Thermostat()
        self.assertEqual(nouveau_thermostat._temperature, TEMPERATURE_INITIALE)

    def test_initialisation_temperature_trop_elevee(self):
        with self.assertRaises(expected_exception=ValueError):
            nouveau_thermostat = Ths.Thermostat.from_temperature(MAX_TEMPERATURE+4)

    def test_initialisation_temperature_trop_basse(self):
        with self.assertRaises(expected_exception=ValueError):
            nouveau_thermostat = Ths.Thermostat.from_temperature(MIN_TEMPERATURE-2)

    def test_initialisation_bonne_temperature(self):
        temp_eval = (MIN_TEMPERATURE + MAX_TEMPERATURE) / 2
        nouveau_thermostat = Ths.Thermostat.from_temperature(22)
        self.assertEqual(temp_eval, nouveau_thermostat.temperature)

@unittest.skip
class test_modification_de_temperature(unittest.TestCase):

    def test_changer_temperature_trop_elevee(self,nouvelle_temperature):
        nvxthermostat = Ths.Thermostat()
        nouvelle_temperature = MAX_TEMPERATURE * 2
        with self.assertRaises(ValueError):
            nvxthermostat.temperature == nouvelle_temperature
        #self.fail("À faire")
       
    def test_changer_temperature_trop_basse(self):
       self.fail("À faire")
       
    def test_changer_temperature_valide(self):
       self.fail("À faire")
     
    def test_augmenter_1_degre_OK(self):
       self.fail("À faire")
   
    def test_diminuer_1_degre_OK(self):
       self.fail("À faire")


if __name__ == '__main__':
    unittest.main(verbosity=2)