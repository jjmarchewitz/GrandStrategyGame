"""
Window: handles resolution, fullscreen toggle, and display object
"""

from dataclasses import dataclass, field
import pygame as pg


@dataclass
class WindowProperties():
    """Properties list of a window object."""
    name: str
    fullscreen: bool
    width: int
    height: int
    width_unit: int = field(init=False)
    height_unit: int = field(init=False)
    center: list[int] = field(init=False)

    def __post_init__(self):
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

        # Window constants
        self.properties = WindowProperties("Game", False, 600, 600)
        # self.properties = WindowProperties("Game", True, 1440, 900)

        pg.init()
        pg.display.init()

        # Open a new window at the desired dimensions and set its properties
        if self.properties.fullscreen:
            display_info = pg.display.Info()
            self.properties.width = display_info.current_w
            self.properties.height = display_info.current_h
            # Initialize display surface as full screen at full resolution
            self.display_surface = pg.display.set_mode((self.properties.width, self.properties.height), pg.FULLSCREEN)
        else:
            # Initialize display surface as a window
            self.display_surface = pg.display.set_mode((self.properties.width, self.properties.height))


        pg.display.set_caption(self.properties.name)

    def clear(self):
        """Fill screen with black."""
        self.display_surface.fill((0, 0, 0))
