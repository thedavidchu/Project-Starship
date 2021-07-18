import numpy as np


from timestep import TimeStep


class Position:
    """
    Integer position
    """
    def __init__(self, x: int, y: int, z: int):
        self.position = np.array([x, y, z], dtype=np.int32)

    # # Math
    # def __neg__(self):
    #     return Position(*(-self.position))
    #
    # def __add__(self, other):
    #     if isinstance(other, Position):
    #         return Position(*(self.position + other.position))
    #     elif isinstance(other, np.ndarray):
    #         return Position(*self.position + other)
    #     elif other == 0:
    #         return Position(*self.position)
    #     else:
    #         raise TypeError('Unsupported type!')
    #
    # def __radd__(self, other):
    #     return self.__add__(other)
    #
    # def __iadd__(self, other):
    #     if isinstance(other, Position):
    #         self.position += other.position
    #         return self
    #     elif isinstance(other, np.ndarray):
    #         self.position += other
    #         return self
    #     elif other == 0:
    #         return self
    #     else:
    #         raise TypeError('Unsupported type!')
    #
    # def __sub__(self, other):
    #     return self.__add__(-other)
    #
    # def __mul__(self, scalar):
    #     return Position(*(self.position * scalar))
    #
    # def __truediv__(self, scalar):
    #     return Position(*(self.position / scalar))

    # Equality
    def __eq__(self, other):
        return (self.position == other.position).all()

    def __ne__(self, other):
        return not self.__eq__(other)

    # String
    def __str__(self):
        return f'Position{tuple(self.position)}'

    def __repr__(self):
        return self.__str__()

    def distance(self, other=0):
        return np.linalg.norm(self.position - other)

    def move(self, displacement):
        self.position += displacement


class Velocity:
    def __init__(self, x: int, y: int, z: int):
        self.velocity = np.array([x, y, z], dtype=np.int32)

    # String
    def __str__(self):
        return f'Velocity{tuple(self.velocity)}'

    def __repr__(self):
        return self.__str__()

    def speed(self):
        return np.linalg.norm(self.velocity)

    def accelerate(self, acceleration):
        self.velocity += acceleration


class Mass(TimeStep):
    def __init__(self, position: np.ndarray, velocity: np.ndarray, mass: int):
        # super(Mass, self).__init__(*position)
        # super(Mass, self).__init__(*velocity)
        self.position = Position(*position)
        self.velocity = Velocity(*velocity)
        self.mass = np.ndarray(mass, dtype=np.int32)

    def force(self, force):
        # TimeStep dt??
        # Force is a float?
        acceleration = force / self.mass
        self.add_action(self.velocity.accelerate, (acceleration,))
        self.add_action(self.position.move, (self.velocity,))




if __name__ == '__main__':
    a = Position(1, 2, 3)
    b = Position(1., 2., 3.)

    print(a == b)
    print(a + b)
    a += b
    print(a - b)
    print(a * 5)
    print(a * 5.6)
    print(a / 3)
    print(a != b)

    c = Mass(1, 2, 3, 4)