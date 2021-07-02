##########################################################################
# State manager: houses two main variables controlling the state of the program
##########################################################################

import pygame as pg

class StateManager():
    """A representation of the current state of the game.
    
    The game state can be one of the super states, but not the other way around."""

    # Singleton instance
    __instance = None
    @staticmethod
    def get_instance():
        if StateManager.__instance == None:
            StateManager()
        return StateManager.__instance

    def __init__(self):
        if StateManager.__instance == None:
            StateManager.__instance = self

        # The purpose of these dictionaries is to catch any typos during development.
        # If I attempted to set the state by typing the strings, a typo would possibly not be caught immediately, and cause a headache down the line.
        # By using this system, a typo in the code will return a "dictionary key not found" type of error and the game will not be able to run.

        # Super-states
        self.super = {
            "QUIT": "QUIT",
            "START_MENU": "START_MENU",
            "GAME_RUNNING": "GAME_RUNNING",
        }

        # Main menu states
        self.start_menu = {
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

        self.update_state(self.start_menu["MAIN"])

    def update_state(self, state):
        self.state = state

        if self.state in self.super:
            self.super_state = self.state
        elif self.state in self.start_menu:
            self.super_state = self.super["START_MENU"]
        elif self.state in self.game:
            self.super_state = self.super["GAME_RUNNING"]
        else:
            raise Exception("Invalid state name.")
