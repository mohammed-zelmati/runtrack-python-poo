"""
Créer la classe Livre qui prend en attributs privés un titre, un auteur et un nbPages de pages.
Créer les accesseurs et mutateurs nécessaires afin de pouvoir modifier et
afficher les attributs. Pour changer le nbPages de pages, ce dernier doit être
un nbPages entier positif, sinon la valeur n’est pas changée et un message
d’erreur est affiché.
"""
class Livre:
    def __init__(self, titre, auteur, nbPages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbPages = nbPages if nbPages > 0 else None

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


# Exemple d'utilisation
mon_livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
print(mon_livre.get_titre())  # Affiche "Le Petit Prince"
print(mon_livre.get_nbPages())  # Affiche 96
print(mon_livre.get_auteur())  # Affiche l'auteur (prénom et nom)

mon_livre.set_nbPages(120)
print(mon_livre.get_nbPages())  # Affiche 120

mon_livre.set_nbPages(-5)  # Affiche "Erreur : Le nombre de pages doit être un entier positif."