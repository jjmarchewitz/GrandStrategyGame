##########################################################################
# State manager: houses two main variables controlling the state of the program
##########################################################################

import pygame as pg

class State():
    """A representation of the current state of the game.
    
    The game state can be one of the super states, but not the other way around."""

    # Singleton instance
    __instance = None
    @staticmethod
    def get_instance():
        if State.__instance == None:
            State()
        return State.__instance

    def __init__(self):
        if State.__instance == None:
            State.__instance = self

        # The purpose of these dictionaries is to catch any typos during development.
        # If I attempted to set the state by typing the strings, a typo would possibly not be caught immediately, and cause a headache down the line.
        # By using this system, a typo in the code will return a "dictionary key not found" type of error and the game will not be able to run.

        # Super-states
        self.super = {
            "QUIT": "QUIT",
            "MAIN_MENU": "MAIN_MENU",
            "GAME_RUNNING": "GAME_RUNNING",
        }

        # Main menu states
        self.main_menu = {
            "MAIN": "MAIN",
            "SP": "SP",
            "HOST": "HOST",
            "JOIN": "JOIN",
            "OPTIONS": "OPTIONS",
        }

        # In-game states
        self.game = {
            "LOAD": "LOAD",
            "PLAY": "PLAY",
            "PAUSE": "PAUSE",
            "PAUSE_MENU": "PAUSE_MENU",
            "SAVING": "SAVING",
            "EXIT_TO_MAIN": "EXIT_TO_MAIN",
        }

        self.update_state(self.main_menu["MAIN"])

    def update_state(self, state):
        self.state = state

        if self.state in self.super:
            self.super_state = self.state
        elif self.state in self.main_menu:
            self.super_state = self.super["MAIN_MENU"]
        elif self.state in self.game:
            self.super_state = self.super["GAME_RUNNING"]
        else:
            raise Exception("Invalid state name.")

    def update_game(self):
        """Process events and refresh the display."""
        self.process_events()
        self.refresh_display()

    def process_events(self):
        """Process all of the pygame events pulled from pg.event.get()."""
        # Process pygame events
        for event in pg.event.get():
            # Quit conditions
            if pg.QUIT == event.type:
                self.state = self.super["QUIT"]

    def refresh_display(self):
        """Update the display."""
        pg.display.flip()
