##########################################################################
# Button: A class for main menu buttons
##########################################################################

import pygame as pg
import engine.file_paths as paths
from pygame.locals import *
from game_window.window import Window


class Button():

    def __init__(self, text, order_num):
        # Singleton instances
        self.window = Window.get_instance()

        # Main menu button constants
        self.properties = {
            "TEXT": text,
            "WIDTH": 6*self.window.properties["WIDTH_UNIT"],
            "HEIGHT": self.window.properties["HEIGHT_UNIT"],
            "ORDER_NUM": order_num,
            "UNPRESSED_BUTTON_COLOR": (255, 255, 255),
            "PRESSED_BUTTON_COLOR": (100, 100, 100),
            "UNPRESSED_TEXT_COLOR": (100, 100, 100),
            "PRESSED_TEXT_COLOR": (255, 255, 255),
            "START_Y": 4*self.window.properties["HEIGHT_UNIT"],
            "Y_GAP": int(0.75*self.window.properties["HEIGHT_UNIT"]),
            "FONT_SIZE": int(0.75*self.window.properties["HEIGHT_UNIT"]),
        }

        # Center coords
        self.properties.update({"CENTER_X": int(self.window.properties["CENTER_X"])})
        self.properties.update({"CENTER_Y": int(self.properties["START_Y"] + (self.properties["ORDER_NUM"] - 1) * (self.properties["HEIGHT"] + self.properties["Y_GAP"]))})

         # Destination coords
        self.properties.update({"TOP_LEFT_BUTTON_X": int(self.properties["CENTER_X"] - self.properties["WIDTH"]/2)})
        self.properties.update({"TOP_LEFT_BUTTON_Y": int(self.properties["CENTER_Y"] - self.properties["HEIGHT"]/2)})

        # Create a new surface for the button's rectangle
        self.button_surface = pg.Surface((self.properties["WIDTH"], self.properties["HEIGHT"]))

        # Create a collision box in top left corner
        self.collision_box = pg.Rect(0, 0, self.properties["WIDTH"], self.properties["HEIGHT"])
        # Move to the correct location. "move_ip" treats the button as a mutable type
        self.collision_box.move_ip(self.properties["TOP_LEFT_BUTTON_X"], self.properties["TOP_LEFT_BUTTON_Y"])

        # Button font
        font_folder = paths.get_font_folder()
        self.font = pg.font.Font(font_folder + "Gamy-PERSONAL.otf", self.properties["FONT_SIZE"])

    def draw(self):
        """Draw a button on screen with default size and colors, with given text and center coordinates."""
        # Color the button based on the pressed state
        if self.is_pressed():
            fill_color = self.properties["PRESSED_BUTTON_COLOR"]
        else:
            fill_color = self.properties["UNPRESSED_BUTTON_COLOR"]

        self.button_surface.fill(fill_color)

        # Draw the button's text onto the button
        self.draw_text()

        # Draw button to display surface
        self.window.display_surface.blit(self.button_surface, (self.properties["TOP_LEFT_BUTTON_X"], self.properties["TOP_LEFT_BUTTON_Y"]))

    def draw_text(self):
        """Draws the button text onto the center of the button."""

        if self.is_pressed():
            text_color = self.properties["PRESSED_TEXT_COLOR"]
        else:
            text_color = self.properties["UNPRESSED_TEXT_COLOR"]

        text_surface = self.font.render(self.properties["TEXT"], True, text_color)

        top_left_x = int(self.button_surface.get_width()/2 - text_surface.get_width()/2)
        top_left_y = int(self.button_surface.get_height()/2 - text_surface.get_height()/2)
        self.button_surface.blit(text_surface, (top_left_x, top_left_y))

    def is_pressed(self):
        """Returns true if the left mouse button is pressed on the button."""
        # If the left mouse button is pressed
        mouse_pressed = pg.mouse.get_pressed()[0] == 1
        # If the mouse is in the button's collision box
        mouse_location = pg.mouse.get_pos()
        mouse_in_collision_box = self.collision_box.collidepoint(mouse_location)

        return mouse_pressed and mouse_in_collision_box