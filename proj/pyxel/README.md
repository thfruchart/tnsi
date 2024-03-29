# Découverte de pyxel
## A. Un premier exemple
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
* A.1. Exécuter le code exemple avec Edupyter-Thonny
  * modifier certaines des valeurs numériques, et comprendre le rôle de chaque paramètre, en s'aidant de la documentation.
* A.2. Mêmes consignes avec le code suivant :

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
#### A.3. images
Pyxel permet de manipuler des images.
* pour cela, un fichier ressource doit être chargé
  * l'usage est d'enregistrer la ressource et le code dans le même répertoire.
  * dans l'exemple suivant, la ressource est : `test.pyxres`
  * [test.pyxres](test.pyxres)
* on peut visualiser (et éditer) la ressource de la manière suivante :
  * dans le menu de Tonny : Outils/Ouvrir la console du système
  * dans la console : `pyxel edit test.pyxres`
* tester et adapter le code suivant :
```python
import pyxel

DELAI = 5

class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("test.pyxres")
        self.x = 0
        self.y = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.frame_count % DELAI == 0 :
            self.x = (self.x + 1) % pyxel.width
            self.y = (self.y + 2) % pyxel.height
        
    def draw(self):
        pyxel.cls(0)
        x_img,y_img,w_img,h_img = 8,0,8,16
        pyxel.blt(self.x, self.y,0,x_img,y_img,w_img,h_img)

App()

```

## B. Exemple : "serpent"

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
#### B.1. tester le code ci-dessus
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

#### B.2. en vous aidant du code ci-dessus, compléter la méthode `update` afin que le serpent de déplace dans les quatre directions (sans grandir à chaque étape)

#### B.3 Compléter votre code pour :
1. empêcher le serpent de "sortir" de la fenêtre : si c'est le cas, la partie est perdue.
    * on peut utiliser `pyxel.quit()` pour mettre fin au jeu
    * une autre possibilité est de créer un booléen `gameover` pour mettre fin à la partie, en contrôlant l'affichage de fin de partie, ce qui permet de créer un menu du type "voulez-vous rejouer?"... 
2. créer une pomme, que le serpent pourra "manger"
   * lors de la création, la pomme est 'en dehors' du serpent
   * si la tête du serpent est au même lieu que la pomme, le serpent "mange" la pomme : celle-ci disparaît, et le serpent grandit d'une unité.
   * un nouvelle pomme est générée à un autre endroit (en dehors du serpent)
3. créer une variable score :
   * chaque fois que le serpent mange la pomme, le score augmente de 1.
   * le serpent ne doit pas se "manger" lui-même, sinon la partie est perdue : ajouter cette contrainte au jeu.
   * prévoir un affichage du score, pendant la partie et en fin de partie
   * prévoir la possibilité de rejouer
4. Améliorer l'affichage, avec des images du fichier ressource  [`monfichier.pyxres`](monfichier.pyxres) que vous pourrez modifier si besoin.
