##########################################################################
# Country Manager: Stores and controls all of the country instances
##########################################################################

from engine.core.countries.country import Country

class CountryManager():
    """Represents the game server."""
    
    # Singleton instance
    __instance = None
    @staticmethod
    def get_instance():
        if CountryManager.__instance == None:
            CountryManager()
        return CountryManager.__instance
    
    def __init__(self):
        if CountryManager.__instance == None:
            CountryManager.__instance = self
            
            self.countries = {
                "A": Country("A"),
                "B": Country("B"),
                "C": Country("C"),
            }