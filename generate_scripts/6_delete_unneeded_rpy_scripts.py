import json
from pathlib import Path

# I don't know if it's ok to be using __file__ here, 
# but I figure it's better than what it was before
direc = Path(__file__).resolve().parent

choicelist = direc / 'extra_json' / 'choicelist.json'

renpydirec = direc / 'Renpy_scripts'
episodelist = renpydirec / 'episodelist.json'
scriptdirec = renpydirec / 'scripts'

# load episodelist
with open(episodelist, 'r', encoding='utf-8') as txt:
	episodelist = json.load(txt)

# load choicelist	
with open(choicelist, 'r', encoding='utf-8') as txt:
	choicelist = json.load(txt)

keeplist = list()

def keep(avgid):
	if avgid not in keeplist:
		keeplist.append(avgid)
	
	if avgid in choicelist:
		for choice in choicelist[avgid]:
			choice = str(choice)
			if choice not in keeplist:
				keep(choice)


for chapter in episodelist:
	for quest in chapter['quests']:
		for scene in quest['scenes']:
			avg = scene['avg'].lstrip('avg')
			keep(avg)


if scriptdirec.is_dir():
	for cutscenepath in list(scriptdirec.glob('*.rpy')):
		fname = cutscenepath.stem
		#just to weed out the other files that were in the same folder
		if not fname[0].isdigit(): continue

		if fname not in keeplist:
			print(f'Deleting {cutscenepath}')
			cutscenepath.unlink()
	
print(f'Finished! Final script file count should be: {len(keeplist)}')


