"""aspect of code that gives a base for how environments should behave"""

class EnvironmentBase:
    """Base class that all problems will be subclasses of"""
    def __init__(self):
        self.states = []

    def get_primes(self, state, action):
        """given a state and an action, return the next state and reward"""
        