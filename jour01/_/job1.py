""" Créez une classe Operation avec un constructeur (méthode qui sera appelée
lors de l’instance de la classe). Ajoutez les attributs “nombre1” et “nombre2”
initialisés avec des valeurs par défaut. Instanciez votre première classe et
imprimez l’objet en console.
Résultat attendu : <__main__.Operation object at 0x000002335CE46A50>
"""
class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation de la classe Operation
operation = Operation()

# Impression de l'objet en console
print(operation)


      