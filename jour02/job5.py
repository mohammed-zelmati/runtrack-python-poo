"""
Créer une classe Voiture qui a pour attributs privés une marque, un modèle, une année, un kilométrage et un attribut nommé 
en_marche initialisé par défaut à False.Cette classe doit posséder des mutateurs et accesseurs pour chaque attribut.
Créer une méthode demarrer qui change la valeur de l’attribut en_marche en True, une méthode arreter qui change la valeur
de l’attribut en_marche en False.
Ajouter à la classe Voiture l’attribut privé reservoir qui est initialisé à 50 par défaut dans le constructeur. 

Créer une méthode privée verifier_plein qui retourne la valeur de l’attribut reservoir. Cette méthode est appelée dans la
méthode demarrer. Si la valeur du réservoir est supérieure à 5 la voiture peut démarrer.
"""
class Voiture:
    # Initialisation des attributs privés
    def __init__(self, marque, model, annee, kilometres):
        self.__marque = marque
        self.__model = model
        self.__annee = annee
        self.__kilometres = kilometres
        self.__en_marche = False # Par défaut, la voiture est à l'arrêt
        self.__reservoir = 50 # Le réservoir est initialisé à 50 par défaut

    # Accesseurs (getters)
    def get_marque(self):
        return self.__marque
    
    def get_model(self):
        return self.__model
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometres(self):
        return self.__kilometres
    
    def get_en_marche(self):
        return  self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    # Mutateurs (setters)===========debut=======================
    def set_marque(self,marque):
        self.__marque = marque  

    def set_model(self,model):
        self.__model = model

    def set_annee(self,annee):
        self.__annee = annee  

    def set_kilometres(self,kilometres):
        self.__kilometres = kilometres

    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir
    # Mutateurs (setters)============fin======================

    def demarrer (self):
        if self.verifier_plein() > 5:
            self.__en_marche = True
            print ("La voiture a démarré.")
        else:
            print(f"La voiture ne peut pas demarrer (le réservoir est trop bas).")

    def arreter (self):  
        self.__en_marche = False 
        print("La voiture est à l'arrêt.") 

    def verifier_plein (self):
        return self.__reservoir      

# Création de l'instance de la voiture
toyota = Voiture("Toyota", "Corolla", 2023, 1070000)
toyota.set_reservoir(43)  # Définir le réservoir à 43 litres

# Affichage des informations de la voiture
print("=== Informations de la voiture ===")
print(f"Marque : {toyota.get_marque()}")
print(f"Modèle : {toyota.get_model()}")
print(f"Année : {toyota.get_annee()}")
print(f"Kilométrage : {toyota.get_kilometres()} km")
print(f"Réservoir : {toyota.get_reservoir()} litres")
print(f"En marche : {toyota.get_en_marche()}")

# Démarrage de la voiture
print("\n=== Démarrage de la voiture ===")
toyota.demarrer()  # La voiture devrait démarrer car le réservoir > 5 litres
print(f"En marche : {toyota.get_en_marche()}")

# Arrêt de la voiture
print("\n=== Arrêt de la voiture ===")
toyota.arreter()
print(f"En marche : {toyota.get_en_marche()}")

# Tester avec un réservoir trop bas
print("\n=== Test avec un réservoir trop bas ===")
toyota.set_reservoir(3)  # Définir le réservoir à 3 litres
toyota.demarrer()  # La voiture ne devrait pas démarrer
print(f"En marche : {toyota.get_en_marche()}")

