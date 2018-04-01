class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs
        
    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        if isinstance(other, Polynomial):
            return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))
        else:
            return Polynomial(*self.coeffs)

    def __len__(self):
        return len(self.coeffs) - 1