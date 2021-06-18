##########################################################################
# Entry-point to the program, execute using
#
# > python main.py
#
# TODO Update if any arguments are needed
##########################################################################

import pygame as pg
from pygame.locals import *
from WindowSettings import *


class GameExecutor():
    """Highest-level instance of the game."""

    def __init__(self):
        """Defining class constants and variables, calling main()."""
        self.WINDOW_WIDTH = 500
        self.WINDOW_HEIGHT = 500
        self.program_running = True

        self.main()

    def main(self):
        """Entry-point into the program."""
        # Initialize pygame
        pg.init()

        # Verify that pygame initialized correctly
        if not pg.display.get_init():
            raise SystemError("Display module did not properly initialize.")

        # Open a new window at the desired dimensions and set its properties
        pg.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pg.display.set_caption("Game")

        # Main display loop
        while self.program_running:
            self.process_pygame_events()

        # Quit pygame
        pg.quit()

    def process_pygame_events(self):
        """Process all of the pygame events pulled from pg.event.get()."""
        # Process pygame events
        for event in pg.event.get():
            # Quit condition
            if event.type is pg.QUIT:
                self.program_running = False


# Keep at the bottom of the script
if __name__ == "__main__":
    game = GameExecutor()
