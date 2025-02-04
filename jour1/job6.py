class Animal:
    def __init__(self):
        self.age = 0
        self.prenom= ""
        
    def viellir(self):
        self.age+=1  
        
    def nommer(self, nom_animal) :
        print("votre animal se nomme",nom_animal)     
        
animal =Animal() 
print("Age de l'animal est:", animal.age)
animal.viellir()
print("Age apres viellissement:",animal.age )
animal.nommer("milkshake")