label loadinfo:
python early:

    import json

    #IMPORT TEXT JSON
    with renpy.open_file('text.json', encoding="utf-8", directory='MonoBehaviour') as txt:
        text_json = json.load(txt)
    textdict = dict()
    for i in range(0, len(text_json['_rows'])):

        textid = text_json['_rows'][i]['_id']
        textstring = text_json['_rows'][i]['_text']
        ###a few strings have weird newline characters that create boxes with this font
        textstring = "\n".join(textstring.splitlines())
        
        ###there is ONE cutscene that changes the text color for an NPC's dialogue
        ###the formatting of the strings crashes renpy
        filterlist = ['1132448', '1132449', '1132458', '1132459', '1132463', '1132464']
        if textid in filterlist: textstring = textstring[8:-3]
        
        textdict[textid] = textstring

    #IMPORT AVG ROLE
    with renpy.open_file('avg_role.json', encoding="utf-8", directory='MonoBehaviour') as txt:
        avgrole_json = json.load(txt)
    avgroledict = dict()
    for i in range(0, len(avgrole_json['_rows'])):
        i = avgrole_json['_rows'][i]
        avgroleid = i['_id']
        avgroledict[avgroleid] = {
        'roleName': i["_roleName"],
        'folderName': i["_folderName"],
        'xPosition': i['_xPostion']
        }

return
