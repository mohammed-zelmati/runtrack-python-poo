"""
Créer une classe nommée Student qui a comme attributs privés un nom, un
prénom, un numéro d’étudiants et un nombre de crédits par défaut à zéro. La
méthode add_credits permet d’ajouter un nombre de crédits au total de
celui de l’étudiant. Ce mutateur doit s’assurer que la valeur passée en
argument est supérieure à zéro pour garantir l’intégrité de la valeur.
Instancier un objet représentant l’étudiant John Doe qui possède le numéro
d’étudiant 145. Ajoutez-lui des crédits à trois reprises et imprimez son total de
crédits en console.
Résultat attendu : 
Le nombre de credits de John Doe est de 30 points

Pour des mesures de confidentialité, l'établissement ne souhaite pas
divulguer la façon dont elle évalue le niveau de ses étudiants. Pour répondre
à cette problématique, créer une méthode nommée student_eval qui sera
privée Cette méthode retourne “Excellent” si le nombre de crédits est égal ou
supérieur à 90, “Très bien” si le nombre est supérieur ou égal à 80, “Bien” si le
nombre est supérieur ou égale à 70, “Passable” si égale ou supérieure à 60 et
“Insuffisant” si inférieur à 60.
Ajouter l’attribut privé nommé level dans le constructeur de la classe Student
qui prend en valeur la méthode student_eval. Créer une méthode
student_info qui écrit en console les informations de l’étudiant (nom,
prénom, identifiant et son niveau).

Résultat attendu : 
Nom = John 
Prénom = Doe
id = 145 
Niveau = Bien
"""

class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()

    def __student_eval(self):
        if self.__credits >= 50:
            return "Excellent"
        elif self.__credits >= 40:
            return "Très bien"
        elif self.__credits >= 30:
            return "Bien"
        elif self.__credits >= 10:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Nom = {self.__nom}")
        print(f"Prénom = {self.__prenom}")
        print(f"id = {self.__num_etudiant}")
        print(f"Niveau = {self.__level}")

# Création de l'objet Student pour John Doe
john_doe = Student("John", "Doe", 145)

# Ajout de crédits
john_doe.add_credits(10)
john_doe.add_credits(10)
john_doe.add_credits(10)

# Affichage du total de crédits
print(f"Le nombre de crédits de John Doe est de {john_doe._Student__credits} points")

# Affichage des informations de l'étudiant
john_doe.student_info()
