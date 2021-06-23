##########################################################################
# Main menu: handles main menu and sub-menus
##########################################################################

import pygame as pg
from pygame.locals import *
# from window import window

class MainMenu():
    # Singleton instance
    __instance = None
    def get_instance():
        if MainMenu.__instance == None:
            MainMenu()
        return MainMenu.__instance

    def __init__(self):
        if MainMenu.__instance == None:
            MainMenu.__instance = self

        self.window = window.Window.get_instance()

        # Main menu button constants
        self.button_properties = {
            "WIDTH": self.window.properties["WIDTH"]/4,
            "HEIGHT": self.window.properties["HEIGHT"]/16,
            "CENTER_COLOR": (255, 255, 255),
            "BORDER_COLOR": (0, 0, 0),
            "TEXT_COLOR": (255, 255, 255),
        }

    def main_menu(self):
        """Draw the main menu and check for button presses.

        This gets called in a loop and if statements can be used to perform actions once per frame.
        """
        # Blue background
        pg.Surface.fill(self.window.display_surface, self.window.properties["MENU_BACKGROUND"])

        # Center X value of the screen
        center_x = self.window.properties["WIDTH"]/2

        # Center coordinates of each button
        button_center_coordinates = {
            "SINGLE_PLAYER": (center_x, 5*self.window.properties["HEIGHT"]/16),
            "HOST_MP": (center_x, 7*self.window.properties["HEIGHT"]/16),
            "JOIN_MP": (center_x, 9*self.window.properties["HEIGHT"]/16),
            "OPTIONS": (center_x, 11*self.window.properties["HEIGHT"]/16),
            "QUIT": (center_x, 13*self.window.properties["HEIGHT"]/16),
        }

        # Draw buttons
        main_menu_buttons = {
            "SINGLE_PLAYER": self.draw_button("SINGLE PLAYER", button_center_coordinates["SINGLE_PLAYER"]),
            "HOST_MP": self.draw_button("HOST", button_center_coordinates["HOST_MP"]),
            "JOIN_MP": self.draw_button("JOIN", button_center_coordinates["JOIN_MP"]),
            "OPTIONS": self.draw_button("OPTIONS", button_center_coordinates["OPTIONS"]),
            "QUIT": self.draw_button("QUIT", button_center_coordinates["QUIT"]),
        }


    def draw_button(self, text, center_coords):
        """Draw a button on screen with default size and colors, with given text and center coordinates."""
        center_x = center_coords[0]
        center_y = center_coords[1]

        # Create in top left with proper width and height, then move to make it easier to read
        button = pg.Rect(0, 0, self.button_properties["WIDTH"], self.button_properties["HEIGHT"])
        # Move in-place treats the button as a mutable type
        button.move_ip(center_x - self.button_properties["WIDTH"]/2, center_y - self.button_properties["HEIGHT"]/2)

        # Create a new surface for the button's rectangle
        button = pg.Surface((self.button_properties["WIDTH"], self.button_properties["HEIGHT"]))

        # Color the button
        button.fill(self.button_properties["CENTER_COLOR"])

        # Destination coords
        top_left_button_x = 
        top_left_button_y =

        # Draw button to display surface
        self.window.display_surface.blit(button, (top_left_button_x, top_left_button_y))
        

        return button


# Singleton instance
menu_obj = None
def get_instance():
    if menu_obj == None:
        menu_obj = Window()
    return menu_obj