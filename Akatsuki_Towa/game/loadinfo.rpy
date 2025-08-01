python early:
    import json
    import csv

    with renpy.open_file('episodelist.json', encoding="utf-8") as txt:
        menudata = json.load(txt)

    def jsonloader(filename, rowkey, idkey, stringkey, encode):
        d = dict()
        with renpy.open_file(filename, encoding=encode, directory='MonoBehaviour') as txt:
            text_json = json.load(txt)
            for row in range(0, len(text_json[rowkey])):
                row = text_json[rowkey][row]

                try: textid = int(row[idkey])
                except: textid = row[idkey]
                textstring = str(row[stringkey])

                textstring = "\n".join(textstring.splitlines())
                    
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

                textstring = "\n".join(textstring.splitlines())

                d[textid] = textstring
        return d


    #LOAD AVG ROLE FILE
    if namefilename.endswith('.json'):
        avgroledict = jsonloader(namefilename, namerowkey, nameidkey, namekey, nameencode)
    elif namefilename.endswith('.csv'):
        avgroledict = csvloader(namefilename, nameidkey, namekey, nameencode)

    #LOAD SCRIPT FILE
    if textfilename.endswith('.json'):
        textdict = jsonloader(textfilename, textrowkey, textidkey, textkey, textencode)
    elif textfilename.endswith('.csv'):
        textdict = csvloader(textfilename, textidkey, textkey, textencode)

    #COMBINE EXTRA STRING DICTIONARY
    for key in list(extextdict.keys()):
        if key not in textdict:
            textdict[key] = extextdict[key]



    #FIX SCRIPT FORMATTING
    
    #change the text color formatting to show up correctly in renpy
    #the original formatting looks like: "[339944]「……………………」[-]"
    #where "339944" is a hex color code
    #known examples: 麻薬密売調査(1) 5/6 (avg10388)

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
     
    #color these dialogue strings green:
    for strid in [1132448, 1132458, 1132463]:
        if strid in textdict:
            textdict[strid] = colortext(textdict[strid], '339944')

    #color these dialogue strings blue:
    for strid in [1132449, 1132459, 1132464]:
        if strid in textdict:
            textdict[strid] = colortext(textdict[strid], '334499')

    #one last color tag that's in the middle of the string...
    if 90224 in textdict:
        text = textdict[90224]
        textdict[90224] = text.replace(r"[FF0000]", r"{color=FF0000}").replace(r"[-]", r"{/color}")

    #FIX TYPO
    #ジオフロントの再調査 is labeled 1/2 when it should be 1/1
    if 17579 in textdict:
        if textdict[17579].endswith('1/2'):
            textdict[17579] = textdict[17579][:-3] + '1/1'
return