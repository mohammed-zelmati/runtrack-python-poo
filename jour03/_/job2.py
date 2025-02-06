"""
Créer une classe CompteBancaire avec les attributs privés, numéro de compte, nom, prénom et solde. 
Cette classe doit posséder les méthodes suivantes :
➔ afficher : qui affiche le détail sur le compte.
➔ afficherSolde : cette méthode affiche dans le terminal le solde du client.
➔ versement : cette méthode prend un paramètre le montant du versement et ajoute celui-ci au solde du client.
➔ retrait : cette méthode prend un entier en argument (le montant à retirer) ,
enlève ce montant au solde du compte et affiche le nouveau solde.

Veillez à ce que le compte possède bien le montant disponible sinon un message d’erreur est affiché.

Créer un compte avec les valeurs de construction de votre choix et faites appel aux différentes méthodes 
afin de vérifier que tout fonctionne correctement.

Ajouter l’attribut découvert à votre classe CompteBancaire, cet attribut aura
pour valeur un booléen. Si le client a le droit à un découvert, la valeur de cet
attribut sera True et des opérations pourront être effectuées même si le solde
est de zéro (méthode retrait).

Ajouter les méthodes suivantes :
➔ agios : cette méthode permet d’appliquer des agios au solde du
compte si celui-ci est négatif.
➔ virement : cette méthode prend en paramètre une référence, un
compte bancaire (celui qui reçoit l’argent) et un montant. Un message
de confirmation ou d'erreur doit être affiché.

Créez une deuxième instance de la classe CompteBancaire. Ce deuxième
compte doit être à découvert (solde négatif). Faire un versement du premier
compte vers celui à découvert afin de le remettre à zéro.
"""
class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def get_numero(self):
        return self.__numero

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_solde(self):
        return self.__solde

    def afficher(self):
        print(f"Compte N°: {self.__numero}, Titulaire: {self.__prenom} {self.__nom}, Solde: {self.__solde}, Découvert: {self.__decouvert}")

    def afficherSolde(self):
        print(f"Le solde du compte est de: {self.__solde}")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} effectué. Nouveau solde: {self.__solde}")

    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} effectué. Nouveau solde: {self.__solde}")
        else:
            print(f"Erreur: Fonds insuffisants pour un retrait de {montant}. Solde actuel: {self.__solde}")

    def agios(self):
        if self.__solde < 0:
            print(f"Agios appliqués. Solde avant agios: {self.__solde}")
            self.__solde *= 1.1 # Appliquer un agio de 10%
            print(f"Nouveau solde après agios: {self.__solde}")

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} effectué vers le compte N°: {compte_destinataire.get_numero()}")
        else:
            print(f"Erreur: Fonds insuffisants pour un virement de {montant}. Solde actuel: {self.__solde}")

# Création d'une première instance de la classe CompteBancaire
compte1 = CompteBancaire(numero=10203090, nom="Dupont", prenom="Jean", solde=10000, decouvert=True)
compte1.afficher()
compte1.afficherSolde()

# Création d'une deuxième instance de la classe CompteBancaire avec un solde négatif
compte2 = CompteBancaire(numero=20984500, nom="Martin", prenom="Marie", solde=-300, decouvert=True)
compte2.afficher()
compte2.agios()

# Virement du premier compte vers le deuxième compte
compte1.virement(compte2, 330)

# solde compte2
print(f"Le solde de compte: {compte2.get_numero()} est {compte2.get_solde()}")

# solde compte1
print(f"Le solde de compte: {compte1.get_numero()} est {compte1.get_solde()}")
