label loadinfo:
python early:
    import json
    import csv

    with renpy.open_file('episodelist.json', encoding="utf-8") as txt:
        menudata = json.load(txt)

    def jsonloader(filename, rowkey, idkey, stringkey):
        d = dict()
        with renpy.open_file(filename, encoding="utf-8", directory='MonoBehaviour') as txt:
            text_json = json.load(txt)
            for row in range(0, len(text_json[rowkey])):
                row = text_json[rowkey][row]

                textid = int(row[idkey])
                textstring = row[stringkey]
                    
                d[textid] = textstring
        return d
                    
    def csvloader(filename, idkey, stringkey):
        #try to check for utf-8 sig encoding
        with renpy.open_file(filename, directory='MonoBehaviour') as txt:
            if txt.read(3) == b'\xef\xbb\xbf': encoding = 'utf-8-sig'
            else: encoding = 'utf-8'

        d = dict()
        with renpy.open_file(filename, encoding=encoding, directory='MonoBehaviour') as txt:
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
                textid = int(row[idpos])

                if len(row) > stringpos:
                    textstring = row[stringpos]
                else:
                    textstring = ''

                d[textid] = textstring
        return d


    #LOAD AVG ROLE FILE
    if namefilename.endswith('.json'):
        avgroledict = jsonloader(namefilename, namerowkey, nameidkey, namekey)
    elif namefilename.endswith('.csv'):
        avgroledict = csvloader(namefilename, nameidkey, namekey)

    #LOAD SCRIPT FILE
    if textfilename.endswith('.json'):
        textdict = jsonloader(textfilename, textrowkey, textidkey, textkey)
    elif textfilename.endswith('.csv'):
        textdict = csvloader(textfilename, textidkey, textkey)


    #FIX SCRIPT FORMATTING
    for key in list(textdict.keys()):
        textstring = textdict[key]

        #some strings have different newline characters that create boxes with the font being used
        textstring = "\n".join(textstring.splitlines())

        #remove formatting from some strings to keep it from showing up in the game
        #known examples: avg 10388
        prefixlist = ['[339944]', '[334499]']
        suffixlist = ['[-]']
        for prefix in prefixlist:
            if textstring.startswith(prefix): textstring = textstring[len(prefix):]
        for suffix in suffixlist:
            if textstring.endswith(suffix): textstring = textstring[:-len(suffix)]
        
        textdict[key] = textstring

    #fix typo
    #ジオフロントの再調査 is labeled 1/2 when it should be 1/1
    if textdict[17579].endswith('1/2'):
        textdict[17579] = textdict[17579][:-3] + '1/1'
return