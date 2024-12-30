import json
import csv
from pathlib import Path


direc = Path.cwd()
scriptdirec = direc / 'MonoBehaviour'
outdirec = Path.cwd() / 'Renpy_scripts'
episodelist = outdirec / 'episodelist.json'

#EX TEXT DICT
ex_textdict = {"ex_1": "Optional Dialogue","ex_2": "Extra Dialogue","ex_3": "Extra/Unused","ex_4": "exact timing unknown","ex_5": "Unused Tio Version","ex_6": "Unused Tita Version","ex_7": "Unused Alt Version","ex_8": "Unused Ending","ex_9": "(2 questions correct)","ex_10": "(1 or no questions correct)","ex_11": "Conditional Dialogue","ex_12": "Quest Complete","ex_13": "Quest Complete (Unused)","ex_14": "Unused","ex_15": "Conditional Dialogue (Unused)","ex_16": "Unused Scenes","ex_17": "Fishing","ex_18": "Fishing Unlock Scene","ex_19": "(Prologue)","ex_20": "Fisherman's Guild","ex_21": "(Grancel, Chapter 1)","ex_100": "受付嬢トリア","ex_101": "スラッシュ","ex_102": "キャンベル議員","ex_103": "フェルナンド","ex_104": "スラッシュ/ヒューイ","ex_105": "リン/エオリア","ex_106": "ティータ","ex_107": "カルノー/プロメテ","ex_108": "マードック工房長","ex_109": "ウォン/グンドルフ","ex_110": "ジリアン/ロナード","ex_200": "中央工房の盗難事件(2) 3/7","ex_201": "準遊撃士・ナハトの奮闘記","ex_202": "Vol.1-エオリア編","ex_203": "Vol.1-ヴェンツェル編","ex_204": "Vol.1-スコット編","ex_205": "Vol.1-リン編","ex_206": "Vol.2 アネラス編","ex_207": "Vol.3 ノエル編","ex_208": "Vol.4 ティータ編","ex_209": "Vol.5 ミレイユ編","ex_210": "Vol.6 ヨシュア編","ex_211": "Vol.7 エリィ編","ex_212": "Vol.8 エステル編","ex_213": "Vol.9 ティオ編","ex_214": "Vol.10 ランディ編","ex_215": "Vol.11 ロイド編","ex_216": "Vol.12 レン編","ex_217": "Vol.13 カシウス編","ex_218": "Vol.14 ユリア編","ex_219": "Vol.15 アガット編","ex_220": "Vol.16 グラッツ編","ex_221": "Vol.17 シェラザード編","ex_222": "Vol.18 クローゼ編","ex_223": "Vol.19 ギルバート編","ex_224": "Vol.20 クルツ編","ex_225": "Vol.21 カルナ編","ex_226": "Vol.22 ダドリー編","ex_227": "Vol.23 アリオス編","ex_228": "Vol.24 リシャール編","ex_229": "Vol.25 キール編","ex_230": "Vol.26 ジョゼット編","ex_231": "Vol.27 ドルン編","ex_232": "Vol.28 ミシェル編","ex_233": "EX.1　リース編","ex_234": "EX.2 ケビン編","ex_235": "ミシェル先生の特別レッスン","ex_236": "歩んでいく道の途中で","ex_237": "試験班の夏休み","ex_238": "第１回《ハロウィンフェス》","ex_240": "作者：藤７８\n(2017.12 グランプリ受賞作品)","ex_241": "作者：トム6W\n(2017.12 準グランプリ受賞作品)","ex_242": "作者：月紅\n(2017.12 ブレイサー賞受賞作品)","ex_243": "新米遊撃士のクリスマス","ex_244": "Heroes War！","ex_300": "毎日討伐","ex_301": "ダルモア商会の依頼","ex_302": "ラッセル博士の依頼","ex_303": "リラの依頼","ex_304": "マオ婆さんの依頼","ex_305": "メイベルの依頼","ex_306": "ホテル《ローエンバウム》の依頼","ex_307": "クロスベル警察学校の依頼","ex_308": "イメルダ夫人の依頼","ex_309": "ウルスラ病院の依頼","ex_310": "《リジョンフード》の依頼","ex_311": "アルモリカ村の依頼","ex_312": "《ホテル・ミレニアム》の依頼","ex_313": "マイヤの依頼","ex_314": "マルクの依頼","ex_315": "ドナートの依頼","ex_116": "カヌートの依頼","ex_117": "セナの依頼","ex_118": "クリントの依頼","ex_119": "ルーシーの依頼","ex_120": "モーリスの依頼"}

tldict = {
	"_rows": []
	}
rows = tldict["_rows"]

donelist = []
donescenelist = []

#IMPORT TEXT JSON
with open((scriptdirec / 'text.json'), 'r', encoding="utf-8")as txt:
	text_json = json.load(txt)
textdict = dict()
for i in range(0, len(text_json['_rows'])):
	textdict[text_json['_rows'][i]['_id']] = text_json['_rows'][i]['_text']

#IMPORT AVG ROLE
with open((scriptdirec / 'avg_role.json'), 'r', encoding="utf-8")as txt:
	role_json = json.load(txt)
avgroledict = dict()
for i in range(0, len(role_json['_rows'])):
	avgroledict[role_json['_rows'][i]['_id']] = role_json['_rows'][i]['_roleName']	

	
