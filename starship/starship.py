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
import matplotlib.pyplot as plt
import warnings
from .engine import Engine
from .fuel_tank import FuelTank


class Starship(object):
    def __init__(self):
        """
        """
        # Statistics
        self.max_health = 100                               # Hull
        self.fuel_tank = FuelTank()                         # Fuel Tank
        self.engine = Engine(energy_density=1)              # Engine
        self.angular_engine = Engine(energy_density=1)
        self.dry_mass = self.fuel_tank.dry_mass + self.engine.dry_mass

        self.rotational_inertia = [100, 100, 100]   # Rotation
        self.max_torque = [100, 100, 100]

        # Translational coordinates
        self.position, self.velocity, self.acceleration = np.array([[0, 0, 0],
                                                                    [0, 1, 0],
                                                                    [0, 0, 0]],
                                                                   dtype=np.float64)
        self.thrust = 0
        self.fuel_burn = 0          # Fuel consumption [kg] - not the best name

        # Rotational Coordinates
        # N.B. Implement with quaternions
        self.angular_position, self.angular_velocity, self.angular_acceleration = np.array([[1, 0, 0],
                                                                                            [0, 0, 0],
                                                                                            [0, 0, 0]],
                                                                                           dtype=np.float64)
        self.angular_thrust = 0     # ??? Do we need this?
        self.angular_fuel_burn = 0                                          # Fuel consumption [kg] - not the best name
        self.angular_torque = [1, 1, 1] * self.angular_thrust               # Multiply by lever arm

        # Record
        self.record_position = []
        self.record_velocity = []
        self.record_acceleration = []

    # ============================== MOVEMENT ============================== #
    def accelerate(self, fuel: int = 1, dt: float = 1):
        """
        Change acceleration.

        N.B. This function does not move the starship or burn fuel.
        It is the command to accelerate in the next time step.

        :param fuel: float - fuel to be injected
        :param dt: float - time step
        :return: None
        """

        # Undo any previous acceleration
        self.fuel_burn = 0

        # Check if allowable fuel consumption
        fuel_tank_limit = self.fuel_tank.max_fuel_use(dt=dt) - self.angular_fuel_burn
        engine_limit = self.engine.get_fuel_limit(dt=dt)
        limit = min(fuel_tank_limit, engine_limit)
        if fuel <= 0:
            return
        elif fuel > limit:
            warnings.warn(f'ERROR: Exceed fuel use limit of {limit}. You entered {fuel}')
            m = limit
        else:
            m = fuel

        # Accelerate
        thrust, m_ = self.engine.thrust(fuel=m, dt=1)
        if m > m_:
            raise Exception('m > m_')

        # Update statistics
        self.thrust = thrust
        self.fuel_burn = m
        self.acceleration = self.angular_position * self.thrust / (self.get_mass()-m)  # Accelerate

        return


    def angular_accelerate(self):
        """
        **Not implemented yet**
        Change angular acceleration.

        N.B. This function does not move the starship or burn fuel.
        It is the command to accelerate in the next time step.
        :return:
        """
        raise NotImplementedError

    def step(self, dt: float = 1, record=True):
        """
        Advance one time step.

        N.B. Take average?

        :param dt: float - time step
        :return: None
        """

        # Update translation
        self.fuel_tank.fuel -= self.fuel_burn                                       # Burn fuel
        self.acceleration = self.angular_position * self.thrust / self.get_mass()   # Accelerate (redundant)
        self.velocity += self.acceleration * dt                                     # Change speed
        self.position += (1/2 * self.acceleration * dt**2 + self.velocity * dt)     # Change position
        self.fuel_burn = 0                                                          # Reset to zero
        self.thrust = 0
        self.acceleration = np.zeros(3, dtype=np.float64)

        # Update rotation
        self.fuel_tank.fuel -= self.angular_fuel_burn                               # Burn fuel
        self.angular_acceleration = np.zeros(3)                                     # Not implemented
        self.angular_velocity += 0
        self.angular_position += 0

        if record:
            self.record()

        return

    # ============================== RETURNS ============================== #
    def get(self, x, show: bool = False, msg: str = ''):
        """
        Return the parameters and show optionally.
        :param x: parameters to print/ return
        :param show: bool - whether to print the object or not
        :return: x
        """

        if show:
            print(msg, x)
        return x

    def get_health(self, show: bool = False):
        return self.get(x=self.health, show=show, msg='Health:')

    def get_mass(self, show: bool = False):
        self.mass = self.fuel_tank.get_mass() + self.engine.get_mass() + self.angular_engine.get_mass()
        return self.get(x=self.mass, show=show, msg='Total Mass [kg]:')

    def get_fuel(self, show: bool = False):
        return self.get(self.fuel_tank.fuel, show=show, msg='Fuel [kg]:')

    def get_thrust(self, show: bool = False):
        return self.get(x=self.thrust, show=show, msg='Thrust [N]:')

    def get_acceleration(self, show: bool = False):
        return self.get(x=self.acceleration, show=show, msg='Acceleration [m/s^2]:')

    def get_velocity(self, show: bool = False):
        return self.get(x=self.velocity, show=show, msg='Velocity [m/s]:')

    def get_position(self, show: bool = False):
        return self.get(x=self.position, show=show, msg='Position [m]:')

    # ============================== RECORD ============================== #
    def record(self):
        self.record_position.append(list(self.position))
        self.record_velocity.append(list(self.velocity))
        self.record_acceleration.append(list(self.acceleration))
        return

    def plot(self):
        x = [p[0] for p in self.record_position]
        y = [p[1] for p in self.record_position]
        z = [p[2] for p in self.record_position]
        print(x, y, z)

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(x, y, z, label='Path')
        ax.set_xlabel('x')                          # Set X-Y-Z labels
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.legend()
        plt.show()
