#création de la classe point:
class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def affichepoint(self):
        print("les coordonnées du pointf sont:", self.x, self.y)
    #  methode pour afficher x     
    def afficherX(self):
        print("x egal", self.x)
    #méthode pour afficher y    
    def afficherY(self):
        print("y egal"), self.y  
    #méthode pour changer x    
    def changerX(self,new_x):
        self.x= new_x  
    #méthode pour changer y
    def changerY(self, new_y):
        self.y = new_y    