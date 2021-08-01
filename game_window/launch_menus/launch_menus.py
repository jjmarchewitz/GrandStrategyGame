"""
Start menu: handles main menu and sub-menus
"""

from engine.state_manager import StateManager
import pygame as pg
from .menus import DummyMenu, MainMenu
from engine.events.event_handler import EventHandler
from game_window.window import Window


class LaunchMenu():
    # Singleton instance
    __instance = None
    def get_instance():
        if LaunchMenu.__instance == None:
            LaunchMenu()
        return LaunchMenu.__instance

    def __init__(self):
        # Create singleton instance
        if LaunchMenu.__instance == None:
            LaunchMenu.__instance = self

        # Grab singleton instances
        self.event_handler = EventHandler.get_instance()
        self.state_manager = StateManager.get_instance()
        self.window = Window.get_instance()

        self.menus = {
            self.state_manager.launch_menu["MAIN_MENU"]: MainMenu(),
            self.state_manager.launch_menu["SP"]: DummyMenu(),
            self.state_manager.launch_menu["HOST"]: DummyMenu(),
            self.state_manager.launch_menu["JOIN"]: DummyMenu(),
            self.state_manager.launch_menu["OPTIONS"]: DummyMenu(),
        }

        self.current_menu = None

    def run(self, current_event = None):
        """Execute the main menu logic, including calling any sub-menus."""

        # Check if the current event is a start menu change
        if current_event != None:
            if current_event.type == self.event_handler.custom_types["UPDATE_GAME_STATE"].pygame_id:
                if current_event.__dict__["STATE"] in self.state_manager.launch_menu.values():
                    self.window.clear()
                    self.current_menu = self.menus[current_event.__dict__["STATE"]]
                    self.current_menu.draw()

        if self.current_menu != None:
            # Update the menu to be the correct one
            self.current_menu.check()