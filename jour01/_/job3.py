
"""
Modifiez votre classe Operation afin d’y ajouter la méthode addition(). Cette
méthode additionne “nombre1” et “nombre2” et affiche en console le résultat.
"""
class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Le résultat de l'addition de {self.nombre1} et {self.nombre2} est: {resultat}")

# Instanciation de la classe Operation
operation = Operation(3, 5)

# Appel de la méthode addition pour afficher le résultat en console
operation.addition()