"""À l’aide de la classe Personne, Eleve et Professeur créent au-dessus, faites
dire bonjour à votre élève grâce à la méthode bonjour ainsi que “Je vais en
cours” grâce à la méthode allerEnCours. Redéfinir l'âge de l’élève à 15 ans.

Créez un objet Professeur, 40 ans, faites dire bonjour à votre professeur et
commencez le cours grâce à la méthode enseigner."""

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

eleve = Eleve()
eleve.bonjour()
eleve.allerEnCours()

# modifier l'âge de l'élève
eleve.modifierAge(15)

# afficher l'âge de l'élève
eleve.afficherAge()

professeur = Professeur()
# modifier l'âge de prof
professeur.modifierAge(40)

# afficher l'âge de prof
professeur.afficherAge()
professeur.bonjour()
professeur.enseigner()

# 