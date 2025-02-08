import random

# Classe représentant une carte (valeur + couleur)
class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur  # Pique, Cœur, Carreau, Trèfle

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

    # Calcul de la valeur d'une carte selon les règles du Blackjack
    def get_valeur(self):
        if self.valeur in ["Valet", "Dame", "Roi"]:
            return 10  
        elif self.valeur == "As":
            return 11  
        else:
            return int(self.valeur)  # Cartes numérotées gardent leur valeur

# Classe gérant le jeu de Blackjack
class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()
        random.shuffle(self.paquet) 

    # Création du paquet de 52 cartes
    def creer_paquet(self):
        valeurs = [str(i) for i in range(2, 11)] + ["Valet", "Dame", "Roi", "As"]
        couleurs = ["Pique", "Cœur", "Carreau", "Trèfle"]
        return [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]

    # Distribution d'une carte
    def tirer_carte(self):
        return self.paquet.pop() if self.paquet else None

# Fonction principale pour jouer au Blackjack
def blackjack():
    jeu = Jeu()

    # Main du joueur et du croupier
    joueur_main = [jeu.tirer_carte(), jeu.tirer_carte()]
    croupier_main = [jeu.tirer_carte(), jeu.tirer_carte()]

    # Affichage des mains initiales
    print("\nVotre main :", [str(c) for c in joueur_main])
    print("Carte visible du croupier :", str(croupier_main[0]))

    # Fonction pour calculer la valeur d'une main
    def calculer_valeur(main):
        total = sum(c.get_valeur() for c in main)
        as_count = sum(1 for c in main if c.valeur == "As")
        while total > 21 and as_count:
            total -= 10  # Transformer un As de 11 en 1 pour éviter le dépassement
            as_count -= 1
        return total

    # Tour du joueur
    while calculer_valeur(joueur_main) < 21:
        choix = input("\nVoulez-vous prendre une carte (tapez 'O') ou passer (tapez 'P') ? ").lower()
        if choix == "p":
            joueur_main.append(jeu.tirer_carte())
            print("Nouvelle main :", [str(c) for c in joueur_main])
        else:
            break

    joueur_score = calculer_valeur(joueur_main)
    
    # Vérification si le joueur dépasse 21
    if joueur_score > 21:
        print("Vous avez dépassé 21 ! Vous perdez.")
        return

    # Tour du croupier
    print("\nLe croupier joue...")
    print("Main complète du croupier :", [str(c) for c in croupier_main])

    while calculer_valeur(croupier_main) < 17:
        croupier_main.append(jeu.tirer_carte())
        print("Nouvelle main du croupier :", [str(c) for c in croupier_main])

    croupier_score = calculer_valeur(croupier_main)

    # Résultat final
    print("\nScore final")
    print(f"Joueur : {joueur_score}")
    print(f"Croupier : {croupier_score}")

    if croupier_score > 21 or joueur_score > croupier_score:
        print("Bravo, vous gagnez !")
    elif joueur_score < croupier_score:
        print("Le croupier gagne...")
    else:
        print("Égalité !")

# Lancer le jeu
blackjack()
