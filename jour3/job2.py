class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte N°{self.__numero} - Titulaire: {self.__prenom} {self.__nom} - Solde: {self.__solde}€")

    def afficherSolde(self):
        print(f"Solde actuel: {self.__solde}€")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant}€ effectué sur le compte N°{self.__numero}. Nouveau solde: {self.__solde}€")

    def retrait(self, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Fonds insuffisants pour effectuer ce retrait.")
        else:
            self.__solde -= montant
            print(f"Retrait de {montant}€ effectué effectué sur le compte N°{self.__numero}. Nouveau solde: {self.__solde}€")
    
    def agios(self):
        if self.__solde < 0:
            self.__solde *= 1.1  # Applique 10% d'agios
            print(f"Des agios ont été appliquéseffectué sur le compte N°{self.__numero}. Nouveau solde: {self.__solde}€")
    
    def virement(self, compte_destinataire, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Virement refusé : fonds insuffisants.")
        else:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant}€ effectué vers le compte N°{compte_destinataire.__numero}.")

# Création des comptes
compte1 = CompteBancaire(12345, "Doe", "John", 1000)
compte2 = CompteBancaire(67890, "Smith", "Jane", -200, decouvert=True)

# Affichage des comptes
compte1.afficher()
compte2.afficher()

# Vérification des fonctionnalités
compte1.versement(500)
compte1.retrait(300)
compte2.agios()
compte1.virement(compte2, 200)
