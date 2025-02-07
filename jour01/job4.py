"""
Créez une classe Personne avec les attributs nom et prenom. Ajoutez une
méthode SePresenter qui retourne le nom et le prénom de la personne.
Ajoutez aussi un constructeur prenant en paramètres de quoi donner des
valeurs initiales aux attributs nom et prenom. Instanciez plusieurs personnes
avec les valeurs de construction de votre choix et faites appel à la méthode
SePresenter afin de vérifier que tout fonctionne correctement.
Résultat attendu : Je suis John Doe
                   Je suis Jean Dupond
"""
class Personne :
    def __init__ (self, nom ,prenom):
        self.nom = nom
        self.prenom = prenom
    #  Méthode pour présenter le prénom et le nom
    def SePresenter (self):
        print(f"Je suis {self.prenom} {self.nom}") 

# Instanciation de la classe Operation
presenter1 = Personne("Doe","John")
presenter2 = Personne("Dupond","Jean")

# Appel de la méthode addition pour afficher le résultat en console
presenter1.SePresenter()  
presenter2.SePresenter()          