from abc import ABC, abstractmethod


class liste_produits():
    def __init__():
#        ls = __req_api()
        pass
    def mettre_a_jour():
        pass
    
class Employe(ABC):
    def __init__(self) -> None:
        super().__init__()
    @abstractmethod
    def calcul_paie(self):
        pass

class Programmer(Employe):
    def __init__(self) -> None:
        super().__init__()
    def calcul_paie(self):
        return 32

emp1 = Programmer()
print(emp1.calcul_paie())