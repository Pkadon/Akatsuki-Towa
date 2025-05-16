import json
from pathlib import Path

# I don't know if it's ok to be using __file__ here, 
# but I figure it's better than what it was before
direc = Path(__file__).resolve().parent
exdirec = direc / "extra_json"
scriptdirec = direc / 'MonoBehaviour'

#IMPORT TEXT
with open((scriptdirec / 'text.json'), 'r', encoding="utf-8")as txt:
	text_json = json.load(txt)
textdict = dict()
for i in range(0, len(text_json['_rows'])):
	textdict[text_json['_rows'][i]['_id']] = text_json['_rows'][i]['_text']
	
#IMPORT TRAINING
trainingdict = dict()
for training_event_file in scriptdirec.glob('training_event*'):
	with open(training_event_file, 'r', encoding="utf-8")as txt:
		training_json = json.load(txt)
	for i in range(0, len(training_json['_rows'])):
		i = training_json['_rows'][i]
		trainingid = i['_id']

		trainingdict[trainingid] = i

#IMPORT QUEST
questdict = dict()
for quest_file in scriptdirec.glob('quest*'):
	with open(quest_file, 'r', encoding="utf-8")as txt:
		quest_json = json.load(txt)
	for i in range(0, len(quest_json['_rows'])):
		i = quest_json['_rows'][i]
		questid = i['_id']
		
		questdict[questid] = i

#IMPORT TRIGGER
triggerdict = dict()
with open((scriptdirec / 'trigger.json'), 'r', encoding="utf-8")as txt:
	trigger_json = json.load(txt)
for i in range(0, len(trigger_json['_rows'])):
	i = trigger_json['_rows'][i]
	triggerid = i['_id']
	
	triggerdict[triggerid] = i

#START
newtraininglist = list()

lastquest = None
lastchapter = None

training_started = False
event_started = False

for trainingid in trainingdict.keys():
	stage = trainingdict[trainingid]
	checktrigger = questdict[stage['_quest']]['_triggerOnBrowse']
	checktrigger = checktrigger+3
	if triggerdict[checktrigger]['_aAvgEnabled'] == 1:
		
		book = stage['_book_str'] #catstrID
		
		if book == 19001:
			category = 0
			if not training_started:
				trainingscenes = {
					'name': textdict[19001],
					'strID': 19001,
					'quests': list()
				}
				newtraininglist.append(trainingscenes)
				training_started = True
				questcount = -1
			
		## to have it auto sort "event" scenes, remove the "continue" line,
		## and uncomment the immediate block below,
		## and uncomment the "newtraininglist.append(eventscenes)" line above
		## it will only be able to sort events that are accessible from any "training_event.json" and "quest.json" files
		## placed in the 'MonoBehaviour' folder
		elif book == 19004:
			'''
			category = 1
			if not event_started:
				eventscenes = {
					'name': textdict[19004],
					'strID': 19004,
					'quests': list()
				}
				newtraininglist.append(eventscenes)
				event_started = True
				questcount = -1
			'''
			continue

		chapter = stage['_chapter_str']
		if chapter != lastchapter:
			quest = {
				'name': textdict[chapter],
				'strID': chapter,
				'scenes': list()
			}
			
			lastchapter = chapter
			newtraininglist[category]['quests'].append(quest)
			questcount += 1

		scene = {
			'name': textdict[questdict[stage['_quest']]['_name']],
			'strID': questdict[stage['_quest']]['_name'],
			'avgID': triggerdict[checktrigger]['_aAvgId']
		}
		newtraininglist[category]['quests'][questcount]['scenes'].append(scene)


with open(exdirec / 'new_training.json', 'w', encoding='utf-8') as f:
	json.dump(newtraininglist, f, ensure_ascii=False, indent=4)
