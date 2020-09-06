class Keeper:
    """Recieves problem_name, finds relevent files, and returns them"""
    def __init__(self): #problem name as input
        # self.problem_name = problem_name
        pass

    def check_if_storage(self):
        """Run this code to ensure that there is a storage folder, if not create one"""
        pass

    def check_if_exists(self):
        """Returns True or False if problem_files exist or not"""
        pass

    def get_filename4load(self):
        """finds filename given the problem name"""
        pass

    def load_data(self,filename):
        """returns unpickled data given a filename"""
        pass

    def get_filename4save(self,data):
        """given the data, returns the appropriate filename for saving"""
        pass

    def save_data(self,data):
        """pickles data in appropriate file name"""
        pass
