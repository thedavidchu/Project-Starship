"""
# starship.py

## Contents
Contains the class call for a generic starship.

## Functionality
Dictate the statistics of a starship. These include:
- Mass
- Thrust
-
"""

import numpy as np
from engine import Engine
from fuel_tank import FuelTank

class Starship(object):
    def __init__(self):
        """
        """
        # Statistics
        self.max_health = 100                               # Hull
        self.fuel_tank = FuelTank()                         # Fuel Tank
        self.engine = Engine()                              # Engine
        self.dry_mass = self.fuel_tank.dry_mass + self.engine.dry_mass

        self.rotational_inertia = [100, 100, 100]   # Rotation
        self.max_torque = [100, 100, 100]

        # Translational coordinates
        self.position, self.velocity, self.acceleration = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.thrust = np.array([0, 0, 0])

        # Rotational Coordinates
        # N.B. Implement with quaternions
        self.angular_position, self.angular_velocity, self.angular_acceleration = np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.torque = [0, 0, 0]

    # ============================== MOVEMENT ============================== #
    def accelerate(self, thrust=None):
        """
        **Not implemented yet**
        Change acceleration.

        N.B. This function does not move the starship or burn fuel.
        :param thrust:
        :return:
        """
        return

    def angular_accelerate(self):
        """
        **Not implemented yet**
        Change angular acceleration.

        N.B. This function does not move the starship or burn fuel.
        :return:
        """
        return

    def step(self, dt):
        """
        Advance one time step.

        N.B. Take average?

        :param dt:
        :return:
        """
        # Translation
        # Check if we can maintain acceleration
        """
        1. Query fuel use
        2. With fuel, attempt to accelerate
        3. Acceleration = F/m * rotation
        4. Update fuel levels
        """

        # Update position and velocity (take average between time steps?)
        self.position += 1/2*self.acceleration*dt**2 + self.velocity*dt
        self.velocity += self.acceleration*dt

        # Rotation
        self.angular_position += 0
        self.angular_velocity += 0



    # ============================== RETURNS ============================== #
    def health(self):
        return self.health

    def coordinates(self):
        return self.position


if __name__ == '__main__':
    a = Starship()