##########################################################################
# Custom Type: A class to hold a custom event type and associated data
##########################################################################

import pygame as pg

class CustomType():
    def __init__(self):
        self.pygame_id = pg.event.custom_type()
        self.event_dict = {}