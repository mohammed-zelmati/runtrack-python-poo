"""
Récupérer la classe Livre. Ajouter l'attribut privé suivant :
- disponible est initialisé par défaut à True.
Créer une méthode nommée vérification qui vérifie si le livre est disponible,
c'est-à-dire que la valeur de son attribut disponible est égale à True. Cette
méthode doit retourner True ou False.
Ajouter une méthode emprunter qui rend le livre indisponible, autrement dit
la valeur de disponible devient False. Bien sûr, pour pouvoir emprunter un
livre, il faut que celui-ci soit disponible, vérifiez donc que celui-ci soit
disponible sans utiliser l’attribut disponible.
Après avoir emprunté un livre, il faut pouvoir le rendre. Créer une méthode
rendre qui dans un premier temps vérifie si le livre a bien été emprunté ( sans
utiliser l’attribut disponible), puis change la valeur de l’attribut disponible.
"""
class Livre:
    def __init__(self, titre, auteur, nbPages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbPages = nbPages if nbPages > 0 else None
        self.__disponible = True

    def get_titre(self):
        return self.__titre    
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nbPages(self):
        return self.__nbPages
    
    def set_titre(self,titre):
        self.__titre = titre   
    
    def set_auteur(self, auteur):
        self.__auteur = auteur
    
    def set_nbPages(self, nbPages):
        if isinstance(nbPages, int) and nbPages > 0:
            self.__nbPages = nbPages
        else: 
            print("Erreur : Le nombre de pages doit être un entier positif.")  

    def verification(self) :
        return self.__disponible
         
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print(f"Le livre '{self.__titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.__titre}' n'est pas disponible pour emprunt.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print(f"Le livre '{self.__titre}' a été rendu.")
        else:
            print(f"Le livre '{self.__titre}' n'a pas été emprunté.")

# Exemple d'utilisation
mon_livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
print(mon_livre.get_titre())  # Affiche "Le Petit Prince"
print(mon_livre.get_auteur())  # Affiche l'auteur (prénom et nom)
print(mon_livre.get_nbPages())  # Affiche 96

mon_livre.set_nbPages(120)
print(mon_livre.get_nbPages())  # Affiche 120

mon_livre.set_nbPages(-5)  # Affiche "Erreur : Le nombre de pages doit être un entier positif."

print(mon_livre.verification())  # Affiche True
mon_livre.emprunter()  # Affiche "Le livre 'Le Petit Prince' a été emprunté."
print(mon_livre.verification())  # Affiche False
mon_livre.emprunter()  # Affiche "Le livre 'Le Petit Prince' n'est pas disponible pour emprunt."
mon_livre.rendre()  # Affiche "Le livre 'Le Petit Prince' a été rendu."
print(mon_livre.verification())  # Affiche True
mon_livre.rendre()  # Affiche "Le livre 'Le Petit Prince' n'a pas été emprunté."

        