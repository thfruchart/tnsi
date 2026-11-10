import pyxel

class Vaisseau :
    """Définit un objet ayant :
        pour attributs :  x, y  (coordonnées à l'écran)
                          vitesse (nombre de pixel d'un déplacement élémentaire) égale à 1 par défaut
                          pv (nombre de points de vies) égal à 3 par défaut
        pour méthodes  :  gauche(), droite(), haut(), bas()
        ces méthodes mettent à jour les attributs x et y, en tenant compte de la vitesse du déplacement"""
    
    def __init__(self, x, y, vitesse = 1, pv = 3) :
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.pv = pv 
    
    def gauche(self) :
        self.x -= self.vitesse
        return self
    
    def droite(self) :
        self.x += self.vitesse
        return self
    
    def bas(self) :
        self.y += self.vitesse
        return self
    
    def haut(self) :
        self.y -= self.vitesse
        return self
    
    def vies_evol(self,nb) :
        self.pv += nb
        return self 
        
    def __repr__(self) :
        return f"Vaisseau(x = {self.x}, y = {self.y}, vitesse = {self.vitesse}, pv = {self.pv})"


class Jeu:
    def __init__(self):
        pyxel.init(256,256, title="Vaisseau")
        
        self.vaisseau = Vaisseau(60,60)
        
        pyxel.run(self.update,self.draw)

    def update(self):
        # déplacement du vaisseau
        if pyxel.btn(pyxel.KEY_UP) :
            self.vaisseau.haut()
            
        

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.vaisseau.x,self.vaisseau.y,16,16,9)

Jeu()