def makerow(dic):
	key = dic['strid']

	rowdict = dict()
	rowdict['note'] = dic['note']
	
	if dic['dupe']:
		rowdict['_id'] = 'dupe'
	else:
		rowdict['_id'] = key
		 
	if 'speaker' in dic:
		if dic['speaker'] != 0:
			rowdict['speaker'] = avgroledict[dic['speaker']]
	
	if isinstance(key, int):
		rowdict['jptext'] = textdict[key]
		if dic['dupe']:
			rowdict['_text'] = f"(SKIP) Duplicate usage of string id {key}"
		else:
			rowdict['_text'] = ""
	elif key in ex_textdict:
		rowdict['jptext'] = ex_textdict[key]
		rowdict['_text'] = f"(SKIP) Extra string. Please edit '{key}' inside 'CONFIG.rpy'"
		
	if dic['add']:
		rowdict['note'] += ' (numbering will be appended to the end automatically)'
	
	return rowdict


def addrow(note, strid, add=None, speaker=None):
	dic = dict()
	dic['note'] = note
	dic['strid'] = strid
	dic['add'] = add
	if speaker: dic['speaker'] = speaker
	
	if strid in donelist or isinstance(strid, str):
		dic['dupe'] = True
	else:
		dic['dupe'] = False
		
	row = makerow(dic)
	
	rows.append(row)
	donelist.append(strid)
	
def processavg(avg):
	choicescenelist = []
	if avg not in donescenelist:
		avgfile = f'{avg}.json'
		with open(scriptdirec / avgfile, 'r', encoding='utf-8') as f:
			f = json.load(f)
		
		#Apply corrections found in mobile version files
		if str(avg) == '10330':
			f['dialogueFrames'][85]['strID'] = 1130996
			f['dialogueFrames'][115]['strID'] = 1130966

		if str(avg) == '10331':
			f['dialogueFrames'][88]['strID'] = 1130996
			f['dialogueFrames'][88]['character']['charID'] = 4
			f['dialogueFrames'][88]['character']['speaker'] = 4
			f['dialogueFrames'][118]['strID'] = 1130966
		
		rowcount = 0
		for frame in f['dialogueFrames']:
			rowcount += 1
			note = f"AVG {avg}, Line {rowcount}"
			strid = frame['strID']
			speaker = frame['character']['speaker']
			
			addrow(note, strid, speaker=speaker)
			
		#to stop recursively processing a looping choice
		donescenelist.append(avg)
		
		#FIGURE OUT IF THERE ARE CHOICES
		if f["ending"]["type"] == 1:
			choicecount = 0

			for choice in range(0, len(f["ending"]["options"])):
				choicecount += 1
				choice = f["ending"]["options"][choice]
				#the text displayed on the choice button
				strid = choice["strID"]
				#the scene that the choice button leads to
				gotoavg = choice["avgID"]
				
				note = f"AVG {avg} Choice {choicecount} (leads to AVG {gotoavg})"
				
				addrow(note, strid)
				choicescenelist.append(gotoavg)
			
			for choicescene in choicescenelist:
				if choicescene not in donescenelist:
					processavg(choicescene)
				
		
		

with open(episodelist, 'r', encoding='utf-8') as txt:
	episodelist = json.load(txt)

catcount = 0
questcount = 0
for chapter in episodelist:
	catcount += 1
	#category title
	note = f"Category {catcount}/Chapter Title"
	strid = chapter['chaptername']
	
	addrow(note, strid)
	
	for quest in chapter['quests']:
		questcount += 1
		#quest title
		note = f"Quest {questcount} Title (Category {catcount})"
		strid = quest['questname']
		add = quest['add']
		
		addrow(note, strid, add=add)
		
		scenecount = 0
		for scene in quest['scenes']:
			scenecount += 1
			
			avg = scene['avg'].lstrip('avg')
			#title
			note = f"AVG {avg} Title (Quest {questcount}, Scene {scenecount})"
			strid = scene['scenename']
			add = scene['add']
			
			addrow(note, strid, add=add)
			
			#info
			note = f"AVG {avg} Info"
			strid = scene['sceneinfo']
			
			if strid in textdict or strid in ex_textdict:
				addrow(note, strid)
			
			processavg(avg)
					
				
		logcount = 0
		for log in quest['logs']:
			logcount += 1
			questtype = log['type']
			
			#questlog title
			strid = log['title']
			note = f"Quest {questcount} Log {logcount} Title"
			
			addrow(note, strid)
			
			#questlog client
			strid = log['client']
			note = f"Quest {questcount} Log {logcount} Client"
			
			addrow(note, strid)
			
			#questlog details
			strid = log['details']
			note = f"Quest {questcount} Log {logcount} Details"
			
			addrow(note, strid)
			
			#questlog steps
			stepcount = 0
			for step in log['steps']:
				stepcount += 1
				strid = step 
				
				if step == log['steps'][-1]:
					note = f"Quest {questcount} Log {logcount} Completion"
				else:
					note = note = f"Quest {questcount} Log {logcount} Step {stepcount}"
				
				addrow(note, strid)
			
#output json file
makejson = True
if makejson:
	with open((outdirec / 'text.json'), 'w', encoding='utf-8') as f:
		json.dump(tldict, f, ensure_ascii=False, indent=4)

#output csv file
makecsv = True
if makecsv:
	for row in rows:
		if 'speaker' not in row:
			row['speaker'] = ''

	fields = list(rows[0].keys())
	with open((outdirec / 'text.csv'), 'w', encoding='utf-8', newline='') as f:
		writer = csv.DictWriter(f, fieldnames=fields, dialect='excel', quoting=csv.QUOTE_ALL)
		
		writer.writeheader()
		
		for row in rows:
			writer.writerow(row)
		
		
		
