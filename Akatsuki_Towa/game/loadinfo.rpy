init -3 python: 
    import json
    import csv

    def jsonloader(filename, rowkey, idkey, stringkey, encode):
        d = dict()
        with renpy.open_file(filename, encoding=encode, directory='MonoBehaviour') as txt:
            text_json = json.load(txt)
            for row in range(0, len(text_json[rowkey])):
                row = text_json[rowkey][row]

                try: textid = int(row[idkey])
                except: textid = row[idkey]

                textstring = str(row[stringkey]).replace('\r', '')
                    
                d[textid] = textstring
        return d
                    
    def csvloader(filename, idkey, stringkey, encode):
        #try to check for utf-8 sig encoding
        if encode == "utf-8":
            with renpy.open_file(filename, directory='MonoBehaviour') as txt:
                if txt.read(3) == b'\xef\xbb\xbf': encode = 'utf-8-sig'

        d = dict()
        with renpy.open_file(filename, encoding=encode, directory='MonoBehaviour') as txt:
            reader = csv.reader(txt)

            #get list of headers
            for row in reader:
                headers = row
                break

            #find string id position
            idpos = headers.index(idkey)

            #find string position
            stringpos = headers.index(stringkey)

            for row in reader:
                try: textid = int(row[idpos])
                except: textid = row[idpos]

                if len(row) > stringpos:
                    textstring = str(row[stringpos])
                else:
                    textstring = ''

                d[textid] = textstring
        return d
        
    def bytesreader(filename, type='text'):
        import codecs
        import struct

        d = dict()
        with renpy.open_file(filename, directory='MonoBehaviour') as txt:
            txt = txt.read()
            is_kor = False

            pos = 4
            entry_count = struct.unpack_from('<i', txt, pos)[0]
            pos += 4
            for entry in range(0, entry_count):
                textlength = struct.unpack_from('<h', txt, pos)[0]
                pos += 2
                textstring = txt[pos:(pos+textlength)].decode('utf-8').replace('\r', '')
                pos += textlength
                if type == 'role':
                    #Skip over string length int, string, _scale int, _xPostion int
                    folderlength = struct.unpack_from('<h', txt, pos)[0]
                    pos += 2
                    pos += folderlength
                    pos += 8

                    #Korean avg_role has an extra 4-byte int to skip over before reaching the id.
                    #The first entry of all avg_role files in all languages on all platforms is Nacht (id 1)
                    #This is to check if we are at the id (pc/chinese mobile) or if there is an unexpected value (kr)
                    if entry == 0:
                        if txt[pos:pos+4] == b'\x01\x00\x00\x00': 
                            is_kor = False
                        else: 
                            is_kor = True

                    if is_kor:
                        pos += 4

                textid = struct.unpack_from('<i', txt, pos)[0]
                pos += 4
                d[textid] = textstring
        return d

    def colortext(string, color):

        prefix = f'[{color}]'
        suffix = '[-]'

        #remove original prefix
        if string.startswith(prefix): string = string[len(prefix):]
        #remove original suffix
        if string.endswith(suffix): string = string[:-len(suffix)]

        #add renpy color text tag
        if '{color=' not in string:
            string = ('{color='+color+'}'+string+'{/color}')

        return string

    #==============================================================================

    #LOAD MENU DATA
    with renpy.open_file('episodelist.json', encoding="utf-8") as txt:
        combined_data = json.load(txt)
    menudata = combined_data['menudata']
    questlog_data = combined_data['questlog_data']

    #Load the list of loop points to use for looping the bgm
    with renpy.open_file('bgm.json', encoding='utf-8') as txt:
        bgm_loop_dict = json.load(txt)

    #==============================================================================

    #LOAD SCRIPT FILES
    avgroledict = dict()
    textdict = dict()
    def load_text(lang):
        avgroledict[lang] = dict()
        textdict[lang] = dict()

        #LOAD AVG ROLE FILE
        if namefilename[lang].endswith('.json'):
            avgroledict[lang] = jsonloader(namefilename[lang], namerowkey[lang], nameidkey[lang], namekey[lang], nameencode[lang])
        elif namefilename[lang].endswith('.csv'):
            avgroledict[lang] = csvloader(namefilename[lang], nameidkey[lang], namekey[lang], nameencode[lang])
        elif namefilename[lang].endswith('.bytes') or namefilename[lang].endswith('.bin'):
            avgroledict[lang] = bytesreader(namefilename[lang], type='role')

        #LOAD SCRIPT FILE
        if textfilename[lang].endswith('.json'):
            textdict[lang] = jsonloader(textfilename[lang], textrowkey[lang], textidkey[lang], textkey[lang], textencode[lang])
        elif textfilename[lang].endswith('.csv'):
            textdict[lang] = csvloader(textfilename[lang], textidkey[lang], textkey[lang], textencode[lang])
        elif textfilename[lang].endswith('.bytes') or textfilename[lang].endswith('.bin'):
            textdict[lang] = bytesreader(textfilename[lang], type='text')

        #COMBINE EXTRA STRING DICTIONARY
        # Do not do any special compensating for missing strings.
        # if a string is missing from a different language, it can always be added.
        if lang in extextdict:
            for key in extextdict[lang]:
                if key not in textdict[lang]:
                    textdict[lang][key] = extextdict[lang][key]

        #FIX SCRIPT FORMATTING
    
        #change the text color formatting to show up correctly in renpy
        #the original formatting looks like: "[339944]「……………………」[-]"
        #where "339944" is a hex color code
        #known examples: 麻薬密売調査(1) 5/6 (avg10388)

        #color these dialogue strings green:
        for strid in [1132448, 1132458, 1132463]:
            if strid in textdict[lang]:
                textdict[lang][strid] = colortext(textdict[lang][strid], '339944')

        #color these dialogue strings blue:
        for strid in [1132449, 1132459, 1132464]:
            if strid in textdict[lang]:
                textdict[lang][strid] = colortext(textdict[lang][strid], '334499')

        #one last color tag that's in the middle of the string...
        if 90224 in textdict[lang]:
            text = textdict[lang][90224]
            textdict[lang][90224] = text.replace(r"[FF0000]", r"{color=FF0000}").replace(r"[-]", r"{/color}")

        #FIX TYPOS
        #Maison Imelda quest dialogue instead mentions Geofront B1 Sector
        if 1000499 in textdict[lang]:
            textdict[lang][1000499] = textdict[lang][1000499].replace('ジオフロントＢ１区画', '《メゾン・イメルダ》')
        if 1000500 in textdict[lang]:
            textdict[lang][1000500] = textdict[lang][1000500].replace('ジオフロントＢ１区画', '《メゾン・イメルダ》')

        #Typo that was found to have been fixed in one of the mobile version.
        if 1182028 in textdict[lang]:
            textdict[lang][1182028] = textdict[lang][1182028].replace('公演', '公園')

        #ジオフロントの再調査 is labeled 1/2 when it should be 1/1
        if 17579 in textdict[lang]:
            if textdict[lang][17579].endswith('1/2'):
                textdict[lang][17579] = textdict[lang][17579][:-3] + '1/1'

        #Preston and Hogarth dialogue is all mixed up
        #Swap the names around, keeping the titles the same
        if 1001682 in textdict[lang]:
            textdict[lang][1001682] = textdict[lang][1001682].replace('プレストン司令', 'ホガース司令').replace('プレストン専務', 'ホガース常務')
        if 1001683 in textdict[lang]:
            textdict[lang][1001683] = textdict[lang][1001683].replace('ホガース局長', 'プレストン局長').replace('ホガース常務', 'プレストン専務')

        #Dialogue in avg 10415 (《エルフェンテック》社の危機(2) 1/2) missing a line break
        if 1140827 in textdict[lang]:
            textdict[lang][1140827] = textdict[lang][1140827].replace('。', '。\n　')

    #==============================================================================

    #DEFINE RENPY SPEAKERS
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

    def load_roles(lang):
        for id in avgroledict[lang]:
            define_character(lang, avgroledict[lang][id], f'c{id}1', namebox_xalign=0.02)
            define_character(lang, avgroledict[lang][id], f'c{id}3', namebox_xalign=0.98)

define config.all_character_callbacks = [typewriter]

init python:

    ### need to keep a character with id "nobody" for possible compatibility issues
    define_character(lang=None, name=None, char_id='nobody')

    ### This is a free no-nameplate speaker with white text used in spritetest.
    ### There needs to be a Character object with char_id=None somewhere in the script
    ### so it can be used as the default value to reset the narrator, so it is not 
    ### recommended to delete this without replacing it somewhere else first.
    define_character(lang=None, name=None, char_id=None)

    ###for no-nameplate messages with green text
    define_character(lang=None, name=None, char_id='c0', what_color='#4FFFB0')

    #==============================================================================
    
    loaded_languages = []
    # Startup loading
    def init_language(lang):
        global loaded_languages

        if lang not in loaded_languages:
            load_text(lang)
            load_roles(lang)
            loaded_languages.append(lang)

    if preferences.language:
        init_language(preferences.language)
    else:
        init_language(config.default_language)