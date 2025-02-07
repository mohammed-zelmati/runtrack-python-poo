"""
Créer une classe Rectangle avec des attributs privés, longueur et largeur
initialisées dans le constructeur.
Créer des accesseurs et mutateurs afin de pouvoir afficher et modifier les
attributs de la classe.

Créer un rectangle avec les valeurs suivantes : longueur 10 et largeur 5.
Changer la valeur de la longueur et de la largeur et vérifier que les
modifications soient bien prises en compte.
"""

class Rectangle:
    def __init__(self, longueur, largeur):
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

# Création d'un rectangle avec longueur 10 et largeur 5
rectangle = Rectangle(10, 5)

# Afficher les valeurs initiales
print(f"Longueur: {rectangle.get_longueur()}, Largeur: {rectangle.get_largeur()}")

# Changer les valeurs de longueur et largeur
rectangle.set_longueur(15)
rectangle.set_largeur(8)

# Vérifier les modifications
print(f"Nouvelles valeurs - Longueur: {rectangle.get_longueur()}, Largeur: {rectangle.get_largeur()}")
