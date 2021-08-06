from dataclasses import dataclass
from typing import Any
import pygame as pg

@dataclass
class Colors():
    """Dataclass to store common colors for the game."""
    
    # These colors should not be used for any actual coloring, and instead are reserved for
    # use as background colors on surfaces that need a transparent background. These serve
    # the function of green in green screens
    background_for_transparent_color_keying_1: Any = pg.Color("0x000000")
    background_for_transparent_color_keying_2: Any = pg.Color("0xFFFFFF")
    background_for_transparent_color_keying_3: Any = pg.Color("0xAAAAAA")
    
    # Colors intended for general use throughout the game
    black: Any = pg.Color("0x161616")
    grey: Any = pg.Color("0x525252")
    white: Any = pg.Color("0xe7e7e7")
    dark_red: Any = pg.Color("0x471e1b")
    rust: Any = pg.Color("0x91362e")
    red: Any = pg.Color("0xc63c3c")
    dark_brown: Any = pg.Color("0x5e2f0f")
    light_brown: Any = pg.Color("0x93530e")
    orange: Any = pg.Color("0xfb9e27")
    relish: Any = pg.Color("0x4d4519")
    dark_yellow: Any = pg.Color("0x7f7024")
    light_yellow: Any = pg.Color("0xddc410")
    dark_green: Any = pg.Color("0x2d4c23")
    cactus_green: Any = pg.Color("0x4e9142")
    lime: Any = pg.Color("0x75db60")
    dark_turquoise: Any = pg.Color("0x1b4a48")
    cyan: Any = pg.Color("0x198089")
    blue: Any = pg.Color("0x12c7e0")
    dark_purple: Any = pg.Color("0x423d76")
    violet: Any = pg.Color("0x5e4b9d")
    lilac: Any = pg.Color("0x7a7ae0")
    eggplant: Any = pg.Color("0x593558")
    magenta: Any = pg.Color("0x944997")
    pink: Any = pg.Color("0xde43d8")