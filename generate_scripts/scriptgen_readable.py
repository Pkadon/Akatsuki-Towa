import json
from pathlib import Path
import os

direc = Path.cwd()
scriptdirec = direc / 'MonoBehavior'

targetdirec = direc / 'Readable_Scripts'
if not os.path.exists(targetdirec):
	os.makedirs(targetdirec)

#IMPORT TEXT JSON
with open((scriptdirec / 'text.json'), 'r', encoding="utf-8")as txt:
	text_json = json.load(txt)
textdict = dict()
for i in range(0, len(text_json['_rows'])):
	textid = str(text_json['_rows'][i]['_id'])
	textstring = text_json['_rows'][i]['_text']

	#strip the "[######]" and "[-]" from a few piece of dialogue that use special effects
	filterlist = ['1132448', '1132449', '1132458', '1132459', '1132463', '1132464']
	if textid in filterlist: textstring = textstring[8:-3]

	textdict[textid] = textstring

#IMPORT AVG ROLE
with open((scriptdirec / 'avg_role.json'), 'r', encoding="utf-8")as txt:
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
	
#start on cutscene files
for avg in list(scriptdirec.rglob('**/*.json')):
	avgid = avg.stem
	if not avgid[0].isdigit(): continue
	
	avgdialoguelist = []
	with open(avg, 'r', encoding="utf-8")as txt:
		avg_json = json.load(txt)
		for i in range(0, len(avg_json['dialogueFrames'])):
			i = avg_json['dialogueFrames'][i]
			speakerid = i['character']['speaker']
			if speakerid == 0: speakerstr = ''
			else: speakerstr = avgroledict[speakerid]["roleName"]
			dialoguestrid = i['strID']
			dialoguestr = textdict[str(dialoguestrid)]
			dialoguestr = dialoguestr.replace('\r\n', '\n')
			avgdialoguelist.append((speakerstr, dialoguestr))
	targetfile = targetdirec / (avgid+'.txt')
	with open(targetfile,'w', encoding="utf-8") as f:
		for speaker, dialogue in avgdialoguelist:
			f.write(f"{speaker}:\n{dialogue}\n\n")
