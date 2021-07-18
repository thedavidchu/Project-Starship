"""
# engine.py

## Contents
Contains the class call for a generic engine.

## Functionality
Dictate the statistics of an engine.

## TODO
- Add fuel mass to total mass
- Update mass when fuel used/ added
- Allow to amass fuel usage to combine small time-steps into larger ones
"""

import math
import warnings

class FuelTank(object):
    def __init__(self, name: str = 'Fuel Tank', dry_mass: int = 100, cost: int = 100, max_fuel: int = 100,
                 max_flow: int = 100):
        # Overview
        self.name = name                    # Default: 'Fuel Tank'
        self.dry_mass = dry_mass            # Default: 100 [kg]
        self.cost = cost                    # Default: 100 [$]

        # Statistics
        self.max_fuel = max_fuel            # Default: 100 [kg]
        self.max_flow = max_flow            # Default: 100 [kg/s]

        # Usage
        self.fuel = self.max_fuel           # How much fuel in tank

    # ============================== CHECK WEIGHT ============================== #
    def get_mass(self):
        """
        Return mass of the fuel tank + fuel
        :return: int - mass of fuel tank + fuel
        """
        return self.dry_mass + self.fuel

    # ============================== USE FUEL ============================== #
    def burn(self, fuel):
        """
        Use fuel that is slated to burn.
        :return: None
        """
        self.fuel -= fuel

    # ============================== CHECK FUEL ============================== #
    def max_fuel_use(self, fuel: int = None, dt: float = 1):
        """
        Returns the maximum amount of fuel you can use in a time step.
        :return: int - max fuel usage
        """
        maxm = min(self.fuel, self.max_flow * dt)

        if fuel is None:
            return maxm
        elif fuel > maxm:
            return maxm
        elif fuel <= 0:
            return 0
        else:
            return fuel

    # ============================== REFUEL ============================== #
    def max_refuel(self, fuel: int = None, dt: float = 1):
        """
        Returns the maximum amount that you can fill the fuel tank.
        :return:
        """
        empty = (self.max_fuel - self.fuel) * dt
        if empty < 0:
            warnings.warn(f'ERROR: Overfilled fuel tank! We have {-empty} excess!')

        maxm = min(empty, self.max_flow * dt)
        if fuel > maxm:
            return maxm
        elif fuel <= 0:
            return 0
        else:
            return fuel

    def refuel(self, fuel, dt: float = 1):
        """
        Refuel in time step.

        :param fuel: int - amount to refill
        :param dt: float - time step to refill in
        :return: None
        """
        max_refuel = self.max_refuel(dt=dt)
        if fuel > max_refuel:
            warnings.warn('ERROR: You spilled some fuel!')
            self.fuel += max_refuel
        elif fuel <= 0:
            warnings.warn('ERROR: You tried to remove fuel!')
        else:
            self.fuel += fuel
