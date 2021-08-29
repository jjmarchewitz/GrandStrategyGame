import os


def get_root_folder():
    return os.getcwd()


def get_font_folder():
    return os.path.join(get_root_folder(), "assets", "fonts")


def get_images_folder():
    return os.path.join(get_root_folder(), "assets", "images")


def get_sounds_folder():
    return os.path.join(get_root_folder(), "assets", "sounds")


def get_flavor_folder():
    return os.path.join(get_root_folder(), "flavor")


def get_map_data_folder():
    return os.path.join(get_root_folder(), "map")


def get_save_game_folder():
    return os.path.join(get_root_folder(), "save_games")
