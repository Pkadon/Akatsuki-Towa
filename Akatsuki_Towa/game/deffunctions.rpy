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

    def play_music(filename, file_start=None, file_to=None, file_loop=None, loop=True, if_changed=True, **qwargs):
        if filename in bgm_loop_dict:
            if persistent.loop_bgm:
                entry = bgm_loop_dict[filename]

                if entry['from'] and not file_start:
                    file_start = entry["from"]
                if entry['to'] and not file_to:
                    file_to = entry["to"]
                if entry['loop'] and not file_loop:
                    file_loop = entry["loop"]

        tag = '<'
        if file_start:
            tag += f' from {file_start}'
        if file_to:
            tag += f' to {file_to}'
        if file_loop:
            tag += f' loop {file_loop}'
        else:
            tag += f' loop 0.0'
        tag += ' >'

        filename = tag + filename
        renpy.music.play(filename, loop=loop, if_changed=if_changed, **qwargs)
        