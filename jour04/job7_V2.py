import pygame
import random
import sys

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()  # Initialiser le module de mixage audio
# Constantes
LARGEUR, HAUTEUR = 1280, 720
COULEUR_FOND = (0, 128, 0)  # Vert foncé pour le tapis de jeu
COULEUR_TEXTE = (165, 42, 42) # Couleur MARRON pour le texte
TAILLE_CARTE = (80, 120)  # Largeur et hauteur d'une carte
FPS = 30

# Couleurs
WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)
YELLOW, ORANGE, PURPLE, BROWN, PINK = (255, 255, 0), (255, 165, 0), (128, 0, 128), (165, 42, 42), (255, 192, 203)

# Initialisation de l'écran
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Blackjack")
horloge = pygame.time.Clock()
background = pygame.image.load("cartes/font.jpg")
fond = pygame.transform.scale(background, (LARGEUR, HAUTEUR))

# Police d'écriture
police = pygame.font.SysFont('Roboto', 50)
polices = pygame.font.SysFont('Roboto', 35)

# Charger les sons
# victoire = "son/win_sound.mp3"
# defaite = "son/lose_sound.mp3"

# Classe Carte
class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
        self.image = pygame.image.load(f"cartes/{valeur}_de_{couleur}.jpg")  # Charger l'image de la carte
        self.image = pygame.transform.scale(self.image, TAILLE_CARTE)

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

# Classe Jeu
class Jeu:
    VALEURS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi", "as"]
    COULEURS = ["coeur", "carreau", "pique", "trefle"]

    def __init__(self):
        self.paquet = [Carte(valeur, couleur) for valeur in self.VALEURS for couleur in self.COULEURS]
        random.shuffle(self.paquet)
        self.main_joueur = []
        self.main_croupier = []
        self.joueur_tour = True
        self.fin_partie = False

    def tirer_carte(self):
        return self.paquet.pop()

    def calculer_valeur_main(self, main):
        valeur = 0
        as_count = 0

        for carte in main:
            if carte.valeur in ["valet", "dame", "roi"]:
                valeur += 10
            elif carte.valeur == "as":
                valeur += 11
                as_count += 1
            else:
                valeur += int(carte.valeur)

        while valeur > 21 and as_count:
            valeur -= 10
            as_count -= 1

        return valeur

    def demarrer_partie(self):
        self.main_joueur = [self.tirer_carte(), self.tirer_carte()]
        self.main_croupier = [self.tirer_carte(), self.tirer_carte()]
        self.joueur_tour = True
        self.fin_partie = False

    def joueur_prend_carte(self):
        self.main_joueur.append(self.tirer_carte())
        if self.calculer_valeur_main(self.main_joueur) > 21:
            self.fin_partie = True

    def croupier_joue(self):
        while self.calculer_valeur_main(self.main_croupier) < 17:
            self.main_croupier.append(self.tirer_carte())
        self.fin_partie = True

# Fonction pour afficher du texte à l'écran
def afficher_texte(texte, x, y, couleur=COULEUR_TEXTE):
    surface_texte = polices.render(texte, True, couleur)
    ecran.blit(surface_texte, (x, y))

# Fonction pour afficher les cartes
def afficher_cartes(main, x, y, masquer_premiere_carte=False):
    for i, carte in enumerate(main):
        if masquer_premiere_carte and i == 0:
            pygame.draw.rect(ecran, (255, 255, 200), (x, y, TAILLE_CARTE[0], TAILLE_CARTE[1]))  
        else:
            ecran.blit(carte.image, (x, y))
        x += TAILLE_CARTE[0] + 10

# Fonction principale
def main():
    jeu = Jeu()
    jeu.demarrer_partie()

    while True:
        ecran.blit(fond, (0, 0))
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 50 <= x <= 200 and 500 <= y <= 550:  # Bouton "Prendre"
                    jeu.joueur_prend_carte()
                if 250 <= x <= 400 and 500 <= y <= 550:  # Bouton "Passer"
                    jeu.joueur_tour = False
                    jeu.croupier_joue()
                if jeu.fin_partie:
                    if 50 <= x <= 200 and 600 <= y <= 650:  # Bouton "Rejouer"
                        jeu.demarrer_partie()
                    if 250 <= x <= 400 and 600 <= y <= 650:  # Bouton "Quitter"
                        pygame.quit()
                        sys.exit()

        # Affichage des cartes
        afficher_texte("Main du joueur :", 50, 50)
        afficher_cartes(jeu.main_joueur, 50, 100)

        afficher_texte("Main du croupier :", 50, 300)
        afficher_cartes(jeu.main_croupier, 50, 350, masquer_premiere_carte=not jeu.fin_partie)

        # Affichage des boutons
        pygame.draw.rect(ecran, ORANGE, (50, 500, 150, 50))  # Bouton "Prendre"
        afficher_texte("Prendre", 70, 510)

        pygame.draw.rect(ecran, GREEN, (250, 500, 150, 50))  # Bouton "Passer"
        afficher_texte("Passer", 270, 510)

        if jeu.fin_partie:
            pygame.draw.rect(ecran, WHITE, (50, 600, 150, 50))  # Bouton "Rejouer"
            afficher_texte("Rejouer", 70, 610)

            pygame.draw.rect(ecran, PINK, (250, 600, 150, 50))  # Bouton "Quitter"
            afficher_texte("Quitter", 270, 610)

            # Affichage des résultats
            valeur_joueur = jeu.calculer_valeur_main(jeu.main_joueur)
            valeur_croupier = jeu.calculer_valeur_main(jeu.main_croupier)

            if valeur_joueur > 21:
                # pygame.display.update()
                # pygame.mixer.music.load(defaite)
                # pygame.mixer.music.play()
                afficher_texte("Vous avez dépassé 21. Vous avez perdu !", 550, 50, RED)
            elif valeur_croupier > 21:
                # pygame.display.update()
                # pygame.mixer.music.load(victoire)
                # pygame.mixer.music.play()
                afficher_texte("Le croupier a dépassé 21. Vous avez gagné !", 550, 50, PURPLE)
            elif valeur_joueur > valeur_croupier:
                # pygame.display.update()
                # pygame.mixer.music.load(victoire)
                # pygame.mixer.music.play()
                afficher_texte("Vous avez gagné !", 550, 50, PURPLE)
            elif valeur_joueur < valeur_croupier:
                # pygame.display.update()
                # pygame.mixer.music.load(defaite)
                # pygame.mixer.music.play()
                afficher_texte("Le croupier a gagné !", 550, 50, RED)
                
            else:
                afficher_texte("Égalité !", 550, 50, BLACK)

        pygame.display.flip()
        horloge.tick(FPS)

# Lancer le jeu
if __name__ == "__main__":
    main()
