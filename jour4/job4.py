# Définition de la classe Forme
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

# Instanciation d'un Rectangle
rect = Rectangle(10, 5)

# Affichage de l'aire du rectangle
print(f"Aire du rectangle : {rect.aire()}")  
