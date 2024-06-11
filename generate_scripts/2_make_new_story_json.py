import json
from pathlib import Path
import os

direc = Path.cwd()
exdirec = direc / 'extra_json'
scriptdirec = direc / 'MonoBehaviour'

#IMPORT TEXT JSON
with open((scriptdirec / 'text.json'), 'r', encoding="utf-8")as txt:
	text_json = json.load(txt)
textdict = dict()
for i in range(0, len(text_json['_rows'])):
	textdict[text_json['_rows'][i]['_id']] = text_json['_rows'][i]['_text']
	
#IMPORT STORY SCENE LIST
with open((scriptdirec / 'avg_replay.json'), 'r', encoding="utf-8") as story:
	story_json = json.load(story)
storydict = dict()
for i in range(0, len(story_json['_rows'])):
	i = story_json['_rows'][i]
	avgids = list(i["_avgId"].split(','))
	avgnames = list(i["_avgName"].split(','))
	avginfos = list(i["_avgInfo"].split(','))
	group = i["_group"]
	chlist = {
		19501: 1,
		19502: 2,
		19503: 3,
		19504: 4,
		19505: 5,
		19506: 6,
		19507: 7,
		19508: 8,
		19509: 9,
		19510: 10,
	}
	subgroup = i["_subGroup"]
	order = i['_order']
	for avgid, name, info in zip(avgids, avgnames, avginfos):
		storydict[avgid] = {
		'name': int(name), 
		'info': int(info),
		'avgid': int(avgid),
		'group': group,
		'subgroup': subgroup,
		'order': order
		}

#IMPORT NEWLY MADE QUEST JSON
with open(exdirec / 'new_quest.json', 'r', encoding="utf-8")as txt:
	new_questdict = json.load(txt)
	
#START
newstorydict = {
	1: {
		'name': textdict[19501],
		'strID': 19501,
		'level1': dict()
	},
	2: {
		'name': textdict[19502],
		'strID': 19502,
		'level1': dict()
	},
	3: {
		'name': textdict[19503],
		'strID': 19503,
		'level1': dict()
	},
	4: {
		'name': textdict[19504],
		'strID': 19504,
		'level1': dict()
	},
	5: {
		'name': textdict[19505],
		'strID': 19505,
		'level1': dict()
	},
	6: {
		'name': textdict[19506],
		'strID': 19506,
		'level1': dict()
	},
	7: {
		'name': textdict[19507],
		'strID': 19507,
		'level1': dict()
	},
	8: {
		'name': textdict[19508],
		'strID': 19508,
		'level1': dict()
	},
	9: {
		'name': textdict[19509],
		'strID': 19509,
		'level1': dict()
	},
	10: {
		'name': textdict[19510],
		'strID': 19510,
		'level1': dict()
	}
}

catorder = {
		19501: 1,
		19502: 2,
		19503: 3,
		19504: 4,
		19505: 5,
		19506: 6,
		19507: 7,
		19508: 8,
		19509: 9,
		19510: 10,
		19512: 13,
		19513: 14,
		90000: 12,
	}
catcount = 0
lastcat = ''
subcount = 0
lastsub = ''

for scene in storydict.keys():
	
	scenedict = storydict[scene]
	category = catorder[scenedict['group']]
	
	name = scenedict['name']
	info = scenedict['info']
	group = scenedict['group']
	subgroup = scenedict['subgroup']
	order = scenedict['order']
	avgid = scenedict['avgid']
	
	if category != lastcat:
		catcount +=1
		lastcat = category
		subcount = 0
	
	if scenedict['subgroup'] != lastsub:
		subcount +=1
		lastsub = scenedict['subgroup']
		sub2count = 0
	
	if subcount not in newstorydict[category]['level1']:
		newstorydict[category]['level1'][subcount] = {
			"name": textdict[scenedict['subgroup']],
			"strID": scenedict['subgroup'],
			'questID': '',
			'level2': dict()
		}
		#look for matching quest
		questidlist = []
		for k in list(new_questdict.keys()):
			if new_questdict[k]["strID"] == scenedict['subgroup']: 
				questidlist.append(int(k))
				newstorydict[category]['level1'][subcount]['questID'] = questidlist
				
	sub2count +=1
	newstorydict[category]['level1'][subcount]['level2'][sub2count] = {
		'name': textdict[scenedict['name']],
		'strID': scenedict['name'],
		'infostrID': scenedict['info'],
		'avgID': avgid
	}
	
	level2 = newstorydict[category]['level1'][subcount]['level2'][sub2count]
	
	###try to fix some of the typos in the original text
	#影でうごめく陰謀(1) has two 5／7's
	if avgid == 10437:
		level2['name'] = level2['name'][:-3]+'6/7'
		level2['sub'] = 3
		level2['add'] = '6/7'
	#ジオフロントの再調査 is labeled 1/2, but there is only one cutscene in the viewer
	if avgid == 12438:
		level2['name'] = level2['name'][:-3]+'1/1'
		level2['sub'] = 3
		level2['add'] = '1/1'
	#大公の仕立て屋を探せ has two 2/4's
	if avgid == 12621:
		level2['name'] = level2['name'][:-3]+'1/4'
		level2['sub'] = 3
		level2['add'] = '1/4'

with open(exdirec / 'new_story.json', 'w', encoding='utf-8') as f:
	json.dump(newstorydict, f, ensure_ascii=False, indent=4)
