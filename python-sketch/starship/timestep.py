class TimeStep:
    """ An object that stores actions and arguments to do and executes them
        when called.

        ## Notes
        1. How to ensure mutual exclusivity between functions that cannot occur
            at the same time?
        2. Actions must be hashable.
    """

    def __init__(self):
        self.action = set()
        self.args = dict()

    def __str__(self):
        return ', '.join([f'{action}{tuple(self.args[action])}' for action in self.action])

    def __call__(self):
        for action in self.action:
            action(*self.args[action])
        return

    def timestep(self):
        self.__call__()
        return

    def add_action(self, action, args):
        self.action.add(action)
        self.args[action] = args


if __name__ == '__main__':
    a = TimeStep()

    print(f'Empty TimeStep: {a}')

    a.add_action(sum, ((1, 2),))
    print(f'TimeStep: {a}')
    a()
