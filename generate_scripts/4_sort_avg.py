import json
from pathlib import Path
import os
import re


direc = Path.cwd()
exdirec = direc / 'extra_json'
scriptdirec = Path.cwd() / 'MonoBehaviour'

sortdirec = direc / "sorted"
if not os.path.exists(sortdirec):
	os.makedirs(sortdirec)

combinescenelist = [
	'new_story.json',
	'new_training.json',
	'EX_story_training.json',
	'EX12_event.json',
	'EX13_exploration.json',
	'EX14_daily.json',
	'EX15_unused.json'
]
combinescenedict = dict()

combinequestlist = [
	'new_quest.json',
	'EXQ_unusedquestlog.json'
]
combinequestdict = dict()

def scenejsonmerger(exjson):
	with open(exjson, 'r', encoding="utf-8")as txt:
		ex = json.load(txt)
		
	for category in list(ex.keys()):
		excategory = ex[category]
		if category not in combinescenedict:
			combinescenedict[category] = excategory 
			combinecategory = combinescenedict[category]
			
		else:
			combinecategory = combinescenedict[category]
			
			exlevel1 = excategory['level1']
			combinelevel1 = combinecategory['level1']
			for level1 in list(exlevel1.keys()):
				
				if level1 not in combinelevel1:
					combinelevel1[level1] = exlevel1[level1]
					
				else:
					exlevel2 = exlevel1[level1]['level2']
					combinelevel2 = combinelevel1[level1]['level2']
					for level2 in list(exlevel2.keys()):
						
						if level2 not in combinelevel2:
							combinelevel2[level2] = exlevel2[level2]
					
						else:
							buttonlist = []
							for button in  range(int(level2), len(combinelevel2)+1):
								buttonlist.append(button)
							buttonlist.reverse()
							
							#moving everything over one to make room for the entry being inserted
							for button in buttonlist:
								combinelevel2[str(button+1)] = combinelevel2[str(button)]
							
							combinelevel2[level2] = exlevel2[level2]
							
def questjsonmerger(questjson):
	with open(questjson, 'r', encoding="utf-8")as txt:
		ex = json.load(txt)
	for quest in list(ex.keys()):
		if quest not in combinequestdict:
			combinequestdict[quest] = ex[quest]


for f in combinescenelist:
	f = exdirec / f
	if os.path.isfile(f):
		scenejsonmerger(f)
###UNCOMMENT TO DUMP COMBINED CUTSCENE DICTIONARY AS JSON
#with open(exdirec / 'combinedstory.json', 'w', encoding='utf-8') as f:
#	json.dump(combinescenedict, f, ensure_ascii=False, indent=4)
	

for f in combinequestlist:
	f = exdirec / f
	if os.path.isfile(f):
		questjsonmerger(f)
###UNCOMMENT TO DUMP COMBINES QUEST DICTIONARY AS JSON	
#with open(exdirec / 'combinedquest.json', 'w', encoding='utf-8') as f:
#	json.dump(combinequestdict, f, ensure_ascii=False, indent=4)
					
					
					
########################################################
###Now sort cutscenes using the new dictionaries
########################################################

#IMPORT TEXT JSON
with open((scriptdirec / 'text.json'), 'r', encoding="utf-8")as txt:
	text_json = json.load(txt)
textdict = dict()
for i in range(0, len(text_json['_rows'])):
	textdict[text_json['_rows'][i]['_id']] = text_json['_rows'][i]['_text']
	
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

def pathnamefixer(pathpart):
	src = ('!', '/', '*', '?', ':', '"', '<', '>')
	dst = ('！', '／', '＊', '？', '：', '”', '＜', '＞')
	for o, l in zip(src, dst):
		pathpart = pathpart.replace(o, l)
	return pathpart
	
