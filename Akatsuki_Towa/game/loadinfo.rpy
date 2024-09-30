label loadinfo:
python early:

    import json

    with renpy.open_file('episodelist.json', encoding="utf-8") as txt:
        menudata = json.load(txt)

    #IMPORT TEXT JSON
    with renpy.open_file('text.json', encoding="utf-8", directory='MonoBehaviour') as txt:
        text_json = json.load(txt)
    textdict = dict()
    for i in range(0, len(text_json['_rows'])):

        textid = text_json['_rows'][i]['_id']
        textstring = text_json['_rows'][i]['_text']
        ###a few strings have weird newline characters that create boxes with this font
        textstring = "\n".join(textstring.splitlines())
        
        ###remove formatting from some strings to keep it from showing up in the game
        ###known examples: avg #10388
        prefixlist = ['[339944]', '[334499]']
        suffixlist = ['[-]']
        for prefix in prefixlist:
            if textstring.startswith(prefix): textstring = textstring[len(prefix):]
        for suffix in suffixlist:
            if textstring.endswith(suffix): textstring = textstring[:-len(suffix)]
        
        textdict[textid] = textstring

    #fix typo
    #ジオフロントの再調査 is labeled 1/2 when it should be 1/1
    if textdict[17579].endswith('1/2'):
        textdict[17579] = textdict[17579][:-3] + '1/1'

       

    #IMPORT AVG ROLE
    with renpy.open_file('avg_role.json', encoding="utf-8", directory='MonoBehaviour') as txt:
        avgrole_json = json.load(txt)
    avgroledict = dict()
    for i in range(0, len(avgrole_json['_rows'])):
        i = avgrole_json['_rows'][i]

        avgroleid = i['_id']
        avgrolename = i["_roleName"]

        avgroledict[avgroleid] = avgrolename
return
