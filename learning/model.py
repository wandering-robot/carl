class Model:
    def __init__(self):
        self.env = {}

    def __getitem__(self,key):
        """using a q as key, return the predected state and reward"""
        pass

    def __setitem__(self,q,state_reward):
        """using q as key, update the model's prediction stochastically with state_reward tuple"""
        pass

    def prioritzed_sweep(self):
        """given a changed aspect of model, propogate the change through the model"""
        pass

