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
	
#IMPORT QUEST
questdict = dict()
for quest in scriptdirec.glob('quest*'):
	with open(quest, 'r', encoding="utf-8")as txt:
		quest_json = json.load(txt)
	for i in range(0, len(quest_json['_rows'])):
		i = quest_json['_rows'][i]
		questid = i['_id']
		questtype = i['_type']
		questname = i['_name']
		questclient = i['_client']
		questreclevel = i['_recommendedLv']
		questpenddesc = i['_descOnPending']
		questcompdesc = i['_descOnComplete']
		questfaildesc = i['_descOnFail']
		triggeronbrowse = i['_triggerOnBrowse']
		
		questprogress_pending = list(i['_stepDescsOnPending'])
		questprogress_complete = list(i['_stepDescsOnComplete'])
		
		questdict[questid] = {
		'questid': questid,
		'type': questtype,
		'name': questname,
		'client': questclient,
		'level': questreclevel,
		'penddesc': questpenddesc,
		'compdesc': questcompdesc,
		'faildesc': questfaildesc,
		'triggeronbrowse': triggeronbrowse,
		
		'progresslist_pending': questprogress_pending,
		'progresslist_complete': questprogress_complete
		}

#IMPORT QUEST BOOK
with open((scriptdirec / 'booktabs.json'), 'r', encoding="utf-8")as txt:
	book_json = json.load(txt)
	
#START
questbook = dict()
chaptercount = 0
for i in range(0, len(book_json['_rows'])):
	i = book_json['_rows'][i]
	bookid = i['_id']
	titlelevel = i['_titlelevel']
	text = i['_text']
	questid = i['_param']

	if titlelevel == 1:
		chaptercount+=1
		#the 14th level 1 title is the start of the bestiary, so don't need to go any higher
		if chaptercount >=14: break
		continue
		
	elif titlelevel == 2:
		#the entries for these quests don't seem to exist and cause problems, so skipping them
		skiplist = [825,826,827,887,987,988,989,990,991,20535,20536,20537,20538,991]
		if questid in skiplist: continue
		
		questbook[questid] = dict()
		quest = questbook[questid]
		
		quest['ID'] = questid
		quest['name'] = textdict[text]
		quest['strID'] = text
		quest['type'] = questdict[questid]['type']
		quest['level'] = questdict[questid]['level']
		quest['client'] = questdict[questid]['client']
		quest['description'] = questdict[questid]['penddesc']
		
		quest['steps'] = []
		
		for step in questdict[questid]['progresslist_pending']:
			#0 is default, 74308 is blank or missing
			skiplist = [0, 74308] 
			if step in skiplist: continue
			else: quest['steps'].append(step)
				
		quest['clear'] = questdict[questid]['compdesc']
		quest['fail'] = questdict[questid]['faildesc']
		
		
with open(exdirec / 'new_quest.json', 'w', encoding='utf-8') as f:
	json.dump(questbook, f, ensure_ascii=False, indent=4)
