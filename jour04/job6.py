"""Créer une classe Vehicule avec comme attribut une marque, le modèle, une année et un prix. Créer la méthode 
informationsVehicule qui écrit en console la marque, le modèle, l'année et le prix du véhicule.
Créer la classe Voiture qui hérite de la classe Vehicule. Dans le constructeur de la classe Voiture, ajouter 
un attribut portes qui contient le nombre entier 4.
Créer dans cette classe, une méthode informationsVehicule qui affiche, en console, les informations générales du véhicule
 et le nombre de portes de la voiture.
Instancier un objet Voiture, passer les informations dont la classe a besoin et faites appel à la méthode informationsVehicule.
Résultat attendu :
                    Marque = Mercedes
                    Model = Classe A
                    Année = 2020
                    Prix = 18500
                    Portes = 4
Créer une classe Moto qui hérite de la classe Vehicule et ajouter l'attribut roue qui contient par défaut l’entier 2. 
Créer à nouveau une méthode informationsVehicule dans la classe Moto qui affiche l'intégralité des informations de la moto.
Instancier un objet Moto et faites appel à la méthode informationsVehicule.
Résultat attendu :
                    Marque = Yamaha
                    Model = 1200 Vmax
                    Année = 1987
                    Prix = 4500
                    Nombre de roue = 2
Créer la méthode demarrer dans la classe Véhicule qui écrit en console . Surcharger la méthode demarrer 
dans la classe Moto et Voiture afin d’afficher un message personnalisé. Faites démarrer votre voiture et votre moto."""

class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque = {self.marque}\nModel = {self.modele }\nAnnée = {self.annee}\nPrix = {self.prix}") 

    def demarrer (self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)  # Appel du constructeur de la classe parente
        self.portes = 4  # Ajout de l'attribut portes

    # Surcharge de la méthode informationsVehicule
    def informationsVehicule(self):
        super().informationsVehicule()  # Appel de la méthode de la classe parente
        print(f"Nombre de portes = {self.portes}")

    def demarrer(self) :
        print("Faites démarrer votre voiture.")
        super().demarrer() # Appel de la méthode de la classe parente
        
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)  # Appel du constructeur de la classe parente
        self.roues = 2  # Ajout de l'attribut roues

    # Surcharge de la méthode informationsVehicule
    def informationsVehicule(self):
        super().informationsVehicule()  # Appel de la méthode de la classe parente
        print(f"Nombre de roues = {self.roues}")

    def demarrer(self) :
        print("Faites démarrer votre moto.")
        super().demarrer() # Appel de la méthode de la classe parente    
       
# Instanciation d'un objet Voiture
voiture = Voiture("Mercedes", "Calsse A", 2020, 18500)
# Appel de la méthode informationsVehicule
voiture.informationsVehicule()
voiture.demarrer()
print("=================================================")
# Instanciation d'un objet Moto
moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
# Appel de la méthode informationsVehicule
moto.informationsVehicule()
moto.demarrer()

