import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon  

    def changerRayon(self, new_rayon):
    
        self.rayon = new_rayon
    
    # Affiche les informations du cercle
    def afficherInfos(self):
        print(f"Rayon : {self.rayon}")
        print(f"Diamètre : {self.diametre()}")
        print(f"Circonférence : {self.circonference()}")
        print(f"Aire : {self.aire()}")
    
    # Calcule et retourne l'aire du cercle
    def circonference(self):
        return 2 * math.pi * self.rayon
    
    # Calcule et retourne l'aire du cercle
    def aire(self):
        return math.pi * self.rayon ** 2
    # Calcule et retourne le diamètre du cercle
    def diametre(self):
        return 2 * self.rayon

# Création d'instances
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Affichage des informations des cercles
cercle1.afficherInfos()
cercle2.afficherInfos()
