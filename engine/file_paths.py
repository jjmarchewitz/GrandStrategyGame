def get_root_folder():
    return __file__.split("engine")[0]

def get_font_folder():
    game_folder = get_root_folder()

    if "\\" in game_folder:
        slash_char = "\\"
    elif "/" in game_folder:
        slash_char = "/"
    else:
        raise Exception("OS-appropriate slash character not detected.")

    font_folder = game_folder + "assets" + slash_char + "fonts" + slash_char

    return font_folder