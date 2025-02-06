class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        return (f"{self.nom} (#{self.numero}, {self.position}) - "
                f"Buts: {self.buts}, Passes: {self.passes}, "
                f"Jaunes: {self.cartons_jaunes}, Rouges: {self.cartons_rouges}")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"\nStatistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            print(joueur.afficherStatistiques())

    def mettreAJourStatistiquesJoueur(self, nom, action):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()
                return f"Action '{action}' effectuée pour {nom}."
        return "Joueur non trouvé."


# --- Test du programme ---
# Création des équipes
equipe1 = Equipe("Paris ")
equipe2 = Equipe("Marseille ")

# Création des joueurs
joueur1 = Joueur("Mbappé", 7, "Attaquant")
joueur2 = Joueur("Messi", 10, "Milieu")
joueur3 = Joueur("Ramos", 4, "Défenseur")

joueur4 = Joueur("Payet", 11, "Attaquant")
joueur5 = Joueur("Guendouzi", 6, "Milieu")
joueur6 = Joueur("Saliba", 2, "Défenseur")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe1.ajouterJoueur(joueur3)

equipe2.ajouterJoueur(joueur4)
equipe2.ajouterJoueur(joueur5)
equipe2.ajouterJoueur(joueur6)

# Simulation d'un match
equipe1.mettreAJourStatistiquesJoueur("Mbappé", "but")
equipe1.mettreAJourStatistiquesJoueur("Messi", "passe")
equipe2.mettreAJourStatistiquesJoueur("Payet", "but")
equipe2.mettreAJourStatistiquesJoueur("Guendouzi", "passe")
equipe1.mettreAJourStatistiquesJoueur("Ramos", "jaune")
equipe2.mettreAJourStatistiquesJoueur("Saliba", "rouge")

# Affichage des statistiques après le match
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
