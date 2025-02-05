# création d'upne classe avec des attributs privés
class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur= longueur    #attribut privé
        self.__largeur = largeur     #attribut privé
     
    # methode pour modifier les attributs privés

    #accesseur pour la longueur
    def get_longueur(self):
        return self.__longueur

    # Accesseur pour la largeur
    def get_largeur(self):
        return self.__largeur

    # Mutateur pour la longueur
    def set_longueur(self, longueur):
        if longueur > 0:  # On vérifie que la longueur est positive
            self.__longueur = longueur
        else:
            print("La longueur doit être positive.")

    # Mutateur pour la largeur
    def set_largeur(self, largeur):
        if largeur > 0:  # On vérifie que la largeur est positive
            self.__largeur = largeur
        else:
            print("La largeur doit être positive.")

    # Méthode pour afficher les dimensions du rectangle
    def afficher(self):
        print(f"Longueur: {self.__longueur}, Largeur: {self.__largeur}")


# Création d'un rectangle avec longueur 10 et largeur 5
rectangle = Rectangle(10, 5)

# Affichage des dimensions initiales
print("Dimensions initiales :")
rectangle.afficher()

# Modification de la longueur et de la largeur
rectangle.set_longueur(12)
rectangle.set_largeur(7)

# Affichage des nouvelles dimensions
print("\nDimensions après modification :")
rectangle.afficher()