class TimeStep:
    """ An object that stores actions and arguments to do and executes them
        when called.

        ## Notes
        1. How to ensure mutual exclusivity between functions that cannot occur
            at the same time?
        2. Actions must be hashable.
    """

    def __init__(self):
        # {function: (arguments,), }
        self.actions = {}

    def __str__(self):
        actions = ', '.join([f'{fn.__name__}{args}' for fn, args in self.actions.items()])
        return f'TimeStep({actions})'

    def __repr__(self):
        return self.__str__()

    def __call__(self):
        self.time_step()
        return

    def time_step(self):
        return [fn(*args) for fn, args in self.actions.items()]

    def add_action(self, fn, args):
        """
        Add an action to the TimeStep.

        :param fn: function pointer
        :param args: tuple - arguments that will be unwrapped
            as parameters when the function is called.
        :return: None
        """
        self.actions[fn] = tuple(args)
        return


if __name__ == '__main__':
    a = TimeStep()

    print(f'Empty TimeStep: {a}')

    a.add_action(sum, ((1, 2),))
    print(f'TimeStep: {a}')
    a()