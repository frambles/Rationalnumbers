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
        if type(other) is int:
            other = Rational(other, 1)
            top = self.numer * other.denom + other.numer * self.denom
            bottom = self.denom * other.denom
        else:
            top = self.numer * other.denom + other.numer * self.denom
            bottom = self.denom * other.denom

        return Rational(top, bottom)

    def __neg__(self):
        return Rational(-self.numer, self.denom)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        if type(other) is int:
            other = Rational(other, 1)
        return Rational((self.numer * other.numer), (self.denom * other.denom))

    def __invert__(self):
        return Rational(self.denom, self.numer)

    def __truediv__(self, other):
        if type(other) is Rational:
            return self * ~other
        else:
            return self * Rational(1, other)

    def __float__(self):
        return float(self.numer / self.denom)

    def __pow__(self, power, modulo=None):
        return Rational(self.numer ** power, self.denom ** power)

    def __abs__(self):
        return Rational(abs(self.numer), self.denom)

    def __radd__(other, self):
        return other + self

    def __rsub__(other, self):
        return other - self

    def __rmul__(other, self):
        return other * self

    def __rtruediv__(other, self):
        return self * ~other

    def __rpow__(self, base):
        return (base ** (1 / self.denom)) ** self.numer

    def __eq__(self, other):
        if float(self) == float(other):
            return bool(1)
        else:
            return bool(0)

    def __ne__(self, other):
        if float(self) != float(other):
            return bool(1)
        else:
            return bool(0)

    def __lt__(self, other):
        if float(self) < float(other):
            return bool(1)
        else:
            return bool(0)

    def __gt__(self, other):
        if float(self) > float(other):
            return bool(1)
        else:
            return bool(0)

    def __le__(self, other):
        if float(self) <= float(other):
            return bool(1)
        else:
            return bool(0)

    def __ge__(self, other):
        if float(self) >= float(other):
            return bool(1)
        else:
            return bool(0)

    def from_float(flo):
        if type is float:
            return
        else:
            pass


def main():
    myrat = Rational(1, 2)
    yourrat = Rational(2, 2)
    print(myrat <= yourrat)


if __name__ == '__main__':
    main()
