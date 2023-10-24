from math import gcd


class Rational:
    def __init__(self, numer, denom):
        if type(numer) is not int:
            raise ValueError("Numerator must be an integer.")
        if type(denom) is not int:
            raise ValueError("Denominator must be an integer.")
        if denom != 0:
            self.numer = numer
            self.denom = denom
            self.simplify()
        else:
            raise ValueError("Cannot create ratio with zero denominator.")

    def __str__(self):
        if self.denom == 1:
            return f"{self.numer}"
        else:
            return f"{self.numer}/{self.denom}"

    def simplify(self):
        if self.numer == 0:
            self.denom = 1
        else:
            divisor = gcd(self.numer, self.denom)
            self.numer //= divisor
            self.denom //= divisor
            if self.denom < 0:
                self.numer *= -1
                self.denom *= -1

    def __add__(self, other):
        top = self.numer * other.denom + other.numer * self.denom
        bottom = self.denom * other.denom

        return Rational(top, bottom)

    def __neg__(self):
        return Rational(-self.numer, self.denom)

    def __sub__(self, other):
        return self + -other


def main():
    myrat = Rational(2, 5)
    yourrat = Rational(1, 5)
    print(myrat - yourrat)


if __name__ == '__main__':
    main()
