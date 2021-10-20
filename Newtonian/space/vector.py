"""
# An N-Dimensional Vector

## TODO
- Continue testing
    - Scalars for all
    - reverse and in-place all
"""


def repeat(value):
    """
    A simplified version of `repeat` from `itertools`.

    Returns the `value` upon each loop of the iteration.
    """
    while True:
        yield value


class Vector:
    """ Create an N-dimensional vector of floats. """
    def __init__(self, *args):
        self._vector = list(map(float, args))    # All must be convertible to float

    def __len__(self):
        """ Returns dimension of the Vector rather than the magnitude. """
        return len(self._vector)

    def __str__(self):
        return f"<{', '.join(map(str, self._vector))}>"

    def __repr__(self):
        return str(self)

    # Iterating over
    def __contains__(self, item):
        return item in self._vector

    def __getitem__(self, item):
        if isinstance(item, int):
            if item >= len(self):
                raise IndexError("index out of bounds")
            return self._vector[item]
        elif isinstance(item, slice):
            return self._vector[item]
        else:
            # Numpy-like and slicing indexing not yet supported
            raise TypeError("other types of indices not implemented yet")

    def __setitem__(self, key, value):
        if isinstance(key, int):
            if key >= len(self):
                raise IndexError("index out of bounds")
            self._vector[key] = float(value)
        elif isinstance(key, slice):
            self._vector[key] = map(float, value)
        else:
            # Numpy-like and slicing indexing not yet supported
            raise TypeError("other types of indices not implemented yet")

    def __iter__(self):
        """ __iter__ and __next__ to allow iterating through. """
        self._idx = 0
        return self

    def __next__(self):
        """ __iter__ and __next__ to allow iterating through. """
        if self._idx < len(self):
            val = self[self._idx]
            self._idx += 1
            return val
        else:
            raise StopIteration

    # Equality
    def __eq__(self, other):
        """ TODO(dchu): test <1, 1> == <1, 1, 0>"""
        if not Vector._is_vector(other):
            return False
        elif not self._same_len(other):
            return False
        return all(map(lambda elem: elem[0] == elem[1], zip(self, other)))

    def __ne__(self, other):
        return not (self == other)

    @classmethod
    def _is_vector(cls, other):
        """
        Determines if the other is a vector.

        TODO(dchu): test with inheritance.
        """
        return isinstance(other, cls)

    @classmethod
    def _is_scalar(cls, other, scalar_types: tuple = (int, float)):
        return isinstance(other, scalar_types)

    def _same_len(self, other):
        return len(self) == len(other)

    def _assert_valid_vector(self, other):
        """ Assert the other is a Vector with matching dimensions. """
        if not Vector._is_vector(other):
            raise TypeError("other is not a vector type")
        elif not self._same_len(other):
            raise ValueError("mismatched vector dimensions")

    @classmethod
    def _is_zero(cls, other):
        if Vector._is_vector(other):
            return 0 in other
        elif Vector._is_scalar(other):
            return other == 0
        else:
            raise TypeError("other is not a vector type")

    @classmethod
    def _assert_non_zero(cls, other):
        if cls._is_zero(other):
            raise ZeroDivisionError("uh-oh! spaghettio! division by zero!")

    def __pos__(self):
        return Vector(*self)

    def __neg__(self):
        return Vector(*map(lambda elem: -elem, self))

    def __abs__(self):
        return Vector(*map(abs, self))

    def _bin_op(self, elem_op, other):
        """ Applies an element-wise function to each of the elements. """
        if Vector._is_vector(other):
            if self._same_len(other):
                return map(elem_op, zip(self, other))
            else:
                raise ValueError("mismatching vector lengths")
        elif Vector._is_scalar(other):
            # repeat(value) = [value, value, value, ...]
            return map(elem_op, zip(self, repeat(other)))
        else:
            raise TypeError("other types not implemented yet")

    def __add__(self, other):
        return Vector(*self._bin_op(lambda elem: elem[0] + elem[1], other))

    def __sub__(self, other):
        return Vector(*self._bin_op(lambda elem: elem[0] - elem[1], other))

    def __mul__(self, other):
        return Vector(*self._bin_op(lambda elem: elem[0] * elem[1], other))

    def __matmul__(self, other):
        self._assert_valid_vector(other)
        return sum(self * other)

    def __truediv__(self, other):
        Vector._assert_non_zero(other)
        return Vector(*self._bin_op(lambda elem: elem[0] / elem[1], other))

    def __pow__(self, power, modulo=None):
        return Vector(*self._bin_op(lambda elem: elem[0] ** elem[1], power))

    # Reverse functions
    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        """ Non-commutative. """
        return -self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        """ Non-commutative. """
        Vector._assert_non_zero(self)
        return Vector(*map(lambda elem: other / elem, self))

    def __rpow__(self, other):
        """ Non-commutative. """
        return Vector(*map(lambda elem: other ** elem, self))

    # In-place functions
    def __iadd__(self, other):
        self._vector = list(self._bin_op(lambda elem: elem[0] + elem[1], other))
        return self

    def __isub__(self, other):
        self._vector = list(self._bin_op(lambda elem: elem[0] - elem[1], other))
        return self

    def __imul__(self, other):
        self._vector = list(self._bin_op(lambda elem: elem[0] * elem[1], other))
        return self

    def __itruediv__(self, other):
        if Vector._is_vector(other) and 0 in other:
            raise ZeroDivisionError("uh-oh! spaghettio")
        elif other == 0:
            raise ZeroDivisionError("uh-oh! spaghettio")
        self._vector = list(self._bin_op(lambda elem: elem[0] / elem[1], other))
        return self

    def __ipow__(self, other):
        self._vector = list(self._bin_op(lambda elem: elem[0] ** elem[1], other))
        return self


