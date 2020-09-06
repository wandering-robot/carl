import pygame as py

from regulatory.gui import GUI
from regulatory.keeper import Keeper
from regulatory.handler import Handler


class Main:
    """Main section of code that allows for different sections to communicate"""
    def __init__(self):
        py.init()
        self.gui = GUI()
        self.keeper = Keeper()
        self.handler = Handler()

    def call_gui(self):
        """uses GUI to obtain user input, returns parameters in dict form"""
        pass

    def unpack_gui(self):
        """goes through the info gathered from GUI and distributes it approproately"""
        pass

    def get_data(self):
        """uses Keeper to obtain data"""
        pass

    def create_memory(self):
        """uses knowledge data to create AI's memory"""
        pass

    def create_environment(self):
        """uses environment data to create AI's environment"""
        pass

    def handle_input(self):
        """uses Handler to interpret user input"""
        pass

    def run_program(self):
        """main loop for learning/displaying"""
        pass

if __name__ == "__main__":
    Main()