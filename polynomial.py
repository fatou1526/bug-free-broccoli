from cmath import sqrt
import matplotlib.pyplot as plt  # type:ignore


class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""

    def __init__(self, *coeffs):
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        assert isinstance(coeffs, list), " Donnez une liste des coefficients, pas %r!" %type(coeffs)  #verifie qu'on a bien une liste
        
        self.coeff2 = coeffs[0]        # self.coeff2 est le coefficient du parametre de degré 2
        self.coeff1 = coeffs[1]        # self.coeff1 est le coefficient du parametre de degré 1
        self.coeff0 = coeffs[2]        # self.coeff0 est le coefficient du parametre de degré 0

    def __add__(self, other):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""
        self.coeff2 = self.coeff2 + other.coeff2
        self.coeff1 = self.coeff1 + other.coeff1
        self.coeff0 = self.coeff0 + other.coeff0
        if self.coeff2 < 0:
            coeff2 = f"{self.coeff2}"
        else:
            coeff2 = f"{self.coeff2}"
        if self.coeff1 < 0:
            coeff1 = f"{self.coeff1}"
        else:
            coeff1 = f"+{self.coeff1}"
        if self.coeff0 < 0:
            coeff0 = f"{self.coeff0}"
        else:
            coeff0 = f"+{self.coeff0}"
        polynome_somme = f"{self.coeff2}X^2+{self.coeff1}X+{self.coeff0}"
        return polynome_somme
    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""
        self.coeff2 = self.coeff2 - other.coeff2
        self.coeff1 = self.coeff1 - other.coeff1
        self.coeff0 = self.coeff0 - other.coeff0
        if self.coeff2 < 0:
            coeff2 = f"{self.coeff2}"
        else:
            coeff2 = f"{self.coeff2}"
        if self.coeff1 < 0:
            coeff1 = f"{self.coeff1}"
        else:
            coeff1 = f"+{self.coeff1}"
        if self.coeff0 < 0:
            coeff0 = f"{self.coeff0}"
        else:
            coeff0 = f"+{self.coeff0}"
        polynome_sous = f"{self.coeff2}X^2+{self.coeff1}X+{self.coeff0}"
        return polynome_sous

    def __repr__(self):
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs.values())]) + ')'
        return msg

    def __str__(self):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """
        if self.coeff2 < 0:
            coeff2 = f"{self.coeff2}"
        else:
            coeff2 = f"{self.coeff2}"
        if self.coeff1 < 0:
            coeff1 = f"{self.coeff1}"
        else:
            coeff1 = f"+{self.coeff1}"
        if self.coeff0 < 0:
            coeff0 = f"{self.coeff0}"
        else:
            coeff0 = f"+{self.coeff0}"
        chaine_polynome = f"{coeff2}X^2 {coeff1}X {coeff0}"
        return chaine_polynome

    def solve(self):
        """ Méthode qui renvoie les solutions si elles existent."""
        delta = self.coeff1**2 - 4*self.coeff2*self.coeff0
        if delta == 0:
            print("on a une solution unique")
            res = (-self.coeff1)/(2*self.coeff2)
            return f"La solution unique est {res}"
        elif delta > 0:
            print("On a une solution double")
            res1 = (-self.coeff1-sqrt(delta))/(2*self.coeff2)
            res2 = (-self.coeff1+sqrt(delta))/(2*self.coeff2)
            return f"Les deux solutions sont {res1}, {res2}"
        else:
            print("On n'a pas de solutions réelles")
            

    def __val(self, x):
        """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
        Si: y = x^2 + 1
        Si: x prend pour valeur 5
        Alors: y = 5^2 + 1 = 26
        """
        y = self.coeff2 * x**2 +self.coeff1 * x + self.coeff0
        return y

    def draw(self, x_points=None):
        """ Méthode qui trace la courbe, voir fichier png."""
        


if __name__ == "__main__":
    bar = [1, 1, 1]
    p1 = Poly2(*bar)
    print(p1)

    baz = [1, 1, 1]
    p2 = Poly2(*baz)

    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2

    print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    p1.draw()  # trace la courbe de p1, voir fichier png
