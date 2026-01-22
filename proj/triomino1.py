import pyxel

MARGE = 50

class App:
    orientation = { 0 : [(0,0), (-1,0) , (0,-1) ],
                 1 : [(0,0), (-1,0), (0,+1) ],
                 2 : [(0,0), (+1,0), (0,-1) ],
                 3 : [(0,0), (+1,0), (0,+1) ],
                }
    
    
    def __init__(self, n):
        self.nb = 2**n
        
        pyxel.init(256,256, title="Triominos")
        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)
            
    def get_coord(self):
        x, y = pyxel.mouse_x, pyxel.mouse_y
        largeur = (256 - MARGE * 2 ) // self.nb
        i = (y - MARGE) // largeur
        j = (x - MARGE) // largeur
        return i,j
    
    def update(self):
        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) :
            i,j = self.get_coord()
            print(i,j) 
        
        
    
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
        pyxel.rect(10,10,8,8,9)
        # dessin du plateau
        for i in range(self.nb) :
            for j in range(self.nb) :
                self.dessine_case(i,j,9,False)
        self.dessine_case(1,3,7)
        i,j = self.get_coord()
        # dessin du triomino avec sens = 0
        sens = 0
        for case in  self.orientation[sens] : 
            delta_i, delta_j = case
            i_case = i + delta_i
            j_case = j + delta_j
            self.dessine_case(i_case,j_case,5)
        
        
            
        
        
App(2)