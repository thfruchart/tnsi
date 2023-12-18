# Découverte de pyxel
## Un premier exemple
```python
import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.y = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        #self.x = (self.x + 1) % pyxel.width
        #self.y = (self.y + 2) % pyxel.height
        return

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, 8, 8, 9)

App()
```
* [Documentation](https://github.com/kitao/pyxel/blob/main/docs/README.fr.md#documentation-de-lapi)
* Exécuter le code exemple avec Edupyter-Thonny
  * modifier certaines des valeurs numériques, et comprendre le rôle de chaque paramètre, en s'aidant de la documentation.
* Mêmes consignes avec le code suivant :

```python
import pyxel

DELAI = 5

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.y = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.frame_count % DELAI == 0 :
            self.x = (self.x + 1) % pyxel.width
            self.y = (self.y + 2) % pyxel.height
        

    def draw(self):
        pyxel.cls(0)
        #pyxel.rect(self.x, self.y, 8, 8, 9)
        pyxel.text(self.x, self.y, "Hello",1+self.x//14)

App()

```

## Exemple : "serpent"

```python
import pyxel

DELAI = 5
LARG = 128
HAUT = 128
CASE = 8

class Snake:
    def __init__(self):
        self.coord = [(10,1),(11,1),(12,1)]
    

class App:
    def __init__(self):
        pyxel.init(LARG, HAUT)
        self.serpent = Snake()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.frame_count % DELAI == 0 :
            return
        

    def draw(self):
        pyxel.cls(0)
        for i in range(len(self.serpent.coord)):
            element = self.serpent.coord[i]
            if i == 0:
                couleur = 9
            else :
                couleur = 11
            x, y = element
            pyxel.rect(x*CASE, y*CASE, CASE, CASE, couleur)
                
        #pyxel.rect(self.x, self.y, 8, 8, 9)
        

App()

```
* tester le code ci-dessus
* compléter la méthode `update` afin que le serpent de déplace dans les quatre directions (sans grandir à chaque étape)

```python
import pyxel

DELAI = 10
LARG = 128
HAUT = 128
CASE = 8
VECT_DIR = {'Haut':(0,-1), 'Bas':(0,1), 'Gauche':(-1,0), 'Droite':(1,0)}

class Snake:
    def __init__(self):
        self.coord = [(10,1),(11,1),(12,1)]
        self.direction = 'Gauche'

class App:
    def __init__(self):
        pyxel.init(LARG, HAUT)
        self.serpent = Snake()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_DOWN) :
            self.serpent.direction = 'Bas'
        if pyxel.frame_count % DELAI == 0 :
            #coordonnée du premier élément du serpent
            x,y = self.serpent.coord[0]
            #coordonnées du déplacement
            u,v = VECT_DIR[self.serpent.direction]
            #nouvelles coordonnées
            tete = (x+u, y+v)
            #ajout en tete du serpent
            self.serpent.coord = [tete] + self.serpent.coord
            
    def draw(self):
        pyxel.cls(0)
        for i in range(len(self.serpent.coord)):
            element = self.serpent.coord[i]
            if i == 0:
                couleur = 9
            else :
                couleur = 11
            x, y = element
            pyxel.rect(x*CASE, y*CASE, CASE, CASE, couleur)         
        
App()
```

Compléter votre code pour :
1. empêcher le serpent de "sortir" de la fenêtre : si c'est le cas, la partie est perdue.
2. 
