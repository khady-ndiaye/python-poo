from Ship import*
def main():
    print("Bienvenue dans le paradoxe du navire de Thésée !")
    
    # Choix du type de bateau
    ship_type = input("Voulez-vous un bateau normal (N) ou un bateau de course (C) ? ").strip().upper()
    if ship_type == "C":
        max_speed = int(input("Entrez la vitesse maximale du bateau de course : "))
        ship = RacingShip("Thésée", max_speed)
    else:
        ship = Ship("Thésée")

    while True:
        print("\nOptions :")
        print("1. Afficher l'état du bateau")
        print("2. Remplacer une pièce")
        print("3. Modifier le matériau d'une pièce")
        print("4. Afficher l'historique des modifications")
        print("5. Quitter")
        
        if isinstance(ship, RacingShip):
            print("6. Afficher la vitesse du bateau de course")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            ship.display_state()

        elif choix == "2":
            part_name = input("Nom de la pièce à remplacer (Mât, Coque, Voile) : ")
            new_material = input("Nouveau matériau : ")
            new_part = Part(part_name, new_material)
            ship.replace_part(part_name, new_part)

        elif choix == "3":
            part_name = input("Nom de la pièce à modifier (Mât, Coque, Voile) : ")
            new_material = input("Nouveau matériau : ")
            ship.change_part(part_name, new_material)

        elif choix == "4":
            ship.show_history()

        elif choix == "5":
            print("Merci d'avoir exploré le paradoxe du navire de Thésée !")
            break
        
        elif choix == "6" and isinstance(ship, RacingShip):
            ship.display_speed()

        else:
            print("Option invalide, essayez à nouveau.")

# Exécution du programme
if __name__ == "__main__":
    main()
