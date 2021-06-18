##########################################################################
# Display wrapper: handles resolution, fullscreen toggle, and display object
##########################################################################

import pygame as pg
from pygame.locals import *

class Window():
    """Wrapper around all display functions"""

    def __init__(self):
        self.window_width = 500
        self.window_height = 500
        self.window_name = "Game"

        # Open a new window at the desired dimensions and set its properties
        pg.display.set_mode((self.window_width, self.window_height))
        pg.display.set_caption(self.window_name)