"""
Créez une classe nommée Point avec les attributs x et y correspondant aux
coordonnées horizontales et verticales du point. Les deux attributs doivent
être initialisés dans le constructeur.

La classe Point doit posséder les méthodes suivantes :
➔ afficherLesPoints qui affiche les coordonnées des points.
➔ afficherX et afficherY qui affiche respectivement x et y.
➔ changerX et changerY qui change la valeur des attributs x et y.
"""

class Point :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints (self):
        print(f"x = {self.x} et y = {self.y}")   

    def afficherX (self):
        print(f"x = {self.x} ") 

    def afficherY (self):
        print(f"y = {self.y}")  

    def changerX (self, new_x) :
        self.x = new_x
        
    def changerY(self, new_y):
        self.y = new_y  


# Instanciation de la classe Point
point= Point(1,1)

# Affichage le coordonnées de point (1,1)
point.afficherLesPoints ()

# Affichage le x de point (1,1)
point.afficherX ()


# Affichage le y de point (1,1)
point.afficherY ()

# Changer le x de point (1,1)
point.changerX (3) 

# Changer le y de point (1,1)
point.changerY(2)

# Affichage des nouvelles coordonnées du point (3, 2)
point.afficherLesPoints()

    