##########################################################################
# Event Conveniences: Helper functions for dealing with Pygame's event handler
##########################################################################

import pygame as pg
import collections
from .custom_type import CustomType

class EventHandler():
    # Singleton instance
    __instance = None
    @staticmethod
    def get_instance():
        if EventHandler.__instance == None:
            EventHandler()
        return EventHandler.__instance

    def __init__(self):
        if EventHandler.__instance == None:
            EventHandler.__instance = self

        # Define custom event types
        start_menu = CustomType()
        start_menu.event_dict = {
            "MENU_NAME": None,
            "BUTTON_STATES": None,
        }
        in_game_menu = CustomType()
        in_game_menu.event_dict = {
            "MENU_NAME": None,
        }

        self.custom_types = {
            "START_MENU": start_menu,
            "IN_GAME_MENU": in_game_menu,
        }

    def get_event_dict(self, event_type):
        event_dict_copy = self.custom_types[event_type].event_dict.copy()
        return event_dict_copy

    def create_event(self, event_type, event_dict):
        # Check for invalid event type
        if event_type not in self.custom_types.keys():
            raise Exception("Incorrect event type.")

        # Check that the incoming event's dictionary keys are all valid
        for key in event_dict.keys():
            if key not in self.custom_types[event_type].event_dict.keys():
                raise Exception("Incorrect event dictionary.")

        # Create a copy of the event type's dictionary that has every key, even ones unused by event_dict
        complete_event_dict = self.custom_types[event_type].event_dict.copy()

        # Populate the key-value pairs of the complete_event_dict with the pairs from event_dict
        for key in event_dict:
            complete_event_dict[key] = event_dict[key]

        event = pg.event.Event(self.custom_types[event_type].pygame_id, complete_event_dict)

        return event