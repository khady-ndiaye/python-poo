class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom  
        self.prixHT = prixHT  
        self.TVA = TVA  
    
    # Calcul du prix TTC
    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)
    
    # Affichage des informations du produit
    def afficher(self):
         return {
            "Nom": self.nom,
            "Prix HT": self.prixHT,
            "TVA": self.TVA,
            "Prix TTC": self.CalculerPrixTTC()
        }
    
    # Modifie le nom du produit
    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom
    
    # Modifie le prix HT du produit
    def modifierPrix(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT
    
    # Méthodes pour retourner chaque information du produit
    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

    def getPrixTTC(self):
        return self.CalculerPrixTTC( )   

# Création de plusieurs produits
produit1 = Produit("laptop", 2000, 20)
produit2 = Produit("Smartphone", 1500, 10)
produit3 = Produit("Tv", 600, 10)

# Affichage des informations de chaque produit
infos=produit1.afficher()
print("les information du produit1 sont:", infos)
infos=produit2.afficher()
print("les information du produit2 sont:", infos)
infos=produit3.afficher()
print(infos)


# Modification du nom et du prix du produit1
nouveau_nom=produit1.modifierNom("Ordinateur Portable")
nouveau_nom=produit1.modifierPrix(850)

# Affichage des nouvelles informations du produit1 après modification
new_infos=produit1.afficher()
print("informations mis à jour:", new_infos)

         