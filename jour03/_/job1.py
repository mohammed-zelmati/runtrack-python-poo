"""
Créer une classe Ville avec comme attributs privés un nom et un nombre d'habitants.
Créer une classe Personne avec les attributs privés suivants : nom, âge et un objet de la classe ville.
Ajouter la méthode ajouterPopulation dans la classe Personne qui permet d’augmenter de 1 le nombre d’habitants de la ville.
Créer un objet Ville avec comme arguments “Paris” et 1000000.
Afficher en console le nombre d’habitants de la ville de Paris.
Créer un autre objet Ville avec comme arguments “Marseille” et 861635.
Afficher en console le nombre d’habitants de la ville de Marseille.
Créer les objets suivants :
- John, 45 ans, habitant à Paris
- Myrtille, 4 ans, habitant à Paris.
- Chloé, 18 ans, habitant à Marseille.
Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de ces nouvelles personnes.
"""
class Ville:
    def __init__(self, nom, population):
        self.__nom = nom
        self.__population = population

    def get_nom(self):
        return self.__nom

    def get_population(self):
        return self.__population

    def ajouter_population(self, nombre=1):
        self.__population += nombre

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ville.ajouter_population()

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age
    
    def get_ville(self):
        return self.__ville

# Création des villes
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage du nombre d'habitants des villes
print(f"Population de la ville de : {paris.get_nom()} : {paris.get_population()} habitants")
print(f"Population de la ville de : {marseille.get_nom()} : {marseille.get_population()} habitants")

# Création des personnes
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Affichage du nombre d'habitants après l'arrivée des nouvelles personnes
print(f"Mise à jour de la population de la ville de : {paris.get_nom()} après l'arrivée de John et Myrtille : {paris.get_population()} habitants")
print(f"Mise à jour de la population de la ville de : {marseille.get_nom()} après l'arrivée de Chloé : {marseille.get_population()} habitants")
