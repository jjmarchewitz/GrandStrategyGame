##########################################################################
# Client: represents a client-side user of the game, is always tied to 
# exactly one Player on the server side
##########################################################################

class Client():
    """Represents a client-side user of the game, is always tied to exactly one Player on the server side."""
    
    # Singleton instance
    __instance = None
    @staticmethod
    def get_instance():
        if Client.__instance == None:
            Client()
        return Client.__instance
    
    def __init__(self):
        if Client.__instance == None:
            Client.__instance = self
    
    def run(self):
        """Runs all client-side functionality, including the display and interaction with the Player object."""
        pass