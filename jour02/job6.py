"""
Créer une classe Commande avec les attributs privés, numéro de
commande, liste de plats commandés et statut de la commande (en cours,
terminée ou annulée).

Ajouter des méthodes permettant d’ajouter un plat à la commande, annuler
une commande, calculer le total d’une commande privée et afficher une
commande avec son total à payer, ainsi qu’une méthode permettant de
calculer la TVA.

Utiliser l’encapsulation et l’abstraction pour créer cette classe de manière que
les attributs ne puissent pas être modifiés de l’extérieur. La liste des plats
commandés doit être représentée sous forme de dictionnaire avec les noms
des plats, le prix ainsi que le statut de la commande.
"""
class Commande:
    def __init__(self, numero_commande):
        # Initialisation des attributs privés
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  # Dictionnaire pour stocker les plats commandés
        self.__statut = "en cours"  # Statut initial de la commande

    # Accesseurs (getters)
    def get_numero_commande(self):
        return self.__numero_commande

    def get_plats_commandes(self):
        return self.__plats_commandes

    def get_statut(self):
        return self.__statut

    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix_plat):
        if self.__statut == "en cours":  # On ne peut ajouter un plat que si la commande est en cours
            self.__plats_commandes[nom_plat] = prix_plat
            print(f"Plat '{nom_plat}' ajouté à la commande.")
        else:
            print("Impossible d'ajouter un plat : la commande n'est pas en cours.")

    # Méthode pour annuler une commande
    def annuler_commande(self):
        if self.__statut == "en cours":
            self.__statut = "annulée"
            print("La commande a été annulée.")
        else:
            print("La commande ne peut pas être annulée (déjà terminée ou annulée).")

    # Méthode privée pour calculer le total de la commande
    def __calculer_total(self):
        return sum(self.__plats_commandes.values())

    # Méthode pour afficher la commande avec le total à payer
    def afficher_commande(self):
        if self.__statut == "annulée":
            print("La commande est annulée.")
            return

        print(f"\n=== Commande n°{self.__numero_commande} ===")
        print("Plats commandés :")
        for plat, prix in self.__plats_commandes.items():
            print(f"- {plat} : {prix} €")
        print(f"Total à payer : {self.__calculer_total()} €")
        print(f"Statut : {self.__statut}")

    # Méthode pour calculer la TVA (20% par défaut)
    def calculer_tva(self, taux_tva=0.20):
        total = self.__calculer_total()
        tva = total * taux_tva
        print(f"TVA ({taux_tva * 100}%) : {tva} €")
        return tva

    # Méthode pour terminer la commande
    def terminer_commande(self):
        if self.__statut == "en cours":
            self.__statut = "terminée"
            print("La commande a été terminée.")
        else:
            print("La commande ne peut pas être terminée (déjà terminée ou annulée).")


# Exemple
# Création d'une commande
commande1 = Commande(12345)

# Ajout de plats à la commande
commande1.ajouter_plat("Pizza", 10)
commande1.ajouter_plat("Spaghetti", 12)
commande1.ajouter_plat("Tiramisu", 6)

# Affichage de la commande
commande1.afficher_commande()

# Calcul de la TVA
commande1.calculer_tva()

# Terminer la commande
commande1.terminer_commande()

# Essayer d'ajouter un plat après avoir terminé la commande
commande1.ajouter_plat("Glace", 4)  # Ne fonctionnera pas

# Annuler la commande (ne fonctionnera pas car elle est déjà terminée)
commande1.annuler_commande()

# Afficher la commande après tentative d'annulation
commande1.afficher_commande()