#Vous avez une classe Cercle qui a un attribut privé rayon (_rayon)
class Cercle:
    def __init__(self, rayon):
        self._rayon = rayon
    @property
    def rayon(self):
        print("Get rayon")
        return self._rayon
    @rayon.setter
    def rayon(self):
        print("Set rayon")
        return self._rayon
    @rayon.deleter
    def rayon(self):
        del self._rayon
        print("Delete rayon")
    
#Instanciations et tests
cercle1 = Cercle(45)
#print(cercle1.rayon)
cercle1._rayon = 50
del cercle1.rayon
print(cercle1.rayon)