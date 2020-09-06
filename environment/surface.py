import pygame as py

class Surface:
    """object that ties pygame surface to environment state"""
    def __init__(self,source):
        self.source = source

        self.colour = None      #(r,g,b)
        self.size = None        #(width, height)
        self.anchor = None      #(x,y)
        self.update()

        self.cell = py.Surface(self.size).convert()     


    def update(self):
        """updates the state's colour, size, and anchor"""
        self.colour = self.source.get_colour()
        self.anchor = self.source.get_anchor()
        if self.source.get_size() != self.size:
            self.size = self.source.get_size()
            self.cell = py.Surface(self.size).convert()     #in here in case the size changes



