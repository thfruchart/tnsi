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
