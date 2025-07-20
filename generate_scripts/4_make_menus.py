import json
from pathlib import Path

# I don't know if it's ok to be using __file__ here, 
# but I figure it's better than what it was before
direc = Path(__file__).resolve().parent
exdirec = direc / 'extra_json'
outputdirec = direc / "Renpy_scripts"
outputdirec.mkdir(exist_ok=True)

def loadjson(filepath):
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
		combinedscenelist += loadjson(filepath)

#Load quest list
quest_path = exdirec / 'new_quest.json'
if quest_path.exists():
	questlog_list = loadjson(quest_path)
	
	questlog_dict = dict()
	for log in questlog_list:
		key = log['ID']
		questlog_dict[key] = log
else:
	questlog_dict = dict()


#########################################################
#build and number questlogs
for key in list(questlog_dict.keys()):
	log = questlog_dict[key]
	
	new_log = {
		'type': log['type'],
		'title': log['strID'],
		'level': log['level'],
		'client': log['client'],
		'details': log['description'],
		'steps': log['steps']
	}
	#Makes it possible to remove the clear string by setting it to null in the json
	if log['clear']: new_log['steps'].append(log['clear'])
	
	questlog_dict[key] = new_log

########################################################
errorcount = 0
###now make menu from the new dictionaries
episodelist = []
for category in combinedscenelist:
	categorydict = dict()
	
	if 'strID' in category and category['strID'] != None: 
		categoryname = category['strID']
	else: categoryname = category['name']

	categorydict['chaptername'] = categoryname
	categorydict['quests'] = []
	quests = categorydict['quests']
	
	for quest in category['quests']:
		questdict = dict()
		
		add = None
		if 'strID' in quest and quest['strID'] != None:
			if 'add' in quest: add = quest['add']
			questname = quest['strID']
		else: questname = quest['name']
		
		questdict['questname'] = questname
		questdict['add'] = add
		questdict['logs'] = []
		questdict['scenes'] = []
		
		#QUESTLOGS
		if 'questID' in quest and len(quest['questID']) > 0:
			for logid in quest['questID']:
				if logid in questlog_dict:
					questdict['logs'].append(questlog_dict[logid])
					
				else:
					errorcount += 1
					print(f"Could not find questlog id {logid} in new_quest.json, it will not be added to the menu.")

		for scene in quest['scenes']:
			scenedict = dict()
			
			#scene name
			add = None
			if 'strID' in scene and scene['strID'] != None:
				if 'add' in scene: add = scene['add']
				scenename = scene["strID"]	
			else: scenename = scene['name']
		
			#scene info
			if 'infostrID' in scene and scene['infostrID'] != None:
				sceneinfo = scene['infostrID']
			elif 'info' in scene and scene['info'] != None:
				sceneinfo = scene['info']
			else: sceneinfo = ''

			scenedict['scenename'] = scenename
			scenedict['add'] = add
			scenedict['sceneinfo'] = sceneinfo
			
			# This is the Renpy label that the game will try to jump to.
			# Renpy labels cannot start with a number, so some kind of
			# string needs to be prepended to it.
			avgid = scene["avgID"]
			if isinstance(avgid, int) or avgid[0].isdigit():
				avgid = f'avg{avgid}'

			scenedict['avg'] = avgid
			
			questdict['scenes'].append(scenedict)
		categorydict['quests'].append(questdict)
	episodelist.append(categorydict)
with open((outputdirec / 'episodelist.json'), 'w', encoding='utf-8') as f:
	json.dump(episodelist, f, ensure_ascii=False)

if errorcount > 0:
	input('\nFinished - Please check the error messages, then press "Enter" to close.')
