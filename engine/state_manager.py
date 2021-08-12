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
        # If I attempted to set the state by typing the values, a typo would possibly not be caught immediately, and cause a headache down the line.
        # By using this system, a typo in the code will return a "dictionary key not found" type of error and the game will not be able to run.

        # Game super states
        self.super_states = {
            "QUIT": "QUIT",
            "LAUNCH_MENU": "LAUNCH_MENU",
            "IN_GAME": "IN_GAME",
        }
        
        # Launch menu states
        self.launch_menu = {
            "MAIN_MENU": "MAIN_MENU",
            "SP": "SP",
            "HOST": "HOST",
            "JOIN": "JOIN",
            "OPTIONS": "OPTIONS",
            "LOAD_SAVE": "LOAD_SAVE",
        }
        
        # In-game states
        self.in_game = {
            "NEW_GAME": "NEW_GAME",
            "PLAY": "PLAY",
            "PAUSE": "PAUSE",
            "PAUSE_MENU": "PAUSE_MENU",
            "SAVING": "SAVING",
            "START_FROM_SAVE": "START_FROM_SAVE",
        }
        
        self.hosting = False
        self.singleplayer = False

    def update_state(self, state):
        """Update the game state and the super-state to match."""
        self.state = state

        # Update super state
        if self.state in self.super_states.values():
            self.super_state = self.state
        elif self.state in self.launch_menu.values():
            self.super_state = self.super_states["LAUNCH_MENU"]
        elif self.state in self.in_game.values():
            self.super_state = self.super_states["IN_GAME"]
        else:
            raise Exception("Invalid state name.")
        
        # Update individual state-related flags
        if self.state == self.launch_menu["MAIN_MENU"]:
            self.hosting = False
            self.singleplayer = False
        elif self.state == self.launch_menu["SP"]:
            self.singleplayer = True
        elif self.state == self.launch_menu["HOST"]:
            self.hosting = True
