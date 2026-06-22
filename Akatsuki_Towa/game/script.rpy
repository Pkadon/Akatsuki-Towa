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
    config.play_channel = "audio"
    config.window_show_transition = None
    config.clear_history_on_language_change = False

    style.default.prefer_emoji = False

    def copy_text_to_clipboard(text):
        import pygame.scrap
        pygame.scrap.put(pygame.SCRAP_TEXT, text.encode("utf-8"))

        renpy.notify("Copied to clipboard!")
    config.hyperlink_handlers = { 'copy' : copy_text_to_clipboard }
    #Then this creates a text tag that can be used like:
    #    "{a=copy:TEXT TO COPY GOES HERE}Click me to copy my text!{/a}"

    #Stores last visited label
    #taken from here: https://lemmasoft.renai.us/forums/viewtopic.php?p=137416#p137416
    def label_callback(name, abnormal):
        global last_label
        if name.startswith('_'): return
        last_label = name
    config.label_callback = label_callback
default last_label = None
        

#################################################################
label start:
return

label avg0:
return