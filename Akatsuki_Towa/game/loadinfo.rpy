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

    #LOAD MENU DATA
    menudata = dict()
    with renpy.open_file('episodelist.json', encoding="utf-8") as txt:
        menudata = json.load(txt)

    avgroledict = dict()
    textdict = dict()
    for lang in language_list:

        avgroledict[lang] = dict()
        textdict[lang] = dict()

        #LOAD AVG ROLE FILE
        if namefilename[lang].endswith('.json'):
            avgroledict[lang] = jsonloader(namefilename[lang], namerowkey[lang], nameidkey[lang], namekey[lang], nameencode[lang])
        elif namefilename[lang].endswith('.csv'):
            avgroledict[lang] = csvloader(namefilename[lang], nameidkey[lang], namekey[lang], nameencode[lang])

        #LOAD SCRIPT FILE
        if textfilename[lang].endswith('.json'):
            textdict[lang] = jsonloader(textfilename[lang], textrowkey[lang], textidkey[lang], textkey[lang], textencode[lang])
        elif textfilename[lang].endswith('.csv'):
            textdict[lang] = csvloader(textfilename[lang], textidkey[lang], textkey[lang], textencode[lang])

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

    #Load the list of loop points to use for looping the bgm
    with renpy.open_file('bgm.json', encoding='utf-8') as txt:
        bgm_loop_dict = json.load(txt)
