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

def fix_label_name(label):
	if isinstance(label, int) or label[0].isdigit():
		label = f'avg{label}'
	return label

def fix_label_list(label_list):
	for label_dict in label_list:
		label = label_dict['label']
		label_dict['label'] = fix_label_name(label)

def remove_flowchart_notes(data):
	if isinstance(data, dict):
		for key in list(data.keys()):
			if 'note' in key:
				data.pop(key)

			else:
				remove_flowchart_notes(data[key])
			

	elif isinstance(data, list):
		for listitem in data:
			remove_flowchart_notes(listitem)

	
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

flow = loadjson(exdirec / 'flow.json')
remove_flowchart_notes(flow)

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
episodelist = {
	'menudata': [],
	'questlog_data': questlog_dict,
	'scene_map': {},
	'flow': flow,
	'flow_map': {}
}

###make flow map first
flow_map = episodelist['flow_map']
category_index = -1
for category in flow:
	category_index += 1

	chapter_index = -1
	for chapter in category['chapters']:
		chapter_index +=1

		group_index = -1
		for group in chapter['groups']:
			group_index += 1

			quest_index = -1
			for quest in group['quests']:
				quest_index += 1

				step_index = -1
				for step in quest['steps']:
					step_index += 1

					flow_pos = (category_index, chapter_index, group_index, quest_index, step_index)
	
					corrected_avgs = []
					for node in step['nodes']:
						fix_label_list(node['labels'])
						for label_dict in node['labels']:
							label = label_dict['label']
							flow_map[label] = flow_pos

					for key in ['intro', 'ending']:
						if key in step:
							fix_label_list(step[key]['labels'])
							for label_dict in step[key]['labels']:
								label = label_dict['label']
								flow_map[label] = flow_pos
							
				

category_index = -1
for category in combinedscenelist:
	category_index +=1
	categorydict = dict()
	
	if 'strID' in category and category['strID'] != None: 
		categoryname = category['strID']
	else: categoryname = category['name']

	categorydict['chaptername'] = categoryname
	categorydict['quests'] = []
	quests = categorydict['quests']
	
	quest_index = -1
	for quest in category['quests']:
		quest_index += 1
		questdict = dict()
		
		add = None
		if 'strID' in quest and quest['strID'] != None:
			if 'add' in quest: add = quest['add']
			questname = quest['strID']
		else: questname = quest['name']
		
		questdict['questname'] = questname
		questdict['add'] = add
		questdict['logs'] = []

		index = (category_index, quest_index)
		questdict['menu_index'] = index
		questdict['in_flow'] = False
		questdict['scenes'] = []
		
		#QUESTLOGS
		if 'questID' in quest and len(quest['questID']) > 0:
			for logid in quest['questID']:
				if logid in questlog_dict:
					questdict['logs'].append(logid)
					
				else:
					errorcount += 1
					print(f"Could not find questlog id {logid} in new_quest.json, it will not be added to the menu.")

		scene_index = -1
		for scene in quest['scenes']:
			scene_index += 1
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

			avgid = fix_label_name(avgid)

			scenedict['avg'] = avgid

			index = (category_index, quest_index, scene_index)

			episodelist['scene_map'][avgid] = index

			if avgid in flow_map:
				if not questdict.get('in_flow'):
					questdict['in_flow'] = True
					questdict['flow_index'] = flow_map[avgid]

				# Add a link to here from the flowchart's quest entry
				fmap_category_index, fmap_chapter_index, fmap_group_index, fmap_quest_index = flow_map[avgid][:4]
				flow[fmap_category_index]['chapters'][fmap_chapter_index]['groups'][fmap_group_index]['quests'][fmap_quest_index]['menu_index'] = index
				
			questdict['scenes'].append(scenedict)
		categorydict['quests'].append(questdict)
	episodelist['menudata'].append(categorydict)
with open((outputdirec / 'episodelist.json'), 'w', encoding='utf-8') as f:
	json.dump(episodelist, f, ensure_ascii=False)

if errorcount > 0:
	input('\nFinished - Please check the error messages, then press "Enter" to close.')
