"""
Window: handles display object and its properties such as resolution and fullscreen toggle
"""

import pygame as pg
from dataclasses import dataclass, field


@dataclass
class WindowProperties():
    """Properties list of a window object."""
    name: str
    fullscreen: bool
    width: int = field(init=False)
    height: int = field(init=False)
    width_unit: int = field(init=False)
    height_unit: int = field(init=False)
    center: list[int] = field(init=False)

    def __post_init__(self):
        display_info = pg.display.Info()
        # If in fullscreen mode, set screen size to the current display size
        if self.fullscreen:
            self.width = display_info.current_w
            self.height = display_info.current_h
        # Otherwise, make a default of 600x600 pixels
        else:
            # TODO: Update with user-changeable settings
            self.width = 600
            self.height = 600
            
        self.width_unit = self.width/12
        self.height_unit = self.height/12
        self.center_x = self.width/2
        self.center_y = self.height/2


class Window():
    """Wrapper around all display functions."""

    # Singleton instance
    __instance = None
    @staticmethod
    def get_instance():
        if Window.__instance == None:
            Window()
        return Window.__instance

    def __init__(self):
        if Window.__instance == None:
            Window.__instance = self
            
        # Init the display if it has not already been initialized
        if not pg.display.get_init():
            pg.display.init()

        # Window constants
        #self.properties = WindowProperties("Game", False)
        self.properties = WindowProperties("Game", True) #, 1440, 900)

        # Open a new window at the desired dimensions and set its properties
        if self.properties.fullscreen:
            # Initialize display surface as full screen at full resolution
            self.display_surface = pg.display.set_mode((self.properties.width, self.properties.height), pg.FULLSCREEN)
        else:
            # Initialize display surface as a window
            self.display_surface = pg.display.set_mode((self.properties.width, self.properties.height))


        pg.display.set_caption(self.properties.name)

    def clear(self):
        """Fill screen with black."""
        self.display_surface.fill((0, 0, 0))
