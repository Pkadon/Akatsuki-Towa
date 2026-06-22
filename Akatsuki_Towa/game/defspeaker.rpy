init -3 python:
    char_dict = dict()
    for lang in language_list:
        char_dict[lang] = dict()

    def define_character(lang, name, char_id, **kwargs):

        ### show_char_id is needed to be able to pass the char_id to the say screen
        ### so that it can update the narrator.
        char_obj = Character(name, show_char_id=char_id, **kwargs)

        if lang:
            char_dict[lang][char_id] = char_obj
        else:
            char_dict[char_id] = char_obj

    def init_roles():
        for lang in language_list:
            for id in avgroledict[lang]:
                define_character(lang, avgroledict[lang][id], f'c{id}1', namebox_xalign=0.02)
                define_character(lang, avgroledict[lang][id], f'c{id}3', namebox_xalign=0.98)

        ### need to keep a character with id "nobody" for possible compatibility issues
        define_character(lang=None, name=None, char_id='nobody')

        ### This is a free no-nameplate speaker with white text used in spritetest.
        ### There needs to be a Character object with char_id=None somewhere in the script
        ### so it can be used as the default value to reset the narrator, so it is not 
        ### recommended to delete this without replacing it somewhere else first.
        define_character(lang=None, name=None, char_id=None)

        ###for no-nameplate messages with green text
        define_character(lang=None, name=None, char_id='c0', what_color='#4FFFB0')

define config.all_character_callbacks = [typewriter]

init python:
    init_roles()
