# tester le fichier

# compléter le code fourni : 

# la méthode update() de la classe Ennemi

# le déplacement des tirs

# la création d'un nouvel ennemi


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
    
    def tirer(self) :
        "renvoie les coordonnées du tir, sous forme d'un dictionnaire"
        return { 'x' : self.x + 16,
                 'y' :  self.y+8,
                 'v' : self.vitesse+3}


class Ennemi :
    """Définit un ennemi ayant :
        pour attributs :  x, y  (coordonnées à l'écran)
                          vitesse (nombre de pixel d'un déplacement élémentaire) égale à 1 par défaut
                          actif (booléen qui signale un ennemi actif) => les ennemis inactifs seront supprimés
                          
        pour méthodes  :  update (qui met à jour les coordonnées de l'ennemi
        ces méthodes mettent à jour les attributs x et y, en tenant compte de la vitesse du déplacement"""
    
    def __init__(self, vitesse = 1) :
        self.x = 240
        self.y = pyxel.rndi(10,240)
        self.vitesse = vitesse
        self.actif = True 
    
    def update(self) :
        ###############
        # a completer #
        ###############
        if self.x < 16 :
            self.actif = False 
        


class Jeu:
    def __init__(self):
        pyxel.init(256,256, title="Vaisseau")
        
        self.vaisseau = Vaisseau(60,60, 2)
        self.en_list = [ Ennemi() ]
        self.tir_list = [ { 'x' : 100, 'y' :  100, 'v' : 4}]
        
        pyxel.run(self.update,self.draw)

    def update(self):
        # déplacement des ennemis
        for ennemi in self.en_list :
            ennemi.update()
        
        # déplacement des tirs
        ###############
        # a completer #
        ###############
        
        
        # déplacement du vaisseau
        if pyxel.btn(pyxel.KEY_UP) :
            self.vaisseau.haut()
        if pyxel.btn(pyxel.KEY_DOWN) :
            self.vaisseau.bas()
        if pyxel.btn(pyxel.KEY_RIGHT) :
            self.vaisseau.droite()
        if pyxel.btn(pyxel.KEY_LEFT) :
            self.vaisseau.gauche()
        
        # tir du vaisseau
        if pyxel.btnp(pyxel.KEY_SPACE, hold=10, repeat=10) :
            self.tir_list.append( self.vaisseau.tirer() )
        
        # détection des collisions et liste des tirs à supprimer
        tir_a_supprimer = []
        for ennemi in self.en_list :
            for tir in self.tir_list :
                if ennemi.x < tir['x'] + 5  < ennemi.x + 16 :
                    if ennemi.y < tir['y'] < ennemi.y + 16 :
                        print('touché')
                        ennemi.actif = False
                        tir_a_supprimer.append(tir)
                        
        # suppression des tirs déjà utilisés
        for tir in tir_a_supprimer :
            self.tir_list.remove(tir)
        # suppression des ennemis inactifs
        a_supprimer = [ ennemi for ennemi in self.en_list if ennemi.actif is False ]
        for ennemi in a_supprimer :
            self.en_list.remove(ennemi)
        
        
        # création ennemi
        if pyxel.frame_count % 50 == pyxel.rndi(0,1) :
            print("créer un ennemi")            
            ###############
            # a completer # 
            ###############
        
            
        
        

    def draw(self):
        pyxel.cls(0)
        # vaisseau
        pyxel.rect(self.vaisseau.x,self.vaisseau.y,16,16,9)
        # ennemis
        for ennemi in self.en_list :
            pyxel.rect(ennemi.x,ennemi.y,16,16,11)
        # tirs
        for tir in self.tir_list :
            x,y = tir['x'], tir['y']
            pyxel.line(tir['x'], tir['y'], tir['x']+5, tir['y'],10)
        
        

Jeu()