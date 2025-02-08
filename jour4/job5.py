import math  

class Forme:
    def aire(self):
        return 0  # Par défaut

# Définition de la classe Rectangle qui hérite de Forme
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    # Surcharge de la méthode aire pour calculer l'aire du rectangle
    def aire(self):
        return self.largeur * self.hauteur

# Définition de la classe Cercle qui hérite de Forme
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    # Surcharge de la méthode aire pour calculer l'aire du cercle
    def aire(self):
        return math.pi * (self.radius ** 2)


#  Instanciation d'un Rectangle
rect = Rectangle(10, 5)
print(f"Aire du rectangle : {rect.aire()}")  

#  Instanciation d'un Cercle
cercle = Cercle(5)
print(f"Aire du cercle : {cercle.aire():.2f}")  #arrondi
