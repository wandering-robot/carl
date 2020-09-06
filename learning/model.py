"""saves agents' knowledge of environment for future planning"""
from random import choice, choices

from test_environment.states_base import BaseState, BaseQ, BaseAction       #imported fake stuff for testing since don't know how to get parent files

class Model:
    """model of environment for agent's future planning"""
    def __init__(self):
        self.env = {}

    def __getitem__(self, q):
        """using a q as key, return the predected state and reward"""
        guesser = self.env[q]
        prime = guesser()
        return prime

    def __setitem__(self, q, s_prime):
        """using q as key, update the model's prediction stochastically with state prime"""
        if not isinstance(s_prime, BaseState):
            raise TypeError('Must be a State object')
        try:
            guess = self.env[q]
            guess.update(s_prime)
        except KeyError:
            self.env[q] = StochGuess(s_prime)


    def prioritized_sweep(self):
        """given a changed aspect of model, propogate the change through the model"""

class StochGuess:
    """the object that a model stores probabilities for each q"""
    def __init__(self, s_prime):
        self.guess = [s_prime]
        self.prob = [1]
        self.n = 1

    def __repr__(self):
        max_prob = max(self.prob)
        i = self.prob.index(max_prob)
        max_prime = self.guess[i]
        return f'{max_prime} w/ {max_prob*100}%'

    def __call__(self):
        prime = choices(self.guess, self.prob)
        return prime

    def update(self, s_prime):
        """update the guess and corresponding probabilities"""
        found = False
        for i in range(self.n):
            if self.guess[i] == s_prime:
                self.prob[i] = self.prob[i] * self.n/(self.n+1) + 1/(self.n+1)
                found = True
            else:
                self.prob[i] = self.prob[i] * self.n/(self.n+1)
        if not found:
            self.guess.append(s_prime)
            self.prob.append(1/(self.n+1))
            self.n += 1

if __name__ == "__main__":

    states = [BaseState(i, j, k) for i in range(5) for j in range(3) for k in range(4)]
    
    actions_range = [-1, 0, 1]
    actions = [BaseAction(right, down, out)
               for right in actions_range
               for down in actions_range
               for out in actions_range]

    qs = {}
    for si in states:
        for ai in actions:
            qs[(si, ai)] = BaseQ(si, ai)

    model = Model()

    si = choice(states)
    ai = choice(actions)
    qi = qs[(si, ai)]

    for state in [states[1], states[2], states[3], states[1], states[2], states[3]]:
        model[qi] = state

for _ in range(10):
    print(model[qi])


    