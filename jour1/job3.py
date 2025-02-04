class Operation:
     def __init__(self, nombre1, nombre2):
         self.nombre1 = nombre1
         self.nombre2 = nombre2
    #definition de la méthode addition
     def addition(self):  
      resultat= self.nombre1 + self.nombre2 
      print("le resultat de l'addition du nombre1 et du nombre2 est egale à", resultat) 


#création d'une instance de la classe( une fille)
operation = Operation(4,5)
#on appelle la méthode pour afficher le resultat
operation.addition()