class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque  
        self.__modele = modele  
        self.__annee = annee  
        self.__kilometrage = kilometrage  
        self.__en_marche = False  
        self.__reservoir = 50  

    # Accesseurs (getters)
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    # Mutateurs (setters)
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def set_reservoir(self, reservoir):
        if reservoir >= 0:
            self.__reservoir = reservoir
        else:
            print("Erreur : le réservoir ne peut pas être négatif.")

    # Méthode privée pour vérifier le plein de carburant
    def __verifier_plein(self):
        return self.__reservoir

    # Méthode pour démarrer la voiture
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print(f"La voiture {self.__marque} {self.__modele} a démarré.")
        else:
            print(f"La voiture {self.__marque} {self.__modele} ne peut pas démarrer, réservoir insuffisant.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        self.__en_marche = False
        print(f"La voiture {self.__marque} {self.__modele} est arrêtée.")

    # Méthode pour afficher l'état actuel de la voiture
    def afficher_etat(self):
        statut = "en marche" if self.__en_marche else "arrêtée"
        print(f"Voiture {self.__marque} {self.__modele} ({self.__annee}), Kilométrage: {self.__kilometrage} km, "
              f"Réservoir: {self.__reservoir} L, Statut: {statut}")

# Création de la voiture
voiture = Voiture("Toyota", "chr", 2022, 15000)
voiture.afficher_etat()
voiture.demarrer()
voiture.set_reservoir(3)
voiture.demarrer()

# Arrêter la voiture
voiture.arreter()

# Affichage de l'état après arrêt
voiture.afficher_etat()
