##########################################################################
# Client: represents a client-side user of the game, is always tied to
# exactly one Player on the server side
##########################################################################

from engine.server.server import Server


class Client:
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

        # Singleton instances
        self.server = Server.get_instance()

        self.country_tag = "A"
        self.player = self.server.add_player(self.country_tag)
        self.country = self.player.country

    def run(self, event):
        """Runs all client-side functionality, including the display and interaction with the Player object."""
        pass
