# Découverte de pyxel
* Un premier exemple
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
