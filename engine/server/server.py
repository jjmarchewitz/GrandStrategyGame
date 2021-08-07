##########################################################################
# Server: Represents the game server, and is the backbone of the game in 
# singleplayer and multiplayer
##########################################################################

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
    
    def poll(self):
        pass