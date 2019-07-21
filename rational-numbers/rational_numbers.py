from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        #Always getting to the least possible number
        (x, y) = (numer, denom)
        while y:
            (x, y) = (y, x % y)
        self.numer = numer // x
        self.denom = denom // x

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + self.denom * other.numer, self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - self.denom * other.numer, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if isinstance(power, int):
            if power > 0:
                return Rational(self.numer ** power, self.denom ** power)
            elif power < 0:
                return Rational(self.denom ** -power, self.numer ** -power)
            else:
                return Rational(1, 1)
        elif isinstance(power, float):
            return pow(self.numer / self.denom, power)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)
