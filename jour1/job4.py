#classe personne

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
    def SePresenter(self):
        print("je suis", self.prenom, self.nom)   
        
#création des instance de la classe        
personne1 = Personne("ndiaye", "khady")
personne2 = Personne("doe", "john")  
#appel de la méthode seprésenter
personne1.SePresenter()
personne2.SePresenter()      
        