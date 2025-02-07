"""
Récupérer votre classe Forme crée juste au-dessus.
Créer une classe fille nommée Cercle qui hérite de la classe Forme et possédant un attribut radius.
Surcharger la méthode aire dans la classe Cercle pour qu'elle renvoie l’aire du cercle.
Créez une instance de chaque classe Rectangle et Cercle et utilisez-les pour tester les différentes
surcharges de la méthode aire en affichant les résultats en console."""


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

class Cercle(Forme):    
    def __init__(self,  radius=3.14):
        self.radius = radius
        

    # Surcharge de la méthode aire
    def aire(self, rayon):
        return self.radius * rayon ** 2  # Calcul de l'aire du cercle

# Instanciation de Cercle
cercle = Cercle()
# Instanciation de Rectangle
rectangle = Rectangle(2,3)

# Calcul et affichage de l'aire du cercle
print(f"L'aire du cercle est : {cercle.aire(2)}")     

# Calcul et affichage de l'aire du rectangle
print(f"L'aire du rectangle est : {rectangle.aire()}")     