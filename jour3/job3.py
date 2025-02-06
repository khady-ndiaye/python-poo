class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "À faire"

    def marquerCommeFinie(self):
        self.statut = "Terminée"

    def __str__(self):
        return f"- {self.titre} : {self.description} [{self.statut}]"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [tache for tache in self.taches if tache.titre != titre]

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.marquerCommeFinie()

    def afficherListe(self):
        print("\nListe des tâches :")
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]



# Création de tâches
tache1 = Tache("Acheter du pain", "Aller à la boulangerie avant 18h")
tache2 = Tache("Faire du sport", "Séance de 30 min de cardio")
tache3 = Tache("Lire un livre", "Lire 20 pages de mon roman")

# Création de la liste de tâches
listeTaches = ListeDeTaches()

# Ajout des tâches
listeTaches.ajouterTache(tache1)
listeTaches.ajouterTache(tache2)
listeTaches.ajouterTache(tache3)

# Marquer une tâche comme terminée
listeTaches.marquerCommeFinie("Faire du sport")

# Suppression d'une tâche
listeTaches.supprimerTache("Acheter du pain")

# Affichage de toutes les tâches
listeTaches.afficherListe()

# Affichage des tâches à faire
print("\nTâches à faire :")
for tache in listeTaches.filterListe("À faire"):
    print(tache)
