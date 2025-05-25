import json
from pathlib import Path
import re

# I don't know if it's ok to be using __file__ here, 
# but I figure it's better than what it was before
direc = Path(__file__).resolve().parent
exdirec = direc / 'extra_json'
outputdirec = direc / "Renpy_scripts"
outputdirec.mkdir(exist_ok=True)

def loadjson(filename):
	filepath = exdirec / filename
	with open(filepath, 'r', encoding='utf-8') as txt:
		return json.load(txt)
	
#Combine scene lists	
scene_lists_to_combine = [
	'new_story.json',
	'new_training.json',
	'EX12_event.json',
	'EX13_exploration.json',
	'EX14_daily.json',
	'EX15_unused.json'
]
combinedscenelist = list()

for filename in scene_lists_to_combine:
	filepath = exdirec / filename
	if filepath.exists():
		combinedscenelist += loadjson(filename)

#Load quest list
questlog_dict = loadjson('new_quest.json')


#########################################################
#build and number questlogs
questlogdict = dict()
for key in list(questlog_dict.keys()):
	log = questlog_dict[key]
	
	questlog_dict[key] = {
		'type': log['type'],
		'title': log['strID'],
		'level': log['level'],
		'client': log['client'],
		'details': log['description'],
		'steps': (log['steps'] + [log['clear']])
	}

########################################################
###now make menu from the new dictionaries
episodelist = []
for category in combinedscenelist:
	categorydict = dict()
	
	categorynumber = str(combinedscenelist.index(category))
	while len(categorynumber) < 2: categorynumber = '0'+categorynumber
	
	if 'strID' in category and category['strID'] != None: 
		level0 = category['strID']
	else: level0 = category['name']

	categorydict['chaptername'] = level0
	categorydict['quests'] = []
	quests = categorydict['quests']
	
	for quest in category['quests']:
		questdict = dict()

		questnumber = str(category['quests'].index(quest))
		while len(questnumber) < 2: questnumber = '0'+questnumber
		
		scenemenu = "quest"+categorynumber+questnumber
		
		add = None
		if 'strID' in quest and quest['strID'] != None:
			if 'add' in quest: add=fr'{quest["add"]}'
			level1 = quest['strID']
		else: level1 = quest['name']
		
		questdict['questname'] = level1
		questdict['add'] = add
		questdict['logs'] = []
		questdict['scenes'] = []
		
		
		#QUESTLOGS
		if 'questID' in quest and len(quest['questID']) > 0:
			for log in quest['questID']:
				questdict['logs'].append(questlog_dict[str(log)])


		for scene in quest['scenes']:
			scenedict = dict()
			
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
		categorydict['quests'].append(questdict)
	episodelist.append(categorydict)
with open((outputdirec / 'episodelist.json'), 'w', encoding='utf-8') as f:
	json.dump(episodelist, f, ensure_ascii=False)
