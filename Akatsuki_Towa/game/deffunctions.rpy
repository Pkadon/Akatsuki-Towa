init -3 python:

    def convertstrid(key):
        if key in textdict[preferences.language]:
            text = textdict[preferences.language][key]
        else:
            text = str(key)

        #Disable OpenType font ligatures.
        tagged = ('{feature:liga=0}' + text + '{/feature}')

        return tagged

    def convertroleid(key):
        if key in avgroledict[preferences.language]:
            text = avgroledict[preferences.language][key]
        else:
            text = str(key)

        return text

    def update_portrait(portrait, alias, atlist, z):
        if renpy.showing(alias):
            renpy.hide(alias)
        renpy.show(portrait, at_list=atlist, tag=alias, zorder=z)

    # Used to pass extra fields to the history screen from the say screen by proxy.
    def arg(line_id, str_id, size=1.0):
        global last_label
        ret_dict = {
            'show_line_id': line_id,
            'show_str_id': str_id,
            'show_label': last_label,
            'what_size': (gui.text_size * size)
        }
        return ret_dict

    def get_char(char_id):
        if char_id in char_dict[preferences.language]: 
            return char_dict[preferences.language][char_id]
        elif char_id in char_dict: 
            return char_dict[char_id]
        else:
            return char_id

    # During screen transitions, renpy sets the speaking character to the default narrator, which hides the namebox.
    # This is used to set narrator to the LAST speaker during the fade-out (from within the say screen in screens.rpy), 
    # and then to the NEXT speaker during the fade-in (from the cutscene script itself) for a smoother-looking transition.
    def update_narrator(char_id):
        if not renpy.predicting():
            global narrator
            narrator = get_char(char_id)

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

    def change_language(lang):
        init_language(lang)

        renpy.change_language(lang, force=True, rebuild=True)

    #Opening a menu in the middle of a cutscene can make the "typewriter" sound effect get stuck on loop, so this makes sure it stops.
    def mute_typewriter():
        global typewriter_channels

        for ch in typewriter_channels:
            renpy.music.stop(channel=ch)
        
    def calculate_text_size(text):
        if isinstance(text, str):
            text = Text(text)
        return text.size()