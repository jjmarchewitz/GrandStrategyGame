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
        self.states = {
            "QUIT": 0,
            "MAIN_MENU": 1,
            "OPTIONS": 2,
            "SINGLE_PLAYER": 3,
            "HOST_MP": 4,
            "JOIN_MP": 5,
        }

        # Set the state to be in the menu
        self.program_state = self.states["MAIN_MENU"]

        # Initialize pygame
        pg.init()
        pg.key.set_repeat()

        # Initialize the game window
        self.window = window.Window()

        # Start game
        self.main()

    def main(self):
        """Entry-point into the program."""

        while self.states["QUIT"] != self.program_state:
            # Main menu
            while self.states["MAIN_MENU"] == self.program_state:
                self.window.main_menu()

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
            # Quit condition
            if pg.QUIT == event.type:
                self.program_state = self.states["QUIT"]


# Keep at the bottom of the script
if __name__ == "__main__":
    game = GameExecutor()
