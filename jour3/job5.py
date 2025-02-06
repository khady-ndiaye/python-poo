import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(10, 30)  # Dégâts aléatoires entre 10 et 30
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts !")
        if adversaire.vie < 0:
            adversaire.vie = 0

    def estVivant(self):
        return self.vie > 0

    def afficherVie(self):
        print(f"{self.nom} a {self.vie} points de vie.")


class Jeu:
    def __init__(self):
        self.niveau = None
        self.joueur = None
        self.ennemi = None

    def choisirNiveau(self):
        while True:
            print("\nChoisissez un niveau de difficulté :")
            print("1 - Facile (100 PV)")
            print("2 - Normal (70 PV)")
            print("3 - Difficile (50 PV)")
            choix = input("Votre choix : ")

            if choix == "1":
                self.niveau = "Facile"
                vie = 100
                break
            elif choix == "2":
                self.niveau = "Normal"
                vie = 70
                break
            elif choix == "3":
                self.niveau = "Difficile"
                vie = 50
                break
            else:
                print("Choix invalide, veuillez entrer 1, 2 ou 3.")

        self.joueur = Personnage("Héros", vie)
        self.ennemi = Personnage("Ennemi", vie)
        print(f"\nNiveau choisi : {self.niveau}. Le combat commence !")

    def tourDeCombat(self):
        while self.joueur.estVivant() and self.ennemi.estVivant():
            input("\nAppuyez sur Entrée pour attaquer !")
            self.joueur.attaquer(self.ennemi)
            self.ennemi.afficherVie()

            if not self.ennemi.estVivant():
                break  # L'ennemi est vaincu

            print("\nL'ennemi attaque !")
            self.ennemi.attaquer(self.joueur)
            self.joueur.afficherVie()

        self.verifierVainqueur()

    def verifierVainqueur(self):
        if self.joueur.estVivant():
            print("\n🎉 Félicitations ! Vous avez vaincu l'ennemi !")
        else:
            print("\n💀 Vous avez été vaincu... L'ennemi a gagné.")

    def lancerJeu(self):
        self.choisirNiveau()
        self.tourDeCombat()


# --- Lancement du jeu ---
jeu = Jeu()
jeu.lancerJeu()

