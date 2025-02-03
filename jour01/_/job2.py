""" 
À l’aide de la classe Operation créée au job1, imprimez en console la
valeur des attributs “nombre1” et “nombre2”.
Résultat attendu : Le nombre1 est 12
                   Le nombre2 est 3   
"""

class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation = Operation(12, 3)


# Impression des valeurs des attributs en console
print(f"Le nombre1 est {operation.nombre1}")
print(f"Le nombre2 est {operation.nombre2}")
