
class Handler:
    def __init__(self):
        pass

    def quit(self):
        """quit the program"""
        pass

class SubHandler(Handler):                                  #will rename when I realize what is needed of the program
    """to be used for specific situations in the program"""

    def __init__(self):
        super().__init__()

    def handle(self):
        """obtain user input at call appropriate method"""
        pass