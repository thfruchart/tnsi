import pyxel
from random import randint

MARGE = 50

class App:
    orientation = { 0 : [(0,0), (-1,0) , (0,-1) ],
                 1 : [(0,0), (-1,0), (0,+1) ],
                 2 : [(0,0), (+1,0), (0,-1) ],
                 3 : [(0,0), (+1,0), (0,+1) ],
                }
    couleurs = [5,11,8,10]
    
    def __init__(self, n):
        self.nb = 2**n
        self.sens = 0
        # coordonnée de la case vide
        self.i_trou = randint(0, self.nb - 1 )
        self.j_trou = randint(0, self.nb - 1 )
        
        pyxel.init(256,256, title="Triominos")
        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)
            
    def get_coord(self):
        x, y = pyxel.mouse_x, pyxel.mouse_y
        largeur = (256 - MARGE * 2 ) // self.nb
        i = (y - MARGE) // largeur
        j = (x - MARGE) // largeur
        return i,j
    
    def possible(self,i,j,sens) :
        """renvoie True si la pièce (i,j,sens) est compatible avec les limites du jeu
        --- et avec la case vide"""
        if not (0 <= i < self.nb) :
            return False
        if not (0 <= j < self.nb) :
            return False
        if (i,j) == (self.i_trou, self.j_trou) :
            return False
        return True
        
    
    def update(self):
        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) :
            i,j = self.get_coord()
            print(i,j)
        if pyxel.btnr(pyxel.MOUSE_BUTTON_RIGHT) :
            self.sens += 1
        self.sens += pyxel.mouse_wheel
        self.sens %= 4
        
        
        
    
    def dessine_case(self,i,j, couleur, plein = True) :
        largeur = (256 - MARGE * 2 ) // self.nb
        
        y = MARGE + i * largeur
        x = MARGE + j * largeur
        
        if plein :
            pyxel.rect(x, y, largeur, largeur, couleur)
        else : 
            pyxel.rectb(x, y, largeur, largeur, couleur)
    
    def draw(self):
        pyxel.cls(0)
        # dessin du plateau
        for i in range(self.nb) :
            for j in range(self.nb) :
                self.dessine_case(i,j,9,False)
        # dessin de la case vide
        self.dessine_case(self.i_trou,self.j_trou,7)
        
        # dessin depuis la souris
        i,j = self.get_coord()
        if self.possible(i,j,self.sens) : 
            for case in  self.orientation[self.sens] :
                coul = self.couleurs[self.sens]
                delta_i, delta_j = case
                i_case = i + delta_i
                j_case = j + delta_j
                self.dessine_case(i_case,j_case,coul)
        
        
            
        
        
App(2)