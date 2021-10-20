""" # Container Class

    ## TODO
    1. Make attributes non-None
"""

from timestep import TimeStep


class Container(TimeStep):
    def __init__(self,
                 current_fill: (int, float) = None,
                 max_fill: (int, float) = None,
    ):
        self.current_fill = 0 if current_fill is None else current_fill
        self.max_fill = 0 if current_fill is None else max_fill

    # ==================== MEASURE CAPACITY ==================== #
    def is_overfilled(self):    # ERROR STATE
        return self.current_fill > self.max_fill

    def is_full(self):
        return self.current_fill >= self.max_fill

    def has_room(self):
        return 0 < self.current_fill < self.max_fill

    def is_empty(self):
        return self.current_fill == 0

    def is_negative(self):  # ERROR STATE
        return self.current_fill < 0

    def is_too_much(self, amount):  # BETTER NAME
        return self.current_fill + amount >= self.max_fill

    def is_enough(self, amount):    # BETTER NAME
        return self.current_fill - amount <= 0

    def _load(self, amount):
        self.current_fill += amount
        return

    def load(self, amount):
        if self.is_full():
            return
        elif self.
        self.add_action()


class Container:
    def __init__(self,
                 current_fill: (int, float) = None,
                 max_fill: (int, float) = None,
                 max_fill_rate: (int, float) = None,
                 min_fill_rate: (int, float) = None,
                 max_empty_rate: (int, float) = None,
                 min_empty_rate: (int, float) = None
                 ):
        """ Class to store current level, maximum, and maximum rates of change.

            ## Inputs

            ## Outputs

            ## Notes
        """

        self.current_fill = current_fill
        self.max_fill = max_fill

        self.max_fill_rate = max_fill_rate
        self.min_fill_rate = min_fill_rate

        self.max_empty_rate = max_empty_rate
        self.min_empty_rate = min_empty_rate

        self.action = lambda *args: False
        self.args = ()

    def __call__(self):
        self.action(*self.args)

    def _empty(self, empty_rate):
        self.current_fill -= empty_rate
        return

    def _fill(self, fill_rate):
        self.current_fill += fill_rate
        return

    def fill(self, fill_rate: (int, float) = None):
        if self.min_fill_rate <= fill_rate <= self.max_fill_rate:
            self.action = self._fill
            self.args = (fill_rate,)

    def empty(self, empty_rate: (int, float) = None):
        if self.min_empty_rate <= empty_rate <= self.max_empty_rate:
            self.action = self._empty
            self.args = (empty_rate,)

    def is_full(self):
        return self.current_fill == self.max_fill

    def is_empty(self):
        return self.current_fill == 0
