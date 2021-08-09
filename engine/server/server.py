##########################################################################
# Server: Represents the game server, and is the backbone of the game in 
# singleplayer and multiplayer
##########################################################################

from engine.core.countries.country_manager import CountryManager

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
        
        for country_tag in self.country_manager.countries.keys():
            # TODO: Update the value of this with an actual bot object
            self.participants.update({country_tag: "BOT_OBJECT_WITH_COUNTRY_PASSED_IN"})
        
        
            
    
    def poll(self):
        pass