from math import gcd

class Fraction:
    "Classe Fraction minimaliste"

    def __init__(self, a, b):
        "Définit la fraction a/b"
        if b == 0:
            raise ValueError("Le dénominateur b est égal à 0")
        self.num = a
        self.den = b

    def simplifie(self):
        k = gcd(self.num, self.den)
        self.num = self.num // k
        self.den = self.den // k

    def inverse(self):
        return Fraction(self.den,self.num)


# Tests

#f = Fraction(2200, 700)
#assert f.num == 2200
#assert f.den == 700
#f.simplifie()
#assert f.num == 22
#assert f.den == 7
#inv_f = f.inverse()
#assert inv_f.num == 7
#assert inv_f.den == 22

#g = Fraction(1, -3)
#g.simplifie()
#assert g.num == -1
#assert g.den == 3
#inv_g = g.inverse()
#assert inv_g.num == 3
#assert inv_g.den == -1
