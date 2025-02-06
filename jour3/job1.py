class Ville:
    def __init__(self, nom, population):
        self.__nom = nom
        self.__population = population

    def get_population(self):
        return self.__population

    def get_nom(self):
        return self.__nom


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()

    def ajouterPopulation(self):
        self.__ville._Ville__population += 1


# Création des villes
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage des populations initiales
print(f"Population de {paris.get_nom()} : {paris.get_population()}")
print(f"Population de {marseille.get_nom()} : {marseille.get_population()}")

# Création des personnes
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Affichage des populations après l'arrivée des personnes
print(f"mise à jour de la population {paris.get_nom()}  : {paris.get_population()} habitants")
print(f"mise à joueur de la population {marseille.get_nom()}  : {marseille.get_population()} habitants")
    
                