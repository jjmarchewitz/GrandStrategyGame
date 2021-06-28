"""
Entry-point to the program, execute using

> python main.py

TODO Update if any arguments are needed
"""

import pygame as pg
from engine.state import State
from game_window.window import Window
from game_window.main_menu.main_menu import MainMenu


class GameExecutor():
    """Highest-level instance of the game."""

    def __init__(self):
        """Defining class constants and variables, calling main()."""

        # Initialize pygame objects
        pg.init()
        pg.display.init()
        pg.font.init()

        # Get singleton instances
        self.state = State.get_instance()
        self.window = Window.get_instance()
        self.main_menu = MainMenu.get_instance()

        # Set the state to be in the menu
        self.state.update_state(self.state.main_menu["MAIN"])

        # Turn off repeated key input
        pg.key.set_repeat()

        # Start game
        self.main()

    def main(self):
        """Entry-point into the program."""

        # Loop until quit condition is met
        while self.state.super["QUIT"] != self.state.super_state:
            # Show main menu
            if self.state.super["MAIN_MENU"] == self.state.super_state:
                self.main_menu.main_menu()
 
        # Quit pygame
        self.exit_program()

    def exit_program(self):
        """Fully closes the game, anything that needs to be done before shutdown should happen here."""
        pg.quit()

    


# Keep at the bottom of the script
if __name__ == "__main__":
    game = GameExecutor()
