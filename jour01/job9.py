""" 
Créez la classe Produit avec des attributs nom, prixHT, TVA. Implémentez la
méthode CalculerPrixTTC qui retourne le prix produit avec la TVA. Ajoutez la
méthode afficher qui liste l’ensemble des informations du produit.
Créez plusieurs produits et calculez leurs TVA.
Ajoutez des méthodes permettant de modifier le nom du produit et son prix.
Ainsi que des méthodes permettant de retourner chaque information du
produit.
Modifiez le nom et le prix de chaque produit et affichez en console le nouveau
prix des produits.
La fonction print() ne doit pas être utilisée dans la classe Produit.
"""


import math

class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return round(self.prixHT * (1 + self.TVA / 100), 2)

    def afficher(self):
        return f"Produit: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}%, Prix TTC: {self.CalculerPrixTTC()}"

    def changerNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def changerPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

    def obtenirPrixTTC(self):
        return self.CalculerPrixTTC()

# Création de plusieurs produits
produit1 = Produit("Produit A", 100, 20)
produit2 = Produit("Produit B", 150, 10)

# Affichage des informations des produits
print(produit1.afficher())
print(produit2.afficher())

# Modification du nom et du prix des produits
produit1.changerNom("Produit A+")
produit1.changerPrixHT(120)
produit2.changerNom("Produit B+")
produit2.changerPrixHT(180)

# Affichage des nouvelles informations des produits
print(produit1.afficher())
print(produit2.afficher())
