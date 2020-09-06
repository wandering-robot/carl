"""Aspect of code that handles the base requirements for states, actions, and qs"""


class BaseState:
    """base state class for specific environments to subclass off of"""
    def __init__(self,reward, *dimensions):
        self.dimensions = tuple(dimensions)
        self.reward = reward

    def __repr__(self):
        return f'{self.dimensions}'

    def __hash__(self):
        return hash(self.dimensions)

    def __eq__(self, other):
        return (self.dimensions) == (other.dimensions)

    def __ne__(self, other):
        return not self == other


class BaseAction:
    """base action class for specific environments to subclass off of"""
    def __init__(self, *directions):
        self.directions = tuple(directions)

    def __repr__(self):
        return f'{self.directions}'

    def __hash__(self):
        return hash(self.directions)

    def __eq__(self, other):
        return (self.directions) == (other.directions)

    def __ne__(self, other):
        return not self == other


class BaseQ:
    """base action class for specific environments to subclass off of"""
    def __init__(self, state, action):
        self.state = state
        self.action = action

        self.elig = 0       #eligibility
        self.value = 0

    def __repr__(self):
        return f'S:{self.state}&A:{self.action}'

    def __hash__(self):
        return hash((self.state, self.action))

    def __eq__(self, other):
        return (self.state, self.action) == (other.state, other.action)

    def __ne__(self, other):
        return not self == other

if __name__ == "__main__":
    from random import choice

    states = [BaseState(i, j, k) for i in range(5) for j in range(3) for k in range(4)]
    actions_range = [-1, 0, 1]
    actions = [BaseAction(right, down, out)
               for right in actions_range
               for down in actions_range
               for out in actions_range]

    qs = {}
    for s in states:
        for a in actions:
            qs[(s, a)] = BaseQ(s, a)

    for _ in range(5):
        random_state = choice(states)
        random_action = choice(actions)
        random_q = qs[(random_state, random_action)]

        print(random_state)
        print(random_action)
        print(random_q)
        print('\n\n')
    