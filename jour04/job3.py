"""Créer une classe Rectangle avec comme attribut privé longueur et largeur.
Créer la méthode perimètre permettant de calculer le périmètre du
rectangle ainsi que la méthode surface permettant de calculer la surface du rectangle.
Créer les accesseurs (getters) et mutateurs (setters) permettant de manipuler les attributs de la classe.

Créer une classe Parallelepipede héritant de la classe Rectangle avec en plus un attribut hauteur et 
une autre méthode volume, permettant de calculer le volume du parallélépipède.

Instancier la classe Rectangle et assurez-vous que toutes les méthodes fonctionnent."""

class Rectangle:

    def __init__(self, longueur , largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Accesseurs (getter)
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs (setter)
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    # calculer le périmètre du rectangle
    def perimetre(self):
        return (self.__longueur + self.__largeur) * 2
    
    # calculer la surface du rectangle
    def surface(self):
        return self.__longueur * self.__largeur
    
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur= hauteur
    # Accesseur (getter)
    def get_hauteur(self):
        return self.hauteur

    # Mutateur(setter)
    def set_hauteur(self, hauteur):
        self.hauteur = hauteur

    # calculer le volume du parallélépipède
    def volume(self):
        return self.surface() * self.hauteur

# Instanciation de la classe Rectangle
perimetre = Rectangle(3,4)
# calculer le périmètre 
print (f"Le périmètre est {perimetre.perimetre()}")
# calculer la surface
print (f"La surface est {perimetre.surface()}")

# Instantanciation de la classe  Parallelepipede
volume =  Parallelepipede(3,4,5)
print (f"Le volume est {volume.volume()}")

# changer la longueur, la largeur et l'hauteur 
volume.set_longueur(12)
volume.set_largeur(10)
volume.set_hauteur(2)

# afficher la longueur, la largeur et l'hauteur modifieés
print (f"La longueur est {volume.get_longueur()}")
print (f"La largeur est {volume.get_largeur()}")
print (f"La largeur est {volume.get_hauteur()}")




