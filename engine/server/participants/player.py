##########################################################################
# Player: A Participant sub-class where one instance controls the
# interface a player has to interact with their country
##########################################################################

from engine.server.participants.participant import Participant


class Player(Participant):
    def __init__(self, country_obj):
        super().__init__(country_obj)
