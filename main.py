"""
Entry-point to the program, execute using

> python main.py

TODO Update if any arguments are needed
"""

import pdb
# pdb.set_trace()

import pygame as pg
from pygame.locals import *
from window import *


class GameExecutor():
    """Highest-level instance of the game."""

    def __init__(self):
        """Defining class constants and variables, calling main()."""

        # Initialize pygame objects
        pg.init()
        pg.display.init()

        # Get singleton instances
        self.window = window.Window.get_instance()
        self.main_menu = main_menu.MainMenu.get_instance()

        # Define program states
        self.states = {
            "MAIN_MENU": 0,
            "SINGLE_PLAYER": 1,
            "HOST_MP": 2,
            "JOIN_MP": 3,
            "OPTIONS": 4,
            "QUIT": 5,
        }

        # Set the state to be in the menu
        self.program_state = self.states["MAIN_MENU"]

        # Turn off repeated key input
        pg.key.set_repeat()

        # Start game
        self.main()

    def main(self):
        """Entry-point into the program."""

        while self.states["QUIT"] != self.program_state:
            # Main menu
            while self.states["MAIN_MENU"] == self.program_state:
                self.main_menu.main_menu()

                # Update frame
                pg.display.flip()
                self.process_quit_events()

            # Options menu
            while self.states["OPTIONS"] == self.program_state:
                self.process_quit_events()

            # Start a new singleplayer
            while self.states["SINGLE_PLAYER"] == self.program_state:
                self.process_quit_events()

            # Host a new multiplayer
            while self.states["HOST_MP"] == self.program_state:
                self.process_quit_events()

            # Join a new multiplayer
            while self.states["JOIN_MP"] == self.program_state:
                self.process_quit_events()

        # Quit pygame
        self.exit_program()

    def exit_program(self):
        """Fully closes the game, anything that needs to be done before shutdown should happen here."""
        pg.quit()

    def process_quit_events(self):
        """Process all of the pygame events pulled from pg.event.get()."""
        # Process pygame events
        for event in pg.event.get():
            # Quit conditions
            if pg.QUIT == event.type:
                self.program_state = self.states["QUIT"]
            elif pg.KEYDOWN == event.type and pg.K_ESCAPE == event.key:
                self.program_state = self.states["QUIT"]


# Keep at the bottom of the script
if __name__ == "__main__":
    game = GameExecutor()
