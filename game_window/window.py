##########################################################################
# Window: handles resolution, fullscreen toggle, and display object
##########################################################################

import pygame as pg

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
        self.properties = {
            "NAME": "Game",
            "WIDTH": 600,
            "HEIGHT": 600,
            "FULLSCREEN": False,
        }
        # This is done because dictionary values cannot reference themselves during instantiation
        self.properties.update({"WIDTH_UNIT": int(self.properties["WIDTH"]/12)})
        self.properties.update({"CENTER_X": int(self.properties["WIDTH"]/2)})
        self.properties.update({"HEIGHT_UNIT": int(self.properties["HEIGHT"]/12)})
        self.properties.update({"CENTER_Y": int(self.properties["HEIGHT"]/2)})


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

    def clear(self):
        # Fill screen with black
        self.display_surface.fill((0, 0, 0))
        pg.display.flip()
