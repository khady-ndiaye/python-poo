# Définition de la classe Rectangle
class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  
        self.__largeur = largeur    

    # Assesseurs 
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs 
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    # Méthode pour calculer le périmètre
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    # Méthode pour calculer la surface
    def surface(self):
        return self.__longueur * self.__largeur

# Définition de la classe Parallelepipede qui hérite de Rectangle
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)  
        self.__hauteur = hauteur  # Nouvel attribut hauteur

    # Assesseur et mutateur pour la hauteur
    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    # Méthode pour calculer le volume
    def volume(self):
        return self.surface() * self.__hauteur


#  Instanciation d'un Rectangle
rect = Rectangle(10, 5)
print(f"Périmètre du rectangle : {rect.perimetre()}")
print(f"Surface du rectangle : {rect.surface()}") 

#  Instanciation d'un Parallelepipede
para = Parallelepipede(10, 5, 8)
print(f"Volume du parallélépipède : {para.volume()}") 
