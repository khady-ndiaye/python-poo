from Part import *

class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {
            "mât": Part("mât", "bois"),
            "coque": Part("coque", "acier"),
            "voile": Part("voile", "coton")
        }
        self.history = []  # Liste pour suivre les modifications
    
    #Affiche l'état actuel du bateau
    def display_state(self):
        print(f"\nÉtat du bateau '{self.name}':")
        for part in self.__parts.values():
            print("-", part)
    #Remplace une pièce par une nouvelle
    def replace_part(self, part_name, new_part):
        
        if part_name in self.__parts:
            old_part = self.__parts[part_name]
            print(f"\nAvant remplacement: ID de {part_name} = {id(self.__parts[part_name])}")
            self.__parts[part_name] = new_part
            self.history.append(f"Remplacement de {old_part} par {new_part}")
            print(f"→ {old_part} a été remplacé par {new_part}.")
            print(f"Après remplacement: ID de {part_name} = {id(self.__parts[part_name])}")
        else:
            print("Cette pièce n'existe pas.")
    #Modifie le matériau d'une pièce
    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            print(f"\nAvant Modification: ID de {part_name} = {id(self.__parts[part_name])}")
            old_material = self.__parts[part_name].material
            self.__parts[part_name].change_material(new_material)
            self.history.append(f"Modification de {part_name} ({old_material} → {new_material})")
            print(f"→ Le matériau de {part_name} a été changé en {new_material}.")
            print(f"Après Modification: ID de {part_name} = {id(self.__parts[part_name])}")
        else:
            print("Cette pièce n'existe pas.")
    #Affiche l'historique des modifications
    def show_history(self):
        print("\n Historique des modifications :")
        for entry in self.history:
            print("-", entry)


class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed
    
    #Affiche la vitesse maximale du bateau de course
    def display_speed(self):
        print(f"🚤 Vitesse maximale de {self.name} : {self.max_speed} nœuds.")
