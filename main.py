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


def main():
    myrat = Rational(7, 3)
    print(myrat)


if __name__ == '__main__':
   main()