class Personne:
    """ ceci est une classe de personne """
    compteur = 0
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        Personne.compteur += 1
        self._adresse = "Paris"

    def objetsCree(cls):
        print("il y a eu {} objet Personne crée".format(Personne.compteur))
    objetsCree = classmethod(objetsCree)

    def staticMethod():
        print("I'm static method")
    staticMethod = staticmethod(staticMethod)

    def _getAdress(self):
        print("someone asked for the adress")
        return self._adresse

    def _setAdress(self,newAdress):
        print("notre utilisateur déménage !")
        self._adresse = newAdress

    adresse = property(_getAdress,_setAdress)
    

Personne.objetsCree()
ayoub = Personne("ayoub", 30)
Personne.objetsCree()
ayoub.staticMethod()
#########TEST properties
print(ayoub.adresse)
ayoub.adresse = "Geneve"
##############
#############
class Duree:
    def __init__(self, minutes, secondes):
        self.minutes = minutes
        self.seconds = secondes
    def __str__(self):
        return "il est {0:02}:{1:02}".format(self.minutes,self.seconds)

    def __add__(self, secondes):
        current_s = self.seconds
        current_m = self.minutes
        current_s += secondes
        if(current_s >= 60):
            current_m += current_s // 60
            current_s = current_s % 60
        return Duree(current_m, current_s)

    def __radd__(self, secondes):
        return self + secondes

dure1 = Duree(1,20)
print(dure1)
print(dure1 + 3660)
print(2 + dure1)

####################