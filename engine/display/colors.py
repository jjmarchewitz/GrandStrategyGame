from dataclasses import dataclass
from typing import Any
import pygame as pg


@dataclass
class Colors:
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
    white: Any = pg.Color("0xE7E7E7")
    dark_red: Any = pg.Color("0x471E1B")
    rust: Any = pg.Color("0x91362E")
    red: Any = pg.Color("0xC63C3C")
    dark_brown: Any = pg.Color("0x5E2F0F")
    light_brown: Any = pg.Color("0x93530E")
    orange: Any = pg.Color("0xFB9E27")
    relish: Any = pg.Color("0x4D4519")
    dark_yellow: Any = pg.Color("0x7F7024")
    light_yellow: Any = pg.Color("0xDDC410")
    dark_green: Any = pg.Color("0x2D4C23")
    cactus_green: Any = pg.Color("0x4E9142")
    lime: Any = pg.Color("0x75DB60")
    dark_turquoise: Any = pg.Color("0x1B4A48")
    cyan: Any = pg.Color("0x198089")
    blue: Any = pg.Color("0x12C7E0")
    dark_purple: Any = pg.Color("0x423D76")
    violet: Any = pg.Color("0x5E4B9D")
    lilac: Any = pg.Color("0x7A7AE0")
    eggplant: Any = pg.Color("0x593558")
    magenta: Any = pg.Color("0x944997")
    pink: Any = pg.Color("0xDE43D8")
