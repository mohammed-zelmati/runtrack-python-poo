"""Créer une classe Personne qui aura comme attribut age prenant un entier et
initialisé à 14 par défaut. Ajouter une méthode afficherAge qui affichera en
console l'âge de la personne et une méthode bonjour qui écrit en console
‘Hello’. Créer une méthode modifierAge prenant en paramètre un entier et
permettant de modifier l'âge de la personne.

Créer une classe Eleve qui hérite de la classe Personne qui n’a pas d’attribut
et une méthode publique allerEnCours qui affiche : “Je vais en cours” ainsi
qu’une méthode afficherAge qui écrit en console : “J’ai XX ans”.

Créer une classe Professeur avec un attribut privé matiereEnseignee, qui
indiquera la matière du professeur, et une méthode publique enseigner qui
affiche : “Le cours va commencer”.

Instancier une classe Personne et une classe Eleve. Afficher l'âge par défaut
de l’élève en console."""

class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, new_age):
        self.age = new_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, age=14, matiereEnseignee=None):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

# Instanciation des classes
personne = Personne()
eleve = Eleve() 

# Afficher l'âge  de l'élève par défaut
eleve.afficherAge()




