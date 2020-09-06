"""bunch of data that is saved when passed to Keeper"""

class Data:
    """How the data of an AI will be stored in memory"""
    def __init__(self, knowledge_list, environment):
        self.knowledge_list = knowledge_list
        self.environment = environment

    def unpack_knowledge(self):
        """return all knowledge"""

    def unpack_environment(self):
        """return environment"""

class KnowledgeData:
    """store the qs and q_values of the problem's environment, model of the environment, and episode number"""
    def __init__(self, q_list, model, episode):
        self.q_list = q_list
        self.model = model
        self.episode = episode


class EnvironmentData:
    """stores the states and action spaces that make up the environment"""
    def __init__(self, states):
        self.states = states
