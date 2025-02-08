# Définition de la classe Personne
class Personne:
    def __init__(self, age=14):
        self.age = age  # Age par défaut à 14

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age  

# Définition de la classe Eleve qui hérite de Personne
class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"Je suis un élève et j’ai {self.age} ans")

# Définition de la classe Professeur
class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee  # Attribut privé

    def enseigner(self):
        print("Le cours va commencer")


personne1 = Personne()
eleve1 = Eleve()
eleve1.afficherAge()  # ➝ "J’ai 14 ans"
