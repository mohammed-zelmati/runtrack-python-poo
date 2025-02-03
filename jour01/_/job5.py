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

        

    