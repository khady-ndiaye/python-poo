# création de la classe opération
 
class Operation:
     def __init__(self, nombre1=0, nombre2=1):#construcyeur initialiser avec de valeurs par defaut
         self.nombre1 = nombre1
         self.nombre2 = nombre2


#création d'une instance de la classe( une fille)
operation = Operation()
print(operation)