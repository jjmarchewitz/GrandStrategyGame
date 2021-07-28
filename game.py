"""
Entry-point to the program, execute using

> python main.py

TODO Update if any arguments are needed
"""

from engine.events.event_handler import EventHandler
import pygame as pg
from game_window.window import Window
from game_window.start_menus.start_menu import StartMenu


class GameExecutor():
    """Highest-level instance of the game."""

    def __init__(self):
        """Defining class constants and variables, calling main()."""

        # Initialize pygame objects
        pg.init()
        pg.display.init()
        pg.font.init()

        # Get singleton instances
        self.event_handler = EventHandler.get_instance()
        self.window = Window.get_instance()
        self.start_menu = StartMenu.get_instance()

        # Set the game to open the start menu
        main_menu_event = self.event_handler.create_event("START_MENU", {"MENU_NAME": "MAIN"})
        pg.event.post(main_menu_event)

        # Turn off repeated key input
        pg.key.set_repeat()

        # Start game
        self.main()

    def main(self):
        """Entry-point into the program."""

        # Loop until quit condition is met
        while True:
            # Get the newest event from the queue
            current_event = pg.event.poll()
            
            # If the event is a quit event, immediately break
            if current_event.type == pg.QUIT:
                break

            # Check the event in the start menu
            self.start_menu.start_menu(current_event)

            # Update the display and queue
            pg.display.flip()
            
        # Quit pygame
        self.exit_program()

    def exit_program(self):
        """Fully closes the game, anything that needs to be done before shutdown should happen here."""
        pg.quit()

    


# Keep at the bottom of the script
if __name__ == "__main__":
    game = GameExecutor()