if __name__ == '__main__':
    x, y, z = Vector(1, 0, 0), Vector(0, 1, 0), Vector(0, 0, 1)

    # Test len, str, repr
    assert all(map(lambda vec: len(vec) == 3, [x, y, z]))
    print(f"Expected: [<1.0, 0.0, 0.0>, <0.0, 1.0, 0.0>, <0.0, 0.0, 1.0>]. Got {[x, y, z]}")
    print("**********")

    # Test contains, getitem, setitem, iter, next
    assert all(map(lambda vec: 0 in vec and 1 in vec, [x, y, z]))
    print(f"Expected: (1.0, 0.0, 0.0). Got: {x[0], x[1], x[2]}")
    x[0], x[1], x[2] = 5, 4, 3
    print(f"Expected: (5.0, 4.0, 3.0). Got: {x[0], x[1], x[2]}")
    print(f"Expected: [10.0, 8.0, 6.0]. Got: {[2 * elem for elem in x]}")
    x[:] = 1, 0, 0
    print(f"Expected: [1.0, 0.0, 0.0]. Got: {x[:]}")
    print("**********")

    # Test eq, ne
    assert x == Vector(1, 0, 0) and y == Vector(0, 1, 0) and z == Vector(0, 0, 1)
    assert x != Vector(1, 0, 0, 0) and x != Vector(0, 0, 0) and x != y and x != 0 and x != "<1.0, 0.0, 0.0>"
    print("**********")

    # Test pos, neg, abs
    print(f"Expected: <1.0, 0.0, 0.0>. Got: {+x}")
    print(f"Expected: <-1.0, 0.0, 0.0>. Got: {-x}")
    print(f"Expected: <1.0, 0.0, 0.0>. Got: {abs(-x)}")
    print("**********")

    # Test add, sub, mul, matmul, div, pow
    a, b, c = Vector(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9)
    print(f"Expected: <5.0, 7.0, 9.0>. Got: {a + b}")
    print(f"Expected: <0.0, -2.0, -3.0>. Got: {x - a}")
    print(f"Expected: <4.0, 10.0, 18.0>. Got: {a * b}")
    print(f"Expected: 32.0. Got: {a @ b}")
    print(f"Expected: <0.25, 0.4, 0.5>. Got: {a / b}")
    print(f"Expected: <1.0, 32.0, 720.0>. Got: {a ** b}")
    print("**********")

    # TODO(dchu): continue
