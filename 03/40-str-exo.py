class Fraction:
    "Classe Fraction minimaliste"

    def __init__(self, a, b):
        "Définit la fraction a/b"
        if b == 0:
            raise ValueError("Le dénominateur b est égal à 0")
        self.num = a
        self.den = b
    
    def __str__(self):
        "Affichage à destination de l'utilisateur"
        return str(self.num) + " / " + str(self.den)


# Tests

#f = Fraction(22, 7)
#assert str(f) == '22 / 7'

#g = Fraction(-1, 3)
#assert str(g) == '-1 / 3'
