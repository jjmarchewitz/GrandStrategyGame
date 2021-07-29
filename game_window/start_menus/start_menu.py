##########################################################################
# Start menu: handles main menu and sub-menus
##########################################################################

import engine.file_paths as paths
import os
import pygame as pg
import textwrap
from .button import Button
from .menus import Menu
from dataclasses import dataclass, field
from engine.events.event_handler import EventHandler
from engine.state_manager import StateManager
from game_window.window import Window, WindowProperties
from pygame.event import pump

@dataclass
class StartMenuProperties():
    window = Window.get_instance()
    background_color: tuple[int, int, int] = (25, 205, 255)
    title_text: str = "GEARS OF HALO THEFT AUTO 5"
    title_color: tuple[int, int, int] = (50, 50, 50)
    title_center_x: int = window.properties.center_x
    title_center_y: int = int(1.5*window.properties.height_unit)
    title_font_size: int = int(1.15*window.properties.height_unit)


class StartMenu():  
    # Singleton instance
    __instance = None
    def get_instance():
        if StartMenu.__instance == None:
            StartMenu()
        return StartMenu.__instance

    def __init__(self):
        # Create singleton instance
        if StartMenu.__instance == None:
            StartMenu.__instance = self

        # Grab singleton instances
        self.event_handler = EventHandler.get_instance()
        self.state_manager = StateManager.get_instance()
        self.window = Window.get_instance()

        # Main menu properties
        self.properties = StartMenuProperties()

        self.menus = {
            "MAIN": "MAIN",
            "SP": "SP",
            "HOST": "HOST",
            "JOIN": "JOIN",
            "OPTIONS": "OPTIONS",
            "QUIT": "QUIT",
        }

        # Main menu buttons
        self.buttons = {
            "SP": Button("SINGLE PLAYER", 1),
            "HOST": Button("HOST", 2),
            "JOIN": Button("JOIN", 3),
            "OPTIONS": Button("OPTIONS", 4),
            "QUIT": Button("QUIT", 5),
        }

        # Title font
        font_file_path = os.path.join(paths.get_font_folder(), "Halo3.ttf")
        self.title_font = pg.font.Font(font_file_path, self.properties.title_font_size)

    def start_menu(self, current_event):
        """Execute the main menu logic, including calling any sub-menus."""

        # Check if the current event is a start menu change
        if self.event_handler.custom_types["START_MENU"].pygame_id == current_event.type:
            self.window.clear()

            # Update the menu to be the correct one
            self.update_menu(current_event)

        # Check the current menu's buttons for updates
        self.check_buttons()

    def update_menu(self, current_event):
        """Check the current event against each menu type and display the appropriate one if required."""
        # Main menu
        if self.menus["MAIN"] == current_event.__dict__["MENU_NAME"]:
            self.state_manager.update_state(self.state_manager.start_menu["MAIN"])
            self.draw_start_menu()
        # Start a new singleplayer
        elif self.menus["SP"] == current_event.__dict__["MENU_NAME"]:
            self.state_manager.update_state(self.state_manager.start_menu["SP"])
        # Host a new multiplayer
        elif self.menus["HOST"] == current_event.__dict__["MENU_NAME"]:
            self.state_manager.update_state(self.state_manager.start_menu["HOST"])
        # Join a new multiplayer
        elif self.menus["JOIN"] == current_event.__dict__["MENU_NAME"]:
            self.state_manager.update_state(self.state_manager.start_menu["JOIN"])
        # Options menu
        elif self.menus["OPTIONS"] == current_event.__dict__["MENU_NAME"]:
            self.state_manager.update_state(self.state_manager.start_menu["OPTIONS"])

    def check_buttons(self):
        """Check the current menu state and call the appropriate button check function."""
        if self.state_manager.state == self.state_manager.start_menu["MAIN"]:
            self.check_start_menu_buttons()
        elif self.state_manager.state == self.state_manager.start_menu["SP"]:
            # TODO: replace with a sub-menu instead of a direct call to start the game
            pass
        elif self.state_manager.state == self.state_manager.start_menu["HOST"]:
            pass
        elif self.state_manager.state == self.state_manager.start_menu["JOIN"]:
            pass
        elif self.state_manager.state == self.state_manager.start_menu["OPTIONS"]:
            pass

    def check_start_menu_buttons(self):
        """Check the start menu buttons and post an event to the queue if pressed."""
        event = None

        # If any of the buttons were pressed, create the corresponding event
        if self.buttons["SP"].is_pressed():
            event = self.event_handler.create_event("START_MENU", {"MENU_NAME": "SP"})
        elif self.buttons["HOST"].is_pressed():
            event = self.event_handler.create_event("START_MENU", {"MENU_NAME": "HOST"})
        elif self.buttons["JOIN"].is_pressed():
            event = self.event_handler.create_event("START_MENU", {"MENU_NAME": "JOIN"})
        elif self.buttons["OPTIONS"].is_pressed():
            event = self.event_handler.create_event("START_MENU", {"MENU_NAME": "OPTIONS"})
        elif self.buttons["QUIT"].is_pressed():
            event = pg.event.Event(pg.QUIT)

        # Check that the event was created and that it isn't already in the queue.
        # Pump = False prevents the queue from being processed by this operation.
        if event != None and pg.event.peek(event.type, pump=False) != 1:
            # Post event to the end of the queue
            pg.event.post(event)


    def draw_start_menu(self):
        """Draw the main menu and check for button presses.

        This gets called in a loop and if statements can be used to perform actions once per frame.
        """
        # Blue background
        self.window.display_surface.fill(self.properties.background_color)

        # Game title
        self.draw_title_text()

        # Draw buttons
        for name, button in self.buttons.items():
            button.draw()


    def draw_title_text(self):
        """Draws the title text onto the main menu screen."""
        # TODO: update so that the wrap works with all text by adding words on one by one. "Motherfucker" on a 600x600 will break the current version.
        wrapped_title_text_lines = textwrap.fill(self.properties.title_text, 12).split("\n")
        number_of_lines = len(wrapped_title_text_lines)
        line_height = self.title_font.size(wrapped_title_text_lines[0])[1]

        title_surface = pg.Surface((self.window.properties.width, number_of_lines * line_height))
        black = (0, 0, 0)
        title_surface.fill(black)
        title_surface.set_colorkey(black)

        for line_number, line in enumerate(wrapped_title_text_lines):
            text_surface = self.title_font.render(line, True, self.properties.title_color)

            top_left_x = int(self.window.properties.width/2 - text_surface.get_width()/2)
            top_left_y = line_number * text_surface.get_height()

            title_surface.blit(text_surface, (top_left_x, top_left_y))
        

        top_left_x = int(self.window.properties.width/2 - title_surface.get_width()/2)
        top_left_y = 0

        self.window.display_surface.blit(title_surface, (top_left_x, top_left_y))