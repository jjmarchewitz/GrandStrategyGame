##########################################################################
# Display wrapper: handles resolution, fullscreen toggle, and display object
##########################################################################

import pygame as pg
from pygame.locals import *

class Window():
    """Wrapper around all display functions."""

    # Singleton instance
    __instance = None
    def get_instance():
        if Window.__instance == None:
            Window()
        return Window.__instance

    def __init__(self):
        if Window.__instance == None:
            Window.__instance = self
            
        # Window constants
        self.properties = {
            "NAME": "Game",
            "WIDTH": 500,
            "HEIGHT": 500,
            "MENU_BACKGROUND": (25, 205, 255),
            "FULLSCREEN": True
        }

        pg.init()
        pg.display.init()

        # Open a new window at the desired dimensions and set its properties
        if self.properties["FULLSCREEN"]:
            display_info = pg.display.Info()
            self.properties["WIDTH"] = display_info.current_w
            self.properties["HEIGHT"] = display_info.current_h
            # Initialize display surface as full screen at full resolution
            self.display_surface = pg.display.set_mode((self.properties["WIDTH"], self.properties["HEIGHT"]), pg.FULLSCREEN)
        else:
            # Initialize display surface as a window
            self.display_surface = pg.display.set_mode((self.properties["WIDTH"], self.properties["HEIGHT"]))
        pg.display.set_caption(self.properties["NAME"])
