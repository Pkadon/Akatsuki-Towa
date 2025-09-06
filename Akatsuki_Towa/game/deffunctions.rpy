init python:

    def convertstrid(key):
        if key in textdict:
            return textdict[key]
        else:
            return str(key)

    def update_portrait(portrait, alias, atlist, z):
        if renpy.showing(alias):
            renpy.hide(alias)
        renpy.show(portrait, at_list=atlist, tag=alias, zorder=z)

    # During screen transitions, renpy sets the speaking character to the default narrator, which hides the namebox.
    # This is used to set narrator to the LAST speaker during the fade-out (from within the say screen in screens.rpy), 
    # and then to the NEXT speaker during the fade-in (from the cutscene script itself) for a smoother-looking transition.
    def update_narrator(char_id):
        if not renpy.predicting():
            global narrator
            narrator = char_dict[char_id]

    def play_music(filename):
        renpy.music.play(filename)