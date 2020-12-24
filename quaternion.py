"""
# Quaternions

## Purpose
Quaternion library. I know that SciPy has one, but I have always wanted to make my own.

## TODO

"""


import numpy as np
import math


class Quaternion(object):
    def __init__(self, a, b, c, d):
        self.q = np.array([a, b, c, d], dtype=float)

    # ============================== MATHEMATICS ============================== #
    def __add__(self, other):
        """
        q + p or q + n
        :param other:
        :return:
        """
        if isinstance(other, Quaternion):
            return Quaternion(*(self.q + other.q))
        elif isinstance(other, (int, float, np.ndarray)):
            ans = self.q[0] + other, self.q[1], self.q[2], self.q[3]
            return Quaternion(*ans)
        else:
            raise TypeError

    def __radd__(self, other):
        """
        n + p
        :param other:
        :return:
        """
        if isinstance(other, Quaternion):
            return Quaternion(*(self.q + other.q))
        elif isinstance(other, (int, float, np.ndarray)):
            ans = self.q[0] + other, self.q[1], self.q[2], self.q[3]
            return Quaternion(*ans)
        else:
            raise TypeError

    def __iadd__(self, other):
        """
        q += p
        :param other:
        :return:
        """
        if isinstance(other, Quaternion):
            self.q += other.q
            return self
        elif isinstance(other, (int, float, np.ndarray)):
            self.q[0] += other
            return self
        else:
            raise TypeError

    def __sub__(self, other):
        """
         q - p
        :param other:
        :return:
        """
        if isinstance(other, Quaternion):
            return Quaternion(*(self.q - other.q))
        elif isinstance(other, (int, float, np.ndarray)):
            ans = self.q[0]-other, self.q[1], self.q[2], self.q[3]
            return Quaternion(*ans)
        else:
            raise TypeError

    def __isub__(self, other):
        """
        q -= p
        :param other:
        :return:
        """
        if isinstance(other, Quaternion):
            self.q -= other.q
            return self
        elif isinstance(other, (int, float, np.ndarray)):
            self.q[0] -= other
            return self
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, Quaternion):
            a1, b1, c1, d1 = self.q
            a2, b2, c2, d2 = other.q
            a = a1*a2 - b1*b2 - c1*c2 - d1*d2
            b = a1*b2 + b1*a2 + c1*d2 - d1*c2
            c = a1*c2 - b2*d2 + c1*a2 + d1*b2
            d = a1*d2 + b1*c2 - c1*b2 + d1*a2
            return Quaternion(a, b, c, d)
        elif isinstance(other, (int, float, np.ndarray)):
            return Quaternion(*(self.q * other))
        else:
            raise TypeError

    def __imul__(self, other):
        """
        q *= p or p *= n
        :param other:
        :return:
        """
        if isinstance(other, Quaternion):
            a1, b1, c1, d1 = self.q
            a2, b2, c2, d2 = other.q
            a = a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2
            b = a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2
            c = a1 * c2 - b2 * d2 + c1 * a2 + d1 * b2
            d = a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2
            self.q = a, b, c, d
            return self
        elif isinstance(other, (int, float, np.ndarray)):
            self.q *= other
            return self
        else:
            raise TypeError

    def __rmul__(self, other):
        """
        n * q
        :param other:
        :return:
        """
        return Quaternion(*other*self.q)

    def __truediv__(self, other):
        """
        q / n
        :param other:
        :return:
        """
        assert isinstance(other, (int, float, np.ndarray))
        return Quaternion(*self.q/other)

    def __idiv__(self, other):
        """
        q /= n
        :param other:
        :return:
        """
        assert isinstance(other, (int, float, np.ndarray))
        self.q /= other
        return self

    def __neg__(self):
        """
        -q
        :return:
        """
        return Quaternion(*-self.q)

    def __pos__(self):
        """
        +q
        :return:
        """
        return Quaternion(*self.q)

    # ============================== RELATIONSHIPS ============================== #
    def __eq__(self, other):
        """
        q == p
        :param other:
        :return:
        """
        return self.q == other.q

    def __ne__(self, other):
        """
        q != p
        :param other:
        :return:
        """
        return self.q != other.q

    # ============================== MORE COMPLEX MATH ============================== #

    def norm(self):
        """
        Find the norm of q (i.e. q = |q| = sqrt(a^2 + b^2 + c^2 + d^2)
        :return: float - norm of q = |q|
        """
        return np.linalg.norm(self.q)

    def normalized(self):
        """
        Find the normalized vector of q (i.e. q/|q|)
        :return: Quaternion - normalized q = q/|q|
        """
        norm = self.norm()
        if norm == 0:
            raise ZeroDivisionError
        ans = self.q / norm
        return Quaternion(*ans)

    def normalize(self):
        """
        Normalize q (i.e. |q| = sqrt(a^2 + b^2 + c^2 + d^2)
        :return: None
        """
        norm = self.norm()
        if norm == 0:
            raise ZeroDivisionError
        self.q /= norm
        return

    def conjugated(self):
        """
        Find the conjugate of q (i.e. q* = a - bi - cj - dk, where q = a + bi + cj + dk)
        :return: Quaternion - conjugate of q = q*
        """
        ans = self.q * np.array([1, -1, -1, -1])
        return Quaternion(*ans)

    def conjugate(self):
        """
        Conjugate q (i.e. q* = a - bi - cj - dk, where q = a + bi + cj + dk)
        :return: None
        """
        self.q *= np.array([1, -1, -1, -1])
        return

    def inverse(self):
        """
        Find the inverse of q (i.e. q^-1 = q*/|q|^2)
        :return: Quaternion - inverse of q = q^-1
        """
        norm = self.norm()
        if norm == 0:
            raise ZeroDivisionError
        ans = self.conjugated().q / norm**2
        return Quaternion(*ans)

    def invert(self):
        """
        Invert q (i.e. q^-1 = q*/|q|^2)
        :return: None
        """
        norm = self.norm()
        if norm == 0:
            raise ZeroDivisionError
        self.conjugate()
        self.q /= norm**2
        return

    # ============================== ROTATION ============================== #
    def rotate(self, axis, angle):
        """
        **UNTESTED... so is ADD, IADD, SUB, ISUB, etc.**
        p' = qpq^-1
        :param axis: Quaternion - normalized axis about which we rotate, we turn it into q
        :param angle: float - angle by which we rotate (Right-Hand-Rule)
        :return: Quaternion - rotated quaternion, p'
        """
        q = math.cos(angle/2) + math.sin(angle/2) * axis.normalize()
        p = q * self * q.inverse()
        self = p
        return p

    # ============================== DISPLAY ============================== #
    def __getitem__(self, item):
        """
        Get q[n] where q = (a, b, c, d)
        :param item: int - index
        :return: float - value of q at index
        """
        return self.q[item]

    def __str__(self):
        """
        Print quaternion in form 'a + b i + c j + d k'
        :return: str - form of mathematical expression
        """
        a, b, c, d = self.q
        return f'{a} + {b} i + {c} j + {d} k'


if __name__ == '__main__':
    q = Quaternion(1, 2, 3, 5)
    p = Quaternion(1, 2, 3, 4)
    a = q + p
    b = q * p

