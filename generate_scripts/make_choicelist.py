import json
from pathlib import Path

# I don't know if it's ok to be using __file__ here, 
# but I figure it's better than what it was before
direc = Path(__file__).resolve().parent
exdirec = direc / 'extra_json'
scriptdirec = direc / 'MonoBehaviour'

choicelist = dict()
###START
for cutscenepath in list(scriptdirec.glob('*.json')):
	fname = cutscenepath.stem
	#just to weed out the other files that were in the same folder
	if not fname[0].isdigit(): continue

	#IMPORT SCRIPT JSON
	with open(cutscenepath, 'r', encoding="utf-8")as txt:
		script_json = json.load(txt)

		#FIGURE OUT IF THERE ARE CHOICES
		if script_json["ending"]["type"] == 1:

			for choice in range(0, len(script_json["ending"]["options"])):
				choiceavgID = script_json["ending"]["options"][choice]["avgID"]

				if fname not in choicelist:
					choicelist[fname] = list()

				choicelist[fname].append(choiceavgID)

with open((exdirec / 'choicelist.json'), 'w', encoding='utf-8') as d:
	json.dump(choicelist, d, indent=4)