def avgwriter(avgid, outdirectory):
	avg = scriptdirec / f'{str(avgid)}.json'
	avgdialoguelist = []
	lessoncount = 0
	with open(avg, 'r', encoding="utf-8")as txt:
		avg_json = json.load(txt)					
	for i in range(0, len(avg_json['dialogueFrames'])):
		i = avg_json['dialogueFrames'][i]
		speakerid = i['character']['speaker']
		if speakerid == 0: speakerstr = ''
		else: speakerstr = f'{avgroledict[speakerid]["roleName"]}:\n'
		dialoguestrid = i['strID']
		dialoguestr = textdict[dialoguestrid]
		dialoguestr = dialoguestr.replace('\r\n', '\n')
		avgdialoguelist.append((speakerstr, dialoguestr))
	outfile = outdirectory / f'{avgid}.txt'
	with open(outfile,'w', encoding="utf-8") as w:
		for speaker, dialogue in avgdialoguelist:
			w.write(f"{speaker}{dialogue}\n\n")
			
	#CHECK FOR CHOICES
	if avgid == 19010:
		#19010 gets it stuck in an infinite loop
		#it's an unused alternate version of an already existing cutscene
		#and isn't important enough to figure out right now
		#it will "work" in the renpy version
		#(still infinitely loop, but won't screw up your file system)
		pass		
	else:
		if avg_json["ending"]["type"] == 1:
			for choice in range(0, len(avg_json["ending"]["options"])):
				choicestrID = avg_json["ending"]["options"][choice]["strID"]
				choicetext = textdict[choicestrID]
				choiceavgID = avg_json["ending"]["options"][choice]["avgID"]
				
				choicedirectory = outdirectory / (f'[{str(choice+1)}] {choicetext}')
				if not os.path.exists(choicedirectory):
					os.makedirs(choicedirectory)
				#then check this choice scene to see if there's another choice after
				avgwriter(choiceavgID, choicedirectory)



for categorynumber in range(1, (len(combinescenedict)+1)):
	category = combinescenedict[str(categorynumber)]
	categoryname = pathnamefixer(category['name'])
	categorynumber = str(categorynumber)
	for questnumber in range(1, (len(category['level1'])+1)):
		quest = category['level1'][str(questnumber)]
		questnumber = str(questnumber)
		questname = pathnamefixer(quest['name'])

		outputdirec = sortdirec / f'{str(categorynumber)} {categoryname}' / f'{str(questnumber)} {questname}'
		if not os.path.exists(outputdirec):
			os.makedirs(outputdirec)
		#QUESTLOG
		if 'questID' in quest and len(quest['questID']) > 0:
			logcount = 0
			for log in quest['questID']:
				log = combinequestdict[str(log)]
				logcount+=1
				
				#prefix
				if log['type'] == 1: titleprefix = '[MAIN]'
				elif log['type'] == 2: titleprefix = '[SUB]'
				elif log['type'] == 0: titleprefix = '[UNUSED]'
				#title
				title = textdict[log["strID"]]
				fulltitle = f'{titleprefix} {title}'
				
				outputfile = outputdirec / pathnamefixer(f'{str(logcount)} {fulltitle}.txt')
				with open(outputfile, 'w', encoding="utf-8") as ql:
					ql.write(f'{fulltitle}\n')
					ql.write(f'【推奨レベル】 {str(log["level"])}\n')
					ql.write(f'【依頼人】 {textdict[log["client"]]}\n')
					ql.write(f'【内容】 {textdict[log["description"]]}\n')
					for step in log['steps']:
						ql.write(f' ● {textdict[step]}\n')

		for scenenumber in range(1, (len(quest['level2'])+1)):
			scene = quest['level2'][str(scenenumber)]

			#scene name
			scenename = scene['name']
		
			#scene info
			if 'infostrID' in scene and scene['infostrID'] != None:
				sceneinfo = f' - {textdict[scene["infostrID"]]}'
			elif 'info' in scene and scene['info'] != None:
				sceneinfo = f' - {scene["info"]}'
			else: sceneinfo = ''
			
			#combine name and info into one line
			level2 = pathnamefixer(f"{str(scenenumber)} {scenename}{sceneinfo}")
			
			#avgfile
			avgnumber = scene['avgID']
			avg = scriptdirec / f'{str(avgnumber)}.json'
			
			outputdirec2 = outputdirec / level2
			if not os.path.exists(outputdirec2):
				os.makedirs(outputdirec2)
				
			outputfile2 = outputdirec2 / f'{avgnumber}.txt'
			print(f'Creating File: {outputfile2}')
						
			avgwriter(avgnumber, outputdirec2)	
