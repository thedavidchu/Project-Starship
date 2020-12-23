import numpy as np


class Quaternion(object):
    def __init__(self, a, b, c, d):
        self.q = np.array([a, b, c, d], dtype=float)

    # ============================== MATHEMATICS ============================== #
    def __add__(self, other):
        return Quaternion(*(self.q + other.q))

    def __sub__(self, other):
        return Quaternion(*(self.q - other.q))

    def __mul__(self, other):
        a1, b1, c1, d1 = self.q
        a2, b2, c2, d2 = other.q
        a = a1*a2 - b1*b2 - c1*c2 - d1*d2
        b = a1*b2 + b1*a2 + c1*d2 - d1*c2
        c = a1*c2 - b2*d2 + c1*a2 + d1*b2
        d = a1*d2 + b1*c2 - c1*b2 + d1*a2
        return Quaternion(a, b, c, d)

    def __rmul__(self, other):
        return Quaternion(*other*self.q)

    def __truediv__(self, other):
        assert isinstance(other, (int, float, np.ndarray))
        return Quaternion(*self.q/other)

    def __neg__(self):
        return Quaternion(*-self.q)

    def __pos__(self):
        return Quaternion(*self.q)

    # ============================== MORE COMPLEX MATH ============================== #

    def norm(self):
        return np.linalg.norm(self.q)

    def normalize(self):
        norm = self.norm()
        if norm == 0:
            raise ZeroDivisionError
        self.q /= norm
        return

    def conjugated(self):
        ans = self.q * np.array([1, -1, -1, -1])
        return Quaternion(*ans)

    def conjugate(self):
        self.q *= np.array([1, -1, -1, -1])
        return

    def inverse(self):
        norm = self.norm()
        if norm == 0:
            raise ZeroDivisionError
        ans = self.conjugated().q / norm**2
        return Quaternion(*ans)

    def invert(self):
        norm = self.norm()
        if norm == 0:
            raise ZeroDivisionError
        self.conjugate()
        self.q /= norm**2
        return

    # ============================== DISPLAY ============================== #

    def __str__(self):
        a, b, c, d = self.q
        return f'{a} + {b} i + {c} j + {d} k'


if __name__ == '__main__':
    q = Quaternion(1,2,3,5)
    p = Quaternion(1,2,3,4)
    a = q + p
    b = q * p

