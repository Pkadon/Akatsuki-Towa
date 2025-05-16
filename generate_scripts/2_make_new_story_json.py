import json
from pathlib import Path

# I don't know if it's ok to be using __file__ here, 
# but I figure it's better than what it was before
direc = Path(__file__).resolve().parent
exdirec = direc / 'extra_json'
scriptdirec = direc / 'MonoBehaviour'

#IMPORT TEXT JSON
with open((scriptdirec / 'text.json'), 'r', encoding="utf-8")as txt:
	text_json = json.load(txt)
textdict = dict()
for i in range(0, len(text_json['_rows'])):
	textdict[text_json['_rows'][i]['_id']] = text_json['_rows'][i]['_text']

#IMPORT NEWLY MADE QUEST JSON
with open(exdirec / 'new_quest.json', 'r', encoding="utf-8")as txt:
	new_questdict = json.load(txt)
	
#START
newstorylist = [
	{
		'name': textdict[19501],
		'strID': 19501,
		'quests': list()
	},
	{
		'name': textdict[19502],
		'strID': 19502,
		'quests': list()
	},
	{
		'name': textdict[19503],
		'strID': 19503,
		'quests': list()
	},
	{
		'name': textdict[19504],
		'strID': 19504,
		'quests': list()
	},
	{
		'name': textdict[19505],
		'strID': 19505,
		'quests': list()
	},
	{
		'name': textdict[19506],
		'strID': 19506,
		'quests': list()
	},
	{
		'name': textdict[19507],
		'strID': 19507,
		'quests': list()
	},
	{
		'name': textdict[19508],
		'strID': 19508,
		'quests': list()
	},
	{
		'name': textdict[19509],
		'strID': 19509,
		'quests': list()
	},
	{
		'name': textdict[19510],
		'strID': 19510,
		'quests': list()
	}
]

catorder = {
		19501: 0,
		19502: 1,
		19503: 2,
		19504: 3,
		19505: 4,
		19506: 5,
		19507: 6,
		19508: 7,
		19509: 8,
		19510: 9,
#		19512: 13,
#		19513: 14,
#		90000: 12,
	}

lastcat = None
lastquest = None
questcount = None
level1 = None
level2 = None

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
	subgroup = i["_subGroup"]
	for avgid, name, info in zip(avgids, avgnames, avginfos):

		name =  int(name)
		info = int(info)
		avgid =  int(avgid)

		category = catorder[group]

		if category != lastcat:
			lastcat = category
			questcount = -1

		if subgroup != lastquest:
			quest = {
					"name": textdict[subgroup],
					"strID": subgroup,
					'questID': '',
					'scenes': list()
				}
			#look for matching quest
			questidlist = []
			for questid in list(new_questdict.keys()):
				if new_questdict[questid]["strID"] == subgroup: 
					questidlist.append(int(questid))
					quest['questID'] = questidlist
					
					break
			
			newstorylist[category]['quests'].append(quest)
			lastquest = subgroup
			questcount += 1
			
			level1 = newstorylist[category]['quests'][questcount]
					
		scene = {
			'name': textdict[name],
			'strID': name,
			'infostrID': info,
			'avgID': avgid
		}
		
		###try to fix some of the typos in the original text
		#影でうごめく陰謀(1) has two 5/7's
		if avgid == 10437:
			scene['name'] = textdict[17535]
			scene['strID'] = 17535
		#大公の仕立て屋を探せ has two 2/4's
		if avgid == 12621:
			scene['name'] = textdict[17807]
			scene['strID'] = 17807
			
		level1['scenes'].append(scene)

with open(exdirec / 'new_story.json', 'w', encoding='utf-8') as f:
	json.dump(newstorylist, f, ensure_ascii=False, indent=4)
