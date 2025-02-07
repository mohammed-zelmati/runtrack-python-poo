"""
Développer votre version du célèbre jeu Blackjack. Le but est de faire le plus de points sans dépasser 21. 
Chaque carte représente une valeur : - de 2 à 10 : ces cartes ont pour valeur sa valeur nominale
                                     - une figure a pour valeur 10 points
                                     - un as 1 ou 11 points au choix

Le jeu commence avec les joueurs qui reçoivent chacun 2 cartes. Ensuite, le joueur peut choisir de "prendre" (recevoir) 
une ou plusieurs cartes supplémentaires pour tenter d'améliorer sa main, ou de "passer" et laisser le tour au croupier. 
Le croupier prend des cartes jusqu'à ce qu'il ait au moins 17 points, puis s'arrête. Si la main du joueur dépasse 21, 
il perd immédiatement. Si le total de la main du joueur est supérieur à celui du croupier, le joueur
gagne. Sinon, c'est le croupier qui gagne.

Créer au minimum deux classes Carte et Jeu.

La classe Carte aura au minimum un attribut valeur et couleur. La classe Jeu quant à elle devra gérer l’ensemble des cartes. 
Les cartes du jeu seront stockées dans un attribut paquet représenté par une liste et contenant 52 cartes.
Créer toutes les méthodes nécessaires pour jouer une partie.
"""
import random

# Classe Carte
class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

# Classe Jeu
class Jeu:
    # Valeurs et couleurs des cartes
    VALEURS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
    COULEURS = ["Cœur", "Carreau", "Pique", "Trèfle"]

    def __init__(self):
        # Création du paquet de 52 cartes
        self.paquet = [Carte(valeur, couleur) for valeur in self.VALEURS for couleur in self.COULEURS]
        random.shuffle(self.paquet)  # Mélanger le paquet

    # Méthode pour tirer une carte du paquet
    def tirer_carte(self):
        return self.paquet.pop()

    # Méthode pour calculer la valeur d'une main
    def calculer_valeur_main(self, main):
        valeur = 0
        as_count = 0  # Compter le nombre d'As dans la main

        for carte in main:
            if carte.valeur in ["Valet", "Dame", "Roi"]:
                valeur += 10
            elif carte.valeur == "As":
                valeur += 11
                as_count += 1
            else:
                valeur += int(carte.valeur)

        # Ajuster la valeur si la main dépasse 21 et qu'il y a des As
        while valeur > 21 and as_count:
            valeur -= 10
            as_count -= 1

        return valeur

    # Méthode pour afficher une main
    def afficher_main(self, main, masquer_premiere_carte=False):
        if masquer_premiere_carte:
            print("Carte cachée")
            for carte in main[1:]:
                print(carte)
        else:
            for carte in main:
                print(carte)
        print(f"Valeur totale : {self.calculer_valeur_main(main)}\n")

    # Méthode pour jouer une partie
    def jouer(self):
        print("=== Bienvenue au Blackjack ! ===")

        # Initialisation des mains du joueur et du croupier
        main_joueur = [self.tirer_carte(), self.tirer_carte()]
        main_croupier = [self.tirer_carte(), self.tirer_carte()]

        # Afficher les mains
        print("\nMain du joueur :")
        self.afficher_main(main_joueur)

        print("Main du croupier :")
        self.afficher_main(main_croupier, masquer_premiere_carte=True)

        # Tour du joueur
        while True:
            choix = input("Voulez-vous prendre une carte ? (o/n) : ").strip().lower()
            if choix == "o":
                main_joueur.append(self.tirer_carte())
                print("\nMain du joueur :")
                self.afficher_main(main_joueur)

                # Vérifier si le joueur a dépassé 21
                if self.calculer_valeur_main(main_joueur) > 21:
                    print("Vous avez dépassé 21. Vous avez perdu !")
                    return
            elif choix == "n":
                break
            else:
                print("Choix invalide. Veuillez répondre par 'o' ou 'n'.")

        # Tour du croupier
        print("\nTour du croupier :")
        self.afficher_main(main_croupier)

        while self.calculer_valeur_main(main_croupier) < 17:
            main_croupier.append(self.tirer_carte())
            print("Le croupier prend une carte.")
            self.afficher_main(main_croupier)

        # Déterminer le gagnant
        valeur_joueur = self.calculer_valeur_main(main_joueur)
        valeur_croupier = self.calculer_valeur_main(main_croupier)

        print("\n=== Résultat ===")
        print(f"Votre main : {valeur_joueur} points")
        print(f"Main du croupier : {valeur_croupier} points")

        if valeur_joueur > 21:
            print("Vous avez dépassé 21. Vous avez perdu !")
        elif valeur_croupier > 21:
            print("Le croupier a dépassé 21. Vous avez gagné !")
        elif valeur_joueur > valeur_croupier:
            print("Vous avez gagné !")
        elif valeur_joueur < valeur_croupier:
            print("Le croupier a gagné !")
        else:
            print("Égalité !")



# Créer une instance du jeu et jouer une partie
jeu = Jeu()
jeu.jouer()        