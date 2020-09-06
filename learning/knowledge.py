
class Knowledge:
    """location of all learned knowledge"""
    def __init__(self,qs,new=False):
        if new:
            self.create_blank_memory()
        else:
            self.qs = qs
            self.episode = 0 

    def __getitem__(self,key):
        """returns specified q object given a state and actoin"""
        pass

    def create_blank_memory(self):
        """get all states and actions for the environment and create pairs"""
        pass

    def get_action(self,state,best=False):
        """returns an action given a state value, will ignore exploration and return best if best=True"""
        pass
