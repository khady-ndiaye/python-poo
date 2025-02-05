class Livre:
    
    def __init__(self, titre, auteur, pages):
        self.__titre = titre  
        self.__auteur = auteur 
        self.__pages = pages  

    # Accesseur pour le titre
    def get_titre(self):
        return self.__titre

    # Accesseur pour l'auteur
    def get_auteur(self):
        return self.__auteur

    # Accesseur pour le nombre de pages
    def get_pages(self):
        return self.__pages

    # Mutateur pour le titre
    def set_titre(self, titre):
        self.__titre = titre

    # Mutateur pour l'auteur
    def set_auteur(self, auteur):
        self.__auteur = auteur

    # Mutateur pour le nombre de pages
    def set_pages(self, pages):
        if isinstance(pages, int) and pages > 0:  # Vérification si pages est un entier positif
            self.__pages = pages
        else:
            print("Erreur : le nombre de pages doit être un nombre entier positif.")

    # Méthode pour afficher les informations du livre
    def afficher(self):
        print(f"Titre: {self.__titre}, Auteur: {self.__auteur}, Nombre de pages: {self.__pages}")


# Création d'un livre avec un titre, un auteur et un nombre de pages
livre = Livre("La semaine de 4 heure", "Timothé Ferries", 96)

# Affichage des informations du livre
print("Informations initiales du livre :")
livre.afficher()

# Test valeur negative
livre.set_pages(-16)  # Cela ne changera pas la valeur

# Test entier positif
livre.set_pages(150)

# Affichage après modification
print("\nInformations après modification :")
livre.afficher()
