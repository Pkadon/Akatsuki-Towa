import json
from pathlib import Path
import os
import re

direc = Path.cwd()
exdirec = direc / 'extra_json'

outputdirec = direc / "Renpy_scripts"
if not os.path.exists(outputdirec):
	os.makedirs(outputdirec)

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
#with open(exdirec / 'combinedstory.json', 'w', encoding='utf-8') as f:
#	json.dump(combinescenedict, f, ensure_ascii=False, indent=4)
	

for f in combinequestlist:
	f = exdirec / f
	if os.path.isfile(f):
		questjsonmerger(f)	
#with open(exdirec / 'combinedquest.json', 'w', encoding='utf-8') as f:
#	json.dump(combinequestdict, f, ensure_ascii=False, indent=4)

#########################################################
#build and number questlogs
questlogdict = dict()
for key in list(combinequestdict.keys()):
	log = combinequestdict[key]
	logname = "log"+str(key)
	
	logdict = dict()
	#build log
	#prefix
	logdict['type'] = log['type']
	#title
	logdict['title'] = log["strID"]
	#level
	logdict['level'] = log["level"]
	#client
	logdict['client'] = log["client"]
	#description
	logdict['details'] = log["description"]
	#steps
	steps = []
	for step in log['steps']:
		steps.append(step)
	#clear
	steps.append(log["clear"])
	
	logdict['steps'] = steps

	questlogdict[logname] = logdict
########################################################
###now make menu from the new dictionaries

episodelist = []
for categorynumber in range(1, (len(combinescenedict)+1)):
	chapterdict = dict()
	category = combinescenedict[str(categorynumber)]
	categorynumber = str(categorynumber)
	while len(categorynumber) < 2: categorynumber = '0'+categorynumber
	
	if 'strID' in category and category['strID'] != None: 
		level0 = int(category['strID'])
	else: level0 = category['name']

	chapterdict['chaptername'] = level0
	chapterdict['quests'] = []
	quests = chapterdict['quests']
	
	for questnumber in range(1, (len(category['level1'])+1)):
		questdict = dict()
		quest = category['level1'][str(questnumber)]
		questnumber = str(questnumber)
		while len(questnumber) < 2: questnumber = '0'+questnumber
		
		scenemenu = "quest"+categorynumber+questnumber
		
		add = None
		if 'strID' in quest and quest['strID'] != None:
			if 'add' in quest: add=fr'{quest["add"]}'
			level1 = int(quest['strID'])
		else: level1 = quest['name']
		
		questdict['questname'] = level1
		questdict['add'] = add
		questdict['logs'] = []
		questdict['scenes'] = []
		
		
		#QUESTLOGS
		if 'questID' in quest and len(quest['questID']) > 0:
			for log in quest['questID']:
				logname = f"log{log}"
				questdict['logs'].append(questlogdict[logname])


		for scenenumber in range(1, (len(quest['level2'])+1)):
			scenedict = dict()
			scene = quest['level2'][str(scenenumber)]
			
			#scene name
			add = None
			if 'strID' in scene and scene['strID'] != None:
				if 'add' in scene: add=fr'{scene["add"]}'
				scenename = scene["strID"]	
			else: scenename = scene['name']
		
			#scene info
			if 'infostrID' in scene and scene['infostrID'] != None:
				sceneinfo = scene['infostrID']
			elif 'info' in scene and scene['info'] != None:
				sceneinfo = scene['info']
			else: sceneinfo = ''
			
			#combine name and info into one line
			level2 = scenename
			
			scenedict['scenename'] = level2
			scenedict['add'] = add
			scenedict['sceneinfo'] = sceneinfo
			scenedict['avg'] = f'avg{scene["avgID"]}'
			
			questdict['scenes'].append(scenedict)
		chapterdict['quests'].append(questdict)
	episodelist.append(chapterdict)
with open((outputdirec / 'episodelist.json'), 'w', encoding='utf-8') as f:
	json.dump(episodelist, f, ensure_ascii=False, indent=4)
