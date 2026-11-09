class Fraction:
    "Classe Fraction minimaliste"

    def __init__(self, a, b):
        "Définit la fraction a/b"
        if b == 0:
            raise ValueError("Le dénominateur b est égal à 0")
        self.num = a
        self.den = b
    
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
