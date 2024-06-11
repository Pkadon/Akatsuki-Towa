import json
from pathlib import Path
import os

direc = Path.cwd()
exdirec = direc / "extra_json"
scriptdirec = direc / 'MonoBehaviour'

#IMPORT TEXT JSON
with open((scriptdirec / 'text.json'), 'r', encoding="utf-8")as txt:
	text_json = json.load(txt)
textdict = dict()
for i in range(0, len(text_json['_rows'])):
	textdict[text_json['_rows'][i]['_id']] = text_json['_rows'][i]['_text']
	
#IMPORT TRAINING
trainingdict = dict()
for train in scriptdirec.glob('training_event*'):
	with open(train, 'r', encoding="utf-8")as txt:
		training_json = json.load(txt)
	for i in range(0, len(training_json['_rows'])):
		i = training_json['_rows'][i]
		trainingid = i['_id']
		trainingbook = i['_book_str']
		trainingchapter = i['_chapter_str']
		trainingquest = i['_quest']
		trainingtrigger = i['_trigger']
		
		trainingdict[trainingid] = {
		'book': trainingbook, 
		'chapter': trainingchapter, 
		'quest': trainingquest, 
		'trigger': trainingtrigger
		}
		
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
		
#IMPORT TRIGGER
with open((scriptdirec / 'trigger.json'), 'r', encoding="utf-8")as txt:
	trigger_json = json.load(txt)
triggerdict = dict()
for i in range(0, len(trigger_json['_rows'])):
	i = trigger_json['_rows'][i]
	triggerdict[str(i['_id'])] = {
	'avgenabled': i['_aAvgEnabled'],
	'avgid': i['_aAvgId'] 
	}

#START
trainingmenu = dict()

lastcat = ''
catcount = 0
lastbut = ''
butcount = 0

lastbut2 = ''
but2count = 0

for trainingid in trainingdict.keys():
	checktrigger = questdict[trainingdict[trainingid]['quest']]['triggeronbrowse']
	checktrigger = str(int(checktrigger)+3)
	if triggerdict[checktrigger]['avgenabled'] == 1:

		
		catstrID = trainingdict[trainingid]['book']
		if catstrID == 19001:
			catorder = 11
			
		## to have it auto sort "event" scenes, remove the "continue", and uncomment the "catorder = 12"
		## it will only be able to sort events that are accessible from any "training_event.json" and "quest.json" files
		## placed in the 'MonoBehaviour' folder
		elif catstrID == 19004:
			#catorder = 12
			continue 
			
		if catorder not in trainingmenu: 
			trainingmenu[catorder] = dict()
			trainingmenu[catorder]['name'] = textdict[catstrID]
			trainingmenu[catorder]['strID'] = catstrID
			trainingmenu[catorder]['level1'] = dict()
			butcount = 0

		but1strID = trainingdict[trainingid]['chapter']
		
		if butcount == 0 or trainingmenu[catorder]['level1'][butcount]['strID'] != but1strID:
			butcount += 1
			trainingmenu[catorder]['level1'][butcount] = dict()
			but1dict = trainingmenu[catorder]['level1'][butcount]
			
			but1dict['name'] = textdict[but1strID]
			but1dict['strID'] = but1strID
			but1dict['level2'] = dict()
			but2count = 0
				
		but2count +=1
		trainingmenu[catorder]['level1'][butcount]['level2'][but2count] = dict()
		but2dict = trainingmenu[catorder]['level1'][butcount]['level2'][but2count]

		but2dict['name'] = textdict[questdict[trainingdict[trainingid]['quest']]['name']]
		but2dict['strID'] = questdict[trainingdict[trainingid]['quest']]['name']
		but2dict['avgID'] = triggerdict[checktrigger]['avgid']

with open(exdirec / 'new_training.json', 'w', encoding='utf-8') as f:
	json.dump(trainingmenu, f, ensure_ascii=False, indent=4)
