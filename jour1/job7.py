class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x  
        self.y = y  
    
    # Déplacer vers la gauche
    def gauche(self):
        self.x -= 1  
    
    # Déplacer vers la droit
    def droite(self):
        self.x += 1  
    
    # Déplacer vers le haut
    def haut(self):
        self.y -= 1  
    
    # Déplace le personnage vers le bas
    def bas(self):
        self.y += 1  
    
    #position actuelle du personnage
    def position(self):
        print(f"Position du personnage: ({self.x}, {self.y})")
        # Renvoie la position sous forme de tuple (x, y)
        return (self.x, self.y)

# Instanciation du personnage à la position (0, 0)
personnage = Personnage(0, 0)

#position initiale
personnage.position()

# Déplacer le personnage
personnage.droite()  
personnage.bas()     

#nouvelle position
personnage.position()
