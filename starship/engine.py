"""
# engine.py

## Contents
Contains the class call for a generic engine.

## Functionality
Dictate the statistics of an engine.
"""


import math


class Engine(object):
    def __init__(self, name: str = 'Engine', dry_mass: int = 100, cost: int = 100,
                 energy_efficiency = lambda x: 1.0 * x, momentum_efficiency = lambda x: 1.0 * x,
                 max_flow: int = 100, energy_density: int = 299792458**2):

        # Overview
        self.name = name                                    # Default: 'Engine'
        self.mass = dry_mass                                # Default: 100 [kg]
        self.cost = cost                                    # Default: 100 [$]

        # Statistics
        self.energy_efficiency = energy_efficiency          # Default: x*100%
        self.momentum_efficiency = momentum_efficiency      # Default: x*100%
        self.max_flow = max_flow                            # Default: 100 [kg/s]
        self.energy_density = energy_density                # Default: c^2 [J/kg]

        # Usage
        self.flow = 0                                       # Not used
        self.temperature = 0                                # Not used
        self.wear = 0                                       # Not used

    def fusion_thrust(self, fuel: int = 1, dt: float = 1.0):
        """
        Take in fuel and output thrust force magnitude and fuel burned.

        Fuel [kg] -> Convert into energy * efficiency ->
                -> find momentum of fuel mass * efficiency ->
                -> output force

        ## Fuel to Energy
            - E = m*c^2, where m = fuel
            - Efficiency: find the % of mass that turns to energy
                * In the limiting case that % -> 0, use a different function to avoid numeric instability

        ## Energy to Momentum
            - E = 1/2*m*v^2 => v = sqrt(2E/m)
            - p = m*v = sqrt(2Em)
            - Efficiency: find the % of mass that is ejected straight back

        ## Flaws
            - If we convert mass to energy, do we have to subtract this from what we eject out the back?
            - As energy/mass -> 0, we will get numeric instability
            - If an invalid amount of fuel is injected, we will have

        :param fuel: int - quantity of fuel to burn
        :return:
            - float - magnitude of thrust
            - int - quantity of fuel burned
        """
        # Error Check Fuel flow
        if fuel > self.max_flow:    # Restrict max fuel flow
            m = self.max_flow
        elif fuel <= 0:             # Fuel flow must be strictly positive
            return 0, 0
        else:                       # Take fuel if valid
            m = fuel

        energy = self.energy_efficiency(m * self.energy_density)
        momentum = self.momentum_efficiency(math.sqrt(2*energy*m))
        force = momentum / dt

        return force, m

    def heat_analysis(self):
        """
        **Not implemented yet**
        Ensure that heat is being properly dissipated from the engine.
        If it overheats, we

        ## Important Factors
        - Heat retention when using engine
        - Heat dissipation
        - How heat affects the engine

        ## Functionality
        - Update temperature
        - Based on engine temperature, determine functionality

        :return: None
        """
        return None