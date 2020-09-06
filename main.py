"""main entry to code"""

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

    def unpack_gui(self):
        """goes through the info gathered from GUI and distributes it approproately"""

    def get_data(self):
        """uses Keeper to obtain data"""

    def create_memory(self):
        """uses knowledge data to create AI's memory"""

    def create_environment(self):
        """uses environment data to create AI's environment"""

    def handle_input(self):
        """uses Handler to interpret user input"""

    def run_program(self):
        """main loop for learning/displaying"""

if __name__ == "__main__":
    Main()
