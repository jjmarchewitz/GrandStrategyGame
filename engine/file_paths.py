import os

def get_root_folder():
    return os.getcwd()

def get_font_folder():
    game_folder = get_root_folder()
    font_folder = os.path.join(game_folder, "assets", "fonts")
    return font_folder