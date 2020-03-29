class Personne:
    """ ceci est une classe de personne """
    compteur = 0
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        Personne.compteur += 1
    def objetsCree(cls):
        print("il y a eu {} objet Personne crée".format(Personne.compteur))
    objetsCree = classmethod(objetsCree)

    def staticMethod():
        print("I'm static method")
    staticMethod = staticmethod(staticMethod)

Personne.objetsCree()
ayoub = Personne("ayoub", 30)
Personne.objetsCree()
ayoub.staticMethod()

