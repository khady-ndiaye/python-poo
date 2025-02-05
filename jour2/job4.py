class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom  
        self.__prenom = prenom 
        self.__numero_etudiant = numero_etudiant 
        self.__credits = 0  #initialisé à 0
        self.__level = self.__student_eval()  

    # Méthode pour ajouter des crédits
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits  
            # Mise à jour du niveau après ajout des crédits
            self.__level = self.__student_eval()
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")

    # Méthode privée pour évaluer le niveau de l'étudiant en fonction des crédits
    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    # Méthode publique pour afficher les informations de l'étudiant
    def student_info(self):
        print(f"Nom: {self.__nom}, Prénom: {self.__prenom}, Numéro d'étudiant: {self.__numero_etudiant}, Niveau: {self.__level}")

# Création de l'objet étudiant John Doe
etudiant = Student("Doe", "John", 145)

# Ajout de crédits
etudiant.add_credits(10)
etudiant.add_credits(10)
etudiant.add_credits(10)

# Affichage des informations de l'étudiant
etudiant.student_info()
