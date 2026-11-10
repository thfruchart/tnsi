# FICHIER vaisseau.py

# compléter la définition du constructeur

# écrire toutes les méthodes

# ajouter un attribut pv (points de vies) fixée initialement à 3.

# ajouter une méthode vies_evol qui modifie le nombre de vies en y ajoutant la valeur passée en paramètre.



class Vaisseau :
    """Définit un objet ayant :
        pour attributs :  x, y  (coordonnées à l'écran)
                          vitesse (nombre de pixel d'un déplacement élémentaire) égale à 1 par défaut
        pour méthodes  :  gauche(), droite(), haut(), bas()
        ces méthodes mettent à jour les attributs x et y, en tenant compte de la vitesse du déplacement"""
    
    def __init__(self, x, y, vitesse) :
        ... = x
        ... = y
        ... = vitesse 
    
    def gauche(self) :
        ...
        
    def __repr__(self) :
        return f"Vaisseau(x = {self.x}, y = {self.y}, vitess = {self.vitesse})"
    