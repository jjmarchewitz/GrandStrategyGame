"""
Button: A class for main menu buttons
"""

import engine.file_paths as paths
import pygame as pg
import os
from dataclasses import dataclass, field
from game_window.window import Window
from pygame.locals import *

@dataclass
class ButtonProperties():
    window = Window.get_instance()
    text: str
    center_x: int
    center_y: int

    # Size and positional
    width: int = 6*window.properties.width_unit
    height: int = window.properties.height_unit
    font_size: int = int(0.75*window.properties.height_unit)

    # Top left coordinates
    top_left_x: int = field(init=False)
    top_left_y: int = field(init=False)

    # Colors
    unpressed_button_color: tuple[int, int, int]  = (255, 255, 255)
    pressed_button_color: tuple[int, int, int]  = (100, 100, 100)
    unpressed_text_color: tuple[int, int, int]  = (100, 100, 100)
    pressed_text_color: tuple[int, int, int]  = (255, 255, 255)

    # Update coordinate values once class has been initialized
    def __post_init__(self):
        self.top_left_x = self.center_x - self.width/2
        self.top_left_y = self.center_y - self.height/2


class Button():

    def __init__(self, text, function, center_coords):
        # Singleton instances
        self.window = Window.get_instance()

        # Main menu button constants
        self.properties = ButtonProperties(text, center_coords[0], center_coords[1])

        # Create a new surface for the button's rectangle
        self.button_surface = pg.Surface((self.properties.width, self.properties.height))

        # Create a collision box in top left corner
        self.collision_box = pg.Rect(0, 0, self.properties.width, self.properties.height)
        # Move to the correct location. "move_ip" treats the button as a mutable type
        self.collision_box.move_ip(self.properties.top_left_x, self.properties.top_left_y)

        # Make the button's function to call on a press an instance variable
        self.function = function

        # Boolean representing if the button is pressed
        self.pressed = False

        # Button font
        font_file_path = os.path.join(paths.get_font_folder(), "Gamy-PERSONAL.otf")
        self.font = pg.font.Font(font_file_path, self.properties.font_size)

    def check(self):
        """Update the button's state and run code accordingly."""
        previous_pressed_state = self.pressed
        currently_pressed = self.is_pressed()

        # If the button was pressed, redraw the button
        if self.was_pressed(previous_pressed_state, currently_pressed):
            self.draw()
        # If the button was released, redraw the button
        elif self.was_released(previous_pressed_state, currently_pressed):
            self.draw()

    def draw(self):
        """Draw a button on screen with default size and colors, with given text and center coordinates."""
        # Color the button based on the pressed state
        if self.pressed:
            fill_color = self.properties.pressed_button_color
            text_color = self.properties.pressed_text_color
        else:
            fill_color = self.properties.unpressed_button_color
            text_color = self.properties.unpressed_text_color

        self.button_surface.fill(fill_color)

        # Draw the button's text onto the button
        self.draw_text(text_color)

        # Draw button to display surface
        self.window.display_surface.blit(self.button_surface, (self.properties.top_left_x, self.properties.top_left_y))

    def draw_text(self, text_color):
        """Draws the button text onto the center of the button."""

        text_surface = self.font.render(self.properties.text, True, text_color)

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

        self.pressed = mouse_pressed and mouse_in_collision_box

        return self.pressed

    def was_released(self, previous_pressed_state, currently_pressed):
        """Returns true if the left mouse button is released from pressing the button"""

        released = False
        if previous_pressed_state == True and currently_pressed == False:
            released = True
            self.function()

        return released

    def was_pressed(self, previous_pressed_state, currently_pressed):
        """Returns true if the left mouse button just started pressing the button"""

        just_pressed = False
        if previous_pressed_state == False and currently_pressed == True:
            just_pressed = True

        return just_pressed


