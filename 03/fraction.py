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
        if self.den<0 : 
            self.num *= (-1)
            self.den *= (-1)
        return self
    
    def inverse(self):
        return Fraction(self.den,self.num)
    
    def __eq__(self, autre):
        "Test d'égalité, renvoie un booléen"
        return self.num * autre.den == self.den * autre.num 
    
    def __str__(self):
        "Affichage à destination de l'utilisateur"
        return str(self.num) + " / " + str(self.den)
        
    def __repr__(self) : 
        "Affichage à destination du programmeur"
        return "Fraction(" + str(self.num)+ ", "  + str(self.den) + ")"

    def __pos__(self) : 
        return Fraction(self.num, self.den)

    def __neg__(self) : 
        return Fraction( - self.num, self.den)
        
    def __add__(self, autre):
        a, b = self.num, self.den
        c, d = autre.num, autre.den
        return Fraction(a*d + c*b, b*d)
    
    def __sub__(self, autre):
        return self + (- autre)
        
    def __lt__(self, autre):
        a, b = self.num, self.den
        c, d = autre.num, autre.den
        return (a*d-b*c) *(b*d) < 0
    
    def __le__(self, autre):
        return self < autre or self == autre
    
    def __gt__(self, autre):
        return autre < self
    
    def __ge__(self, autre):
        return self > autre or self == autre
    
    def __mul__(self, autre):
        a, b = self.num, self.den
        c, d = autre.num, autre.den
        return Fraction(a*c , b*d )
    
    def __truediv__(self, autre):
        a, b = self.num, self.den
        c, d = autre.num, autre.den
        return Fraction(a*d , b*c )
    
# Tests

f = Fraction(1, 3)
g = Fraction(2, 5)
assert f == Fraction(2, 6), "Erreur avec __eq__"
assert +f == f, "Erreur avec __pos__"
assert -f == Fraction(-1, 3), "Erreur avec __neg__"
assert f + f == Fraction(2, 3), "Erreur avec __add__"
assert f + g == Fraction(11, 15), "Erreur avec __add__"
assert f - g == Fraction(-1, 15), "Erreur avec __sub__"
assert f < g, "Erreur avec __lt__"
assert f <= g, "Erreur avec __le__"
assert g > f, "Erreur avec __gt__"
assert g >= f, "Erreur avec __ge__"
assert f * g == Fraction(2, 15), "Erreur avec __mul__"
assert f / g == Fraction(5, 6), "Erreur avec __truediv__"
