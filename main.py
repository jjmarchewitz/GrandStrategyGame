"""
Entry-point to the program, execute using

> python main.py

TODO Update if any arguments are needed
"""

import pdb
# pdb.set_trace()

import pygame as pg
from pygame.locals import *
from window import window


class GameExecutor():
    """Highest-level instance of the game."""

    def __init__(self):
        """Defining class constants and variables, calling main()."""
        self.states = {
            "QUIT": 0,
            "MENU": 1,
            "GAME": 2,
        }

        # Set the state to be in the menu
        self.program_state = self.states["MENU"]

        # Initialize pygame
        pg.init()
        pg.key.set_repeat()

        # Initialize the game window
        self.window = window.Window()

        # Start game
        self.main()

    def main(self):
        """Entry-point into the program."""
        # Menu loop
        while self.states["MENU"] == self.program_state:
            self.process_quit_events()

        # Game loop
        while self.states["GAME"] == self.program_state:
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
