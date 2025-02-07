"""Créer une classe nommée Forme possédant une méthode nommée aire qui renvoie 0.
Créer une classe Rectangle qui hérite de la classe Forme et qui possède deux attributs largeur et hauteur. 
Surcharger la méthode aire dans la classe Rectangle afin qu’elle ne renvoie plus 0, mais l’aire du rectangle.
Écrire en console le résultat de la méthode aire de la classe Rectangle.
"""

class Forme:
    def aire(self):
        return 0
    
class Rectangle(Forme):    
    def __init__(self,  largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    # Surcharge de la méthode aire
    def aire(self):
        return self.largeur * self.hauteur  # Calcul de l'aire du rectangle

# Instanciation de Rectangle
rectangle = Rectangle(8, 6)

# Calcul et affichage de l'aire du rectangle
print(f"L'aire du rectangle est : {rectangle.aire()}")       
