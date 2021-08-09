##########################################################################
# Server: Represents the game server, and is the backbone of the game in 
# singleplayer and multiplayer
##########################################################################

from engine.core.countries.country_manager import CountryManager
from engine.server.participants.bot import Bot

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
            
        self.country_manager = CountryManager.get_instance()
            
        self.participants = {}
        
        # Initialize all countries with bots
        for country_tag, country_obj in self.country_manager.countries.items():
            self.participants.update({country_tag: Bot(country_obj)})
        
        
            
    
    def poll(self):
        pass