"""
Créez une classe Animal avec un attribut age initialisé à zéro et prenom
initialisé vide dans son constructeur.
Instanciez un objet Animal et affichez en console l’attribut âge. Créez une
méthode vieillir qui ajoute 1 à l'âge de l’animal. Faites vieillir votre animal et
affichez son âge mis à jour en console.

Résultat attendu : L'age de l'animal 0 ans
                   L'age de l'animal 1 ans
Créez une méthode nommer qui prend en paramètre le nom de l’animal.
Nommez votre animal et affichez en console son nom.

Résultat attendu : L'animal se nomme Luna
"""
class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
            self.nom = nom

# Instanciation de la classe Animal
animal = Animal()

# Affichage de l'âge initial
print(f"L'age de l'animal  {animal.age} ans")

# Faire vieillir l'animal
animal.vieillir()

# Affichage de l'âge mis à jour
print(f"L'age de l'animal  {animal.age} ans")

# Nommer l'animal
animal.nommer("Luna")

# Affichage du nom de l'animal
print(f"L'animal se nomme   {animal.nom}")