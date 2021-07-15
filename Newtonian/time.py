class Time:
    def __init__(self, dt=0.05):
        self.time = 0
        self.dt = dt

        self.action = {}

    def add_action(self, function, params):
        self.action[function] = params
        return

    def step(self):
        return [function(*params) for function, params in self.action.items()]
