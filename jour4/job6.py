# Définition de la classe Vehicule
class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    # Méthode d'affichage des informations du véhicule
    def informationsVehicule(self):
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modele}")
        print(f"Année : {self.annee}")
        print(f"Prix : {self.prix}€")

    # Méthode pour démarrer le véhicule
    def demarrer(self):
        print("Attention, je roule.")

# Définition de la classe Voiture qui hérite de Vehicule
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)  
        self.portes = 4  # Nombre de portes fixé à 4

    # Surcharge de la méthode informationsVehicule
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes : {self.portes}")

    # Surcharge de la méthode demarrer
    def demarrer(self):
        print(f"La {self.marque} {self.modele} démarre... Vroum vroum !")

# Définition de la classe Moto qui hérite de Vehicule
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2  # Nombre de roues fixé à 2

    # Surcharge de la méthode informationsVehicule
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues : {self.roues}")

    # Surcharge de la méthode demarrer
    def demarrer(self):
        print(f"La moto {self.marque} {self.modele} démarre... Brrm Brrm !")


#  Instanciation d'une Voiture
voiture = Voiture("Tesla", "Model S", 2023, 79999)
print("🚗 Informations de la voiture :")
voiture.informationsVehicule()
voiture.demarrer()

print("\n")

#  Instanciation d'une Moto
moto = Moto("Yamaha", "R1", 2022, 25000)
print(" Informations de la moto :")
moto.informationsVehicule()
moto.demarrer()
