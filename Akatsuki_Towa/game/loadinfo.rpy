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

                textstring = "\n".join(textstring.splitlines())
                    
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

                textstring = "\n".join(textstring.splitlines())

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

    #COMBINE EXTRA STRING DICTIONARY
    for key in list(extextdict.keys()):
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


    #FIX TYPO
    #ジオフロントの再調査 is labeled 1/2 when it should be 1/1
    if 17579 in textdict:
        if textdict[17579].endswith('1/2'):
            textdict[17579] = textdict[17579][:-3] + '1/1'
return