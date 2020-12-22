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
        self.fuel = self.max_fuel

    # ============================== CHECK WEIGHT ============================== #
    def mass(self):
        """
        Return mass of the fuel tank + fuel
        :return: int - mass of fuel tank + fuel
        """
        return self.dry_mass + self.fuel

    # ============================== USAGE ============================== #
    def max_use_fuel(self):
        """
        Returns the maximum amout of fuel you can use in a timestep.
        :return: int - max fuel usage
        """
        return min(self.fuel, self.max_flow)

    def use_fuel(self, fuel: int = 1):
        """
        Takes fuel request and returns the maximum amout of fuel useable.

        :param fuel:
        :return:
        """
        # Check flow
        if fuel > self.max_flow:
            warnings.warn('ERROR: Requested more than max flow')
            m = self.max_flow
        elif fuel <= 0:
            warnings.warn('ERROR: Requested backward flow')
            return 0
        else:
            m = fuel

        # Check fuel levels
        if fuel > self.fuel:
            warnings.warn('ERROR: You wanted to use more fuel than we have!')
            m = self.fuel

        return m

    # ============================== REFUEL ============================== #
    def max_refuel(self):
        """
        Returns the maximum amount that you can fill the fuel tank.
        :return:
        """
        empty = self.max_fuel - self.fuel
        if empty < 0:
            warnings.warn(f'ERROR: Overfilled fuel tank! We have {-empty} excess!')
        return min(empty, self.max_flow)

    def refuel(self, fuel):
        """
        Refuel the fuel tank.

        :param fuel: int - amount of fuel we want to put in the tank
        :return: int - the amout of fuel we managed to fit in the tank
        """
        # Check flow
        if fuel > self.max_flow:                # Cap at max flow
            warnings.warn(f'ERROR: Tried to refuel too quickly. Capped at {self.max_flow}')
            m = self.max_flow
        elif fuel <= 0:                         # Ensure positive flow
            warnings.warn('ERROR: Tried to refuel negative fuel!')
            return 0, 0
        else:                                   # Accept
            m = fuel

        # Check overfill
        empty = self.max_fuel - self.fuel
        if fuel > empty:
            warnings.warn(f'ERROR: Overflow warning. Fuel capped at {empty}')
            m = empty

        return m

