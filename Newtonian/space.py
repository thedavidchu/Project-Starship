import numpy as np


class Space:
    def __init__(self, x, y, z):
        self.space = np.array([x, y, z], dtype=float)

    def __str__(self):
        x, y, z = self.space
        return f'Space(x={x}, y={y}, z={z})'

    def __repr__(self):
        return self.__str__()

    def __iadd__(self, other):
        self.space += other.space
        return self

    def __radd__(self, other_scalar):
        """
        ## Inputs
        other: int
        """
        return Space(*(self.space + other_scalar))

    def __add__(self, other_space):
        space = self.space + other_space.space
        return Space(*space)

    def __neg__(self):
        return Space(*-self.space)

    def __sub__(self, other_space):
        space = self.space - other_space.space
        return Space(*space)

    def __mul__(self, other_scalar):
        space = self.space * other_scalar
        return Space(*space)

    def __truediv__(self, other_scalar):
        space = self.space / other_scalar
        return Space(*space)

    @staticmethod
    def mean(*args):
        return sum(map(lambda x: x.space, args)) / len(args)


class Force(Space):
    def __init__(self, x, y, z):
        super(Force, self).__init__(x, y, z)

    def __str__(self):
        x, y, z = self.space
        return f'Force(F_x={x}, F_y={y}, F_z={z})'


class Acceleration(Space):
    def __init__(self, x, y, z):
        super(Acceleration, self).__init__(x, y, z)

    def __str__(self):
        x, y, z = self.space
        return f'Acceleration(x"={x}, y"={y}, z"={z}'


class Velocity(Space):
    def __init__(self, x, y, z):
        super(Velocity, self).__init__(x, y, z)

    def __str__(self):
        x, y, z = self.space
        return f'Velocity(x\'={x}, y\'={y}, z\'={z})'

    def __accelerate(self, acceleration):
        self += acceleration


class Position(Space):
    def __init__(self, x, y, z):
        super(Position, self).__init__(x, y, z)

    def __str__(self):
        x, y, z = self.space
        return f'Position(x={x}, y={y}, z={z})'


class Mass(float):
    def __str__(self):
        return f'Mass(mass={float(self)})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def sum(*args):
        return sum(args)


class Object:
    def __init__(self, mass, x, y, z, u, v, w):
        self.mass = Mass(mass)
        self.position = Position(x, y, z)
        self.velocity = Velocity(u, v, w)

    def __str__(self):
        return f'Object(mass={self.mass}, position={self.position}, velocity={self.velocity})'

    def change_mass(self, dm: Mass):
        self.mass += dm

    def force(self, force: Force):
        """Apply a constant force for time interval"""
        acceleration = force / self.mass

    @staticmethod
    def centre_of_mass(*args):
        return sum(map(lambda x: x.position * x.mass, args)) / Mass.sum(*args)


if __name__ == '__main__':
    a = Object(10, 0, 1, -1, 0, -1, 1)
    b = Object(5, 0, 0, 0, 0, 0, 0)

    cm = Object.centre_of_mass(a, b)
    # Expected (0, 0.67, -0.67)
    print(f'Centre of Mass: {cm}')
    print(a, b)



