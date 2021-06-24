##########################################################################
# Main menu: handles main menu and sub-menus
##########################################################################

import pygame as pg
from pygame.locals import *
from game_window.window import Window

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

        self.window = Window.get_instance()

        # Main menu button constants
        self.button_properties = {
            "WIDTH": 2*self.window.properties["WIDTH"]/6,
            "HEIGHT": self.window.properties["HEIGHT"]/12,
            "CENTER_COLOR": (255, 255, 255),
            "BORDER_COLOR": (0, 0, 0),
            "TEXT_COLOR": (255, 255, 255),
            "CENTER_X": self.window.properties["WIDTH"]/2,
            "START_Y": 4*self.window.properties["HEIGHT"]/12,
            "Y_GAP": self.window.properties["HEIGHT"]/16,
        }

    def main_menu(self):
        """Draw the main menu and check for button presses.

        This gets called in a loop and if statements can be used to perform actions once per frame.
        """
        # Blue background
        pg.Surface.fill(self.window.display_surface, self.window.properties["MENU_BACKGROUND"])

        # Draw buttons
        main_menu_buttons = {
            "SINGLE_PLAYER": self.draw_button("SINGLE PLAYER", 1),
            "HOST_MP": self.draw_button("HOST", 2),
            "JOIN_MP": self.draw_button("JOIN", 3),
            "OPTIONS": self.draw_button("OPTIONS", 4),
            "QUIT": self.draw_button("QUIT", 5),
        }

    def draw_button(self, text, order_num):
        """Draw a button on screen with default size and colors, with given text and center coordinates."""
        center_x = self.button_properties["CENTER_X"]
        center_y = self.button_properties["START_Y"] + (order_num - 1) * (self.button_properties["HEIGHT"] + self.button_properties["Y_GAP"])

        # Create in top left with proper width and height, then move to make it easier to read
        button = pg.Rect(0, 0, self.button_properties["WIDTH"], self.button_properties["HEIGHT"])
        # Move in-place treats the button as a mutable type
        button.move_ip(center_x - self.button_properties["WIDTH"]/2, center_y - self.button_properties["HEIGHT"]/2)

        # Create a new surface for the button's rectangle
        button = pg.Surface((self.button_properties["WIDTH"], self.button_properties["HEIGHT"]))

        # Color the button
        button.fill(self.button_properties["CENTER_COLOR"])

        # Destination coords
        top_left_button_x = center_x - self.button_properties["WIDTH"]/2
        top_left_button_y = center_y - self.button_properties["HEIGHT"]/2

        # Draw button to display surface
        self.window.display_surface.blit(button, (top_left_button_x, top_left_button_y))
        

        return button


# Singleton instance
menu_obj = None
def get_instance():
    if menu_obj == None:
        menu_obj = Window()
    return menu_obj