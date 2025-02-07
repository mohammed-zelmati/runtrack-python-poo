"""
Créez un jeu de combat en utilisant la POO.

À tour de rôle, votre personnage et l’ennemi attaquent. Le but étant de vaincre l’ennemi (vie à zéro).

Votre programme doit contenir au minimum deux classes, Personnage et Jeu.

Commencer par créer une classe nommée Personnage prenant des paramètres de construction : nom (string) et vie(int).
Créez au minimum une méthode attaquer qui enlève des points à son adversaire.

Ensuite créer la classe Jeu ne prenant pas de paramètre. Créer une méthode choisirNiveau qui permet 
de demander au joueur le niveau de difficulté. Celui-ci sera stocké dans l’attribut niveau.

En fonction du niveau choisi, le nombre de points de vie du joueur ainsi que de l'ennemi seront différents.
Créer lancerJeu, méthode qui utilise l’attribut niveau. Cette méthode aura pour but d’instancier 
deux objets Personnage, un qui représente le joueur et l’autre l'ennemi avec un nombre de points 
défini en fonction du niveau.

Implémenter le déroulement d’une partie en demandant au joueur le niveau de difficulté et pensez 
à ajouter une méthode qui vérifie la santé de vos personnages ainsi qu’une méthode permettant de vérifier qui a gagné.
"""

import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(10, 20)  # Dégâts aléatoires entre 10 et 20
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} points de dégâts!")

    def estEnVie(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        niveau = input("Choisissez un niveau de difficulté (facile, moyen, difficile) : ")
        niveaux = {'facile': 100, 'moyen': 75, 'difficile': 45}
        self.niveau = niveaux.get(niveau, 100)
        print(f"Vous avez choisi le niveau {niveau}. Le joueur et l'ennemi auront {self.niveau} points de vie.")

    def lancerJeu(self):
        self.choisirNiveau()
        joueur = Personnage("Joueur", self.niveau)
        ennemi = Personnage("Ennemi", self.niveau)
        tour = 0

        while joueur.estEnVie() and ennemi.estEnVie():
            tour += 1
            print(f"\n--- Tour {tour} ---")
            joueur.attaquer(ennemi)
            if ennemi.estEnVie():
                ennemi.attaquer(joueur)

            print(f"{joueur.nom} : {joueur.vie} points de vie")
            print(f"{ennemi.nom} : {ennemi.vie} points de vie")

        self.verifierGagnant(joueur, ennemi)

    def verifierGagnant(self, joueur, ennemi):
        if joueur.estEnVie():
            print("\nLe joueur a gagné !")
        else:
            print("\nL'ennemi a gagné !")

# Créer une instance du jeu et lancer le jeu
jeu = Jeu()
jeu.lancerJeu()
