"""
Entry-point to the program, execute using

> python game.py

Use --fullscreen to start the game in fullscreen mode
"""

import pygame as pg
import sys
from engine.events.event_handler import EventHandler
from engine.display.launch_menus.launch_menus import LaunchMenu
from engine.display.window import Window
from engine.server.server import Server
from engine.state_manager import StateManager


class GameExecutor():
    """Highest-level instance of the game."""

    def __init__(self):
        """Defining class constants and variables, calling main()."""

        # Initialize pygame modules
        pg.init()
        pg.display.init()
        pg.font.init()
        
        # Process command line arguments (The script name will always be the first arg)
        fullscreen = False
    
        if len(sys.argv) > 1:
            if "--fullscreen" in sys.argv:
                fullscreen = True

        # Window instance (must be first)
        self.window = Window(fullscreen)
        
        # Get singleton instances
        self.event_handler = EventHandler.get_instance()
        self.launch_menu = LaunchMenu.get_instance()
        self.server = Server.get_instance()
        self.state_manager = StateManager.get_instance()

        # Set the game to open the main launch menu
        self.event_handler.create_and_push_state_event(self.state_manager.launch_menu["MAIN_MENU"])
        
        # Set the initial game state
        self.state_manager.update_state(self.state_manager.launch_menu["MAIN_MENU"])

        # Turn off repeated key input
        pg.key.set_repeat()

        # Start game
        self.main()

    def main(self):
        """Entry-point into the program."""

        # Loop until quit condition is met
        while True:
            
            # Get the current event processing function list based on the current super state
            event_processing_function_list = self.get_current_event_processing_function_list()
            
            while True:
                # Get the newest event from the queue
                current_event = pg.event.poll()
                
                # Get the current super state
                current_super_state = self.state_manager.super_state

                # If the event is a quit event, immediately break
                if current_event.type == pg.QUIT:
                    break
                
                # Pass the event to the game executor to update the state
                self.process_event(current_event)
                
                # If the super state has changed after the self.process_event() call, break and update the processing functions list
                if current_super_state != self.state_manager.super_state:
                    event_processing_function_list = self.get_current_event_processing_function_list()

                # Pass the event to the current event processing function list
                for event_processing_function in event_processing_function_list:
                    event_processing_function(current_event)

                # Update the display and queue
                pg.display.flip()
                
            # If the event is a quit event, immediately break
            if current_event.type == pg.QUIT:
                break

        # Quit pygame
        self.exit_program()
        
        
    def process_event(self, event):
        """Check the event for a state update and update the state accordingly."""
        if event.type == self.event_handler.custom_types["UPDATE_GAME_STATE"].pygame_id:
            self.state_manager.update_state(event.__dict__["STATE"])
            
            # if event.__dict__["STATE"] == self.state_manager.in_game["NEW_GAME"]:
                
            
    
    def get_current_event_processing_function_list(self):
        """Return the list of functions that the current event should be passed into based on the current super-state."""
        if self.state_manager.super_state == self.state_manager.super_states["LAUNCH_MENU"]:
            event_processing_functions_list = [
                self.launch_menu.run
            ]
        elif self.state_manager.super_state == self.state_manager.super_states["IN_GAME"]:
            event_processing_functions_list = [
                self.server.run
            ]
            
        return event_processing_functions_list
            

    def exit_program(self):
        """Fully closes the game, anything before shutdown should happen here."""
        pg.quit()




# Keep at the bottom of the script
if __name__ == "__main__":
    game = GameExecutor()
