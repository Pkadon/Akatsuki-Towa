init python:

    def convertstrid(key):
        if key in textdict:
            text = textdict[key]
        else:
            text = str(key)

        #Disable OpenType font ligatures.
        tagged = ('{feature:liga=0}' + text + '{/feature}')

        return tagged

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


    # Used to make it possible to cleanly loop the music
    # bgm_loop_dict is loaded in loadinfo.rpy from bgm.json
    # persistent.loop_bgm is defined in options.rpy, under "Preference defaults"

    def play_music(filename, start=None, to=None, loop=None, **qwargs):
        if filename in bgm_loop_dict:
            if persistent.loop_bgm:
                entry = bgm_loop_dict[filename]

                if entry['from'] and not start:
                    start = entry["from"]
                if entry['to'] and not to:
                    to = entry["to"]
                if entry['loop'] and not loop:
                    loop = entry["loop"]

        tag = '<'
        if start:
            tag += f' from {start}'
        if to:
            tag += f' to {to}'
        if loop:
            tag += f' loop {loop}'
        else:
            tag += f' loop 0.0'
        tag += '>'

        filename = tag + filename
        renpy.music.play(filename, loop=True, **qwargs)
        