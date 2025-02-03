"""Créez une classe Personnage représentant un personnage de jeu. Le plateau
de jeu est représenté par une matrice. Le joueur est défini par ses attributs x
et y, représentant les index du tableau.
Créez le constructeur de cette classe en initialisant la position (x et y).
Créez les méthodes : gauche, droite, bas et haut permettant respectivement
de faire avancer à gauche et à droite, en haut ou en bas.
Implémentez une méthode “position” renvoyant les coordonnées sous forme
d’un tuple."""


class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def bas(self):
        self.y += 1

    def haut(self):
        self.y -= 1

    def position(self):
        return (self.x, self.y)

# Instanciation de la classe Personnage
joueur = Personnage(1, 1)

# Déplacement du joueur
joueur.gauche()
joueur.bas()

# Affichage de la position actuelle
print(f"Position actuelle : {joueur.position()}")
