"""
Entry-point to the program, execute using

> python main.py

TODO: Update if any arguments are needed
"""

import pygame as pg
from dataclasses import dataclass, field
from engine.events.event_handler import EventHandler
from engine.state_manager import StateManager
from game_window.window import Window
from game_window.launch_menus.launch_menus import LaunchMenu
    

class GameExecutor():
    """Highest-level instance of the game."""

    def __init__(self):
        """Defining class constants and variables, calling main()."""

        # Initialize pygame objects
        pg.display.init()
        pg.font.init()

        # Get singleton instances
        self.event_handler = EventHandler.get_instance()
        self.launch_menu = LaunchMenu.get_instance()
        self.state_manager = StateManager.get_instance()
        self.window = Window.get_instance()

        # Set the game to open the start menu
        main_menu_event = self.event_handler.create_state_event(self.state_manager.launch_menu["MAIN_MENU"])
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

            # Pass the event to the launch menu
            self.launch_menu.run(current_event)
            
            # Pass the event to the game executor to update the state
            self.process_event(current_event)

            # Update the display and queue
            pg.display.flip()

        # Quit pygame
        self.exit_program()
        
        
    def process_event(self, event):
        """Check the event for a state update and update the state accordingly."""
        if event.type == self.event_handler.custom_types["UPDATE_GAME_STATE"]:
            self.state_manager.update_state(event.__dict__["STATE"])
            

    def exit_program(self):
        """Fully closes the game, anything before shutdown should happen here."""
        pg.quit()




# Keep at the bottom of the script
if __name__ == "__main__":
    game = GameExecutor()
