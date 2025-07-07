#################################################################

# This changes the persistent file location from the "%APPDATA%/Renpy" folder to the game's install folder.
# This is specifically necessary, because the current menu code is incompatible with 
# some of the cached data from older versions of the game.  
# This should let each new version create its own fresh saves folder, instead of snowballing.
init python early:
        config.save_directory = None

init python:
    config.has_autosave = False
    config.has_quicksave = False
    config.autosave_on_quit = False
    config.autosave_on_choice = False
    config.save = False

    config.window_show_transition = None

#################################################################
label start:
return

label avg0:
return