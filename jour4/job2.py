from job1 import Personne
from job1 import Eleve

class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):
        super().__init__(age)  
        self.__matiereEnseignee = matiereEnseignee  

    def enseigner(self):
        print("Le cours va commencer")
        
eleve1 = Eleve()
eleve1.bonjour()  
eleve1.allerEnCours()  

# Modifier l'âge de l'élève à 15 ans
eleve1.modifierAge(15)
eleve1.afficherAge()  

# Création d'un professeur (40 ans, enseigne les mathématiques)
professeur1 = Professeur(40, "Mathématiques")
professeur1.bonjour()  
professeur1.enseigner()  