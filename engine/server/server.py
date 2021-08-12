##########################################################################
# Server: Represents the game server, and is the backbone of the game in 
# singleplayer and multiplayer
##########################################################################

from dataclasses import dataclass
from engine.core.countries.country_manager import CountryManager
from engine.state_manager import StateManager
from engine.server.participants.bot import Bot
from engine.server.participants.player import Player

@dataclass
class GameSpeeds():
    paused: int = 0
    one: int = 1
    two: int = 2
    three: int = 3
    four: int = 4

class Server():
    """Represents the game server."""
    
    # Singleton instance
    __instance = None
    @staticmethod
    def get_instance():
        if Server.__instance == None:
            Server()
        return Server.__instance
    
    def __init__(self):
        if Server.__instance == None:
            Server.__instance = self
            
        # Get singleton instances
        self.country_manager = CountryManager.get_instance()
        self.state_manager = StateManager.get_instance()
            
        self.participants = {}
        
        self.game_speeds = GameSpeeds()
        
        self.speed = self.game_speeds.paused
        
        # Initialize all countries with bots
        for country_tag, country_obj in self.country_manager.countries.items():
            self.participants.update({country_tag: Bot(country_obj)})
            
        
    def run(self, event):
        pass
   
    
    def add_player(self, tag):
        """Replace a Bot object with a Player at the given country tag."""
        retval = None
        if tag != None:
            self.participants.update({tag: Player(self.country_manager.countries[tag])})
            retval = self.participants[tag]
        return retval
      
        
    def remove_player(self, tag):
        self.participants.update({tag: Bot(self.country_manager.countries[tag])})