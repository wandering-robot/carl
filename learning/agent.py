
class Agent:
    def __init__(self):
        pass

    def get_state(self):
        """obtain state from environment"""
        pass

    def get_primes(self, state, action):        #make direct call to environment's get_primes
        """given state and action, obtain state prime and reward"""
        pass

    def update_knowledge(self):
        """passes update to knowledge to change q values"""
        pass

    def update_model(self):
        """passes update to model to change primes"""
        pass

    def make_eligible(self):
        """add q to list of recently visited qs"""
        pass

    def similar_qs(self):
        """finds qs that will lead to same primes"""
        pass

    