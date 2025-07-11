import json
from pathlib import Path

# I don't know if it's ok to be using __file__ here, 
# but I figure it's better than what it was before
direc = Path(__file__).resolve().parent
scriptdirec = direc / 'MonoBehaviour'
targetdirec = direc / 'Renpy_Scripts' / 'scripts'
if not targetdirec.exists():
	targetdirec.mkdir(parents=True, exist_ok=True)
	

def load_design_json(filepath):
	with open(filepath, 'r', encoding='utf-8') as f:
		j = json.load(f)
		d = dict()
		for index in range(0, len(j['_rows'])):
			row = j['_rows'][index]
			row_id = row['_id']
			d[row_id] = row
		return d
			
#IMPORT AVG ROLE
avg_role_file = (scriptdirec / 'avg_role.json')
avg_role_dict = load_design_json(avg_role_file)

#IMPORT BGM
bgm_file = (scriptdirec / 'bgm.json')
bgm_dict = load_design_json(bgm_file)

#IMPORT SFX
sfx_file = (scriptdirec / 'sfx.json')
sfx_dict = load_design_json(sfx_file)


#IMPORT VOICE
voice_file = (scriptdirec / 'voice.json')
voice_dict = load_design_json(voice_file)

#################################################

class GameState:
	def __init__(self, avgcode):
		self.avgcode = avgcode
		self.lines = []
		self.state = {
			'l': None, #left
			'mid': None, #middle
			'r': None, #right
		}
		self.bgm = 'not set'
		self.first_fade = True
	
	def add_line(self, *lines):
		for line in lines:
			if not line.endswith('\n'):
				line += '\n'
			self.lines.append(line)
			
	def write_file(self, outpath):
		out = Path(outpath) / f'{self.avgcode}.rpy'
		with open(out, 'w', encoding='utf-8') as w:
			w.write(f"label avg{self.avgcode}:\n")
			w.write('\n')
			for line in self.lines:
				w.write(line)
			w.write('return')
	
	def hide_portraits(self, *positions, write=True, clear=True):
		if 'all' in positions:
			positions = ['l', 'mid', 'r']
		for pos in positions:
			if self.state[pos] != None:
				if write:
					alias = self.state[pos]['alias']
					self.add_line(f'hide {alias}')
				if clear:
					self.state[pos] = None
					
	def unpack_portrait_dict(self, pos, color='light'):
		folderName = self.state[pos]['folderName']
		expression = self.state[pos]['expression']
		alias = self.state[pos]['alias']
		offset = self.state[pos]['offset']
		mirror = self.state[pos]['mirror']
		zorder = self.state[pos]['zorder']
		#don't need to worry about tracking transforms so far, but that could change
		
		if mirror == 1: flip = ', flip'
		else: flip = ''
		
		return (
			f"$ update_portrait("
			f"'{folderName} {expression}', "
			f"'{alias}', "
			f"[{pos}({offset}), {color}{flip}], "
			f"{zorder}"
			")"
		)
	
	def darken_portraits(self, lit_pos):
		for key in self.state.keys():
			if key == lit_pos: continue
			
			elif self.state[key]:
				if self.state[lit_pos]:
					lit_alias = self.state[lit_pos]['alias']
				else:
					lit_alias = None

				alias = self.state[key]['alias']
				if alias == lit_alias:
					self.hide_portraits(key, write=False)
				else:
					line = self.unpack_portrait_dict(key, color='dark')
					self.add_line(line)
		
	def update_portrait(self, pos, portrait_dict):
		if portrait_dict == None:
			self.hide_portraits(pos)
		#if the current portrait in the new portrait's position uses a different alias
		#explicitly hide it
		#otherwise it will be handled on the renpy side
		elif self.state[pos] and portrait_dict['alias'] != self.state[pos]['alias']:
			self.hide_portraits(pos)

		self.state[pos] = portrait_dict
		self.darken_portraits(pos)
		
	def update_bgm(self, newbgm):
		if self.bgm != newbgm:
			if newbgm == None:
				self.add_line('stop music\n')
			else:
				self.add_line(f'play music "{newbgm}"\n')
			self.bgm = newbgm
			
	def add_fade(self, portraitpos=None):
		#Adds a placeholder portrait, so it isn't missing during the transition
		#it will use the same alias as the real one, so it shouldn't need to be hidden
		if portraitpos:
			line = self.unpack_portrait_dict(portraitpos, color='light')
			self.add_line(line)

		#The first fade-in from the scene select menu needs to be treated specially
		#just because of how the default renpy fade transition interacts with the say window
		if self.first_fade == True:
			self.add_line(
				'window show\n'
				'with fade_in\n'
				)
			self.first_fade = False
			
		else:
			self.add_line(f"with fade\n")
		

def make_schedule_dict(json, key):
	d = dict()
	schedule = json[key]
	for entry in schedule:
		idnumber = entry['id']
		start = entry['start']
		end = entry['end']
		for frame in range(start, end+1):
			d[frame] = idnumber
	return d

###START
for cutscenepath in list(scriptdirec.glob('*.json')):
	fname = cutscenepath.stem
	#just to weed out the other files that were in the same folder
	if not fname[0].isdigit(): continue

	#IMPORT SCRIPT JSON
	with open(cutscenepath, 'r', encoding="utf-8")as txt:
		script_json = json.load(txt)

###########################################################################
# Make corrections to original files
	#Fix unset charPos
	if fname == '10008':
		script_json['dialogueFrames'][98]['charPos'] = 1
		script_json['dialogueFrames'][98]['character']['mirror'] = 1
	elif fname == '12766':
		script_json['dialogueFrames'][16]['charPos'] = 1

	#Apply corrections found in mobile version files
	elif fname == '10330':
		script_json['dialogueFrames'][85]['strID'] = 1130996
		script_json['dialogueFrames'][115]['strID'] = 1130966
	elif fname == '10331':
		script_json['dialogueFrames'][88]['strID'] = 1130996
		script_json['dialogueFrames'][88]['character']['charID'] = 4
		script_json['dialogueFrames'][88]['character']['speaker'] = 4
		script_json['dialogueFrames'][118]['strID'] = 1130966
	
	#The CharFadeOut was on the wrong line
	elif fname == '1138':
		script_json['dialogueFrames'][108]['CharFadeOut'] = 1
		script_json['dialogueFrames'][109]['CharFadeOut'] = 0
	elif fname == '1209':
		script_json['dialogueFrames'][14]['CharFadeOut'] = 1
		script_json['dialogueFrames'][15]['CharFadeOut'] = 0
		
	#This one was all kinds of messed up.
	#It would also be possible to change it to hide the Nacht portrait on line 94,
	#and interpret all of the dialogue after that as occuring "off-screen".
	#But since they had already set up the animations in the files,
	#I changed it to show the portraits that were "missing" here instead
	elif fname == '1226':
		#missing portrait and expression
		script_json['dialogueFrames'][96]['character']['charID'] = 1
		script_json['dialogueFrames'][96]['expression'] = 14 #expression was unset so this is a guess
		
		#missing portrait and expression, and misplaced CharFadeOut
		script_json['dialogueFrames'][98]['character']['charID'] = 1
		script_json['dialogueFrames'][98]['expression'] = 12 #expression was unset so this is a guess
		script_json['dialogueFrames'][98]['CharFadeOut'] = 1
		script_json['dialogueFrames'][99]['CharFadeOut'] = 0
		
###########################################################################

	#FIGURE OUT BACKGROUND SCHEDULE
	background_schedule = make_schedule_dict(script_json, 'backgrounds')
		
	#FIGURE OUT BGM SCHEDULE
	bgm_schedule = make_schedule_dict(script_json, 'bgm')
			
	#FIGURE OUT MEMORY SCHEDULE
	memory_schedule = make_schedule_dict(script_json, 'memory')

	state = GameState(fname)

	lastplayed = None
	lastbackground = None
	showingimage = None
	memory = False
	
	framecount = 0
	for frame in script_json['dialogueFrames']:
		framecount += 1
		
		fade = False
		
		#Skip duplicate line 
		#(if we skip it any earlier, it's going to screw up bgm and background scheduling)
		if fname == '12038' and framecount == 15: continue

		template = frame['template']
		charID = frame['character']['charID']
		speaker = frame['character']['speaker']
		displayName = frame['character']['displayName']
		mirror = frame['character']['mirror']
		expression = frame['expression']
		charPos = frame['charPos']
		strID = frame['strID']
		contentSize = frame['contentSize']
		isClearModle = frame['isClearModle']
		CharFadeIn = frame['CharFadeIn']
		CharFadeOut = frame['CharFadeOut']
		voiceID = frame['voice']['id']
		voiceFirst = frame['voice']['first']
		sfxID = frame['sfx']['id']
		sfxFirst = frame['sfx']['first']
		effect = frame['effect']
		avgImageID = frame['avgImageID']
		
		#Check bgm schedule, and update if needed
		if len(bgm_schedule) > 0:
			#Stop the music if framecount is not listed in the bgm schedule
			#and filter out the unused bgm id -1
			if framecount not in bgm_schedule or bgm_schedule[framecount] == -1:
				bgmName = None
			#Otherwise figure out the name of the bgm that should be playing
			else:
				bgmName = bgm_dict[bgm_schedule[framecount]]['_bgmName']

			state.update_bgm(bgmName)
			
		#check if there is supposed to be a background
		if len(background_schedule) > 0:
			#this is for if there will be a background later, but not yet
			if framecount not in background_schedule:
				framebackground = 'placeholderbackground'
			else:	
				framebackground = str(background_schedule[framecount])
				while len(framebackground) < 3: framebackground = '0'+framebackground
				framebackground = 'avg_bg_'+framebackground
		#this is for if there isn't supposed to be a background at all
		else: framebackground = 'placeholderbackground'
		
		if lastbackground != framebackground:
			#generate scene line only if it's different from the last frame
			state.add_line(f"scene {framebackground}\n")
			lastbackground = framebackground
			fade = True
			#The "scene" statement will hide all portraits, so the state needs to track that
			state.hide_portraits('all', write=False)
			#The scene statement will also hide the memory overlay, so track that too:
			memory = False
			
		#check for memory overlay
		if len(memory_schedule) > 0:
			if framecount in memory_schedule:
				if not memory:
					state.add_line('show memoryoverlay zorder 2\n')
					memory = True
			else:
				if memory:
					state.add_line('hide memoryoverlay\n')
					memory = False

		#The fade will be written later
		#This is just to merge it with the fade from the background change up above
		if isClearModle == 1:
			fade = True
			
		#Both isClearModle and the green-text speaker 0 hide all portraits
		if isClearModle == 1 or speaker == 0:
			state.hide_portraits('all')
			
		#check for image to display
		if avgImageID == 0:
			if showingimage:
				state.add_line(f'hide {showingimage}\n')
				showingimage = None
		else:
			avgimagename = "Image"+str(avgImageID)
			if showingimage != avgimagename:
				state.add_line(f'show {avgimagename} zorder 4\n')
				showingimage = avgimagename
		
		#figure out if a portrait needs to be displayed 
		if charID == 0:
			folderName = None
		else:
			folderName = avg_role_dict[charID]['_folderName']
		
		#figure out where on the screen character portrait goes
		if charPos == 1: 
			portraitpos = 'l'
			zorder = 6
			darkpos = 'r'
			if folderName:
				state.hide_portraits('mid')
		elif charPos == 3: 
			portraitpos = 'r'
			zorder = 5
			darkpos = 'l'
			if folderName:
				state.hide_portraits('mid')
		elif charPos in [2, 0]: 
			portraitpos = 'mid'
			zorder = 5
			darkpos = None
			if folderName:
				state.hide_portraits('l', 'r',)

		if folderName:
			alias = f'p{speaker}'
			expression = str(expression)
			offset = str(int(avg_role_dict[charID]['_xPostion']))
			
			portrait_dict = {
				'folderName': folderName,
				'alias': alias,
				'expression': expression,
				'offset': offset,
				'mirror': mirror,
				'zorder': zorder
			}

			state.update_portrait(portraitpos, portrait_dict)

			renpytransform = portraitpos
			#check if portrait is entering or exiting:
			if CharFadeIn == 1: renpytransform += '_entrance'
			if CharFadeOut == 1:  renpytransform += '_exit'

			#moved midback up here so it can get the xoffset added to it	
			if effect == 103 or effect == 203: renpytransform += '_midback'

			renpytransform += f'({offset})'

			#then get effects figured out
			if effect == 102: renpytransform += ', r_shake'
			elif effect == 202: renpytransform += ', l_shake'
			
			#manually add flip to portraits on the left side of the screen
			if mirror == 1: flip = ', flip'
			else: flip = ''
			
			#The fade will cover up portrait animations, so get it out of the way first
			if fade:
				if CharFadeIn == 1 or CharFadeOut == 1 or effect in [103, 203, 102, 202]:
				#everything except for CharFadeIn needs a placeholder portrait so it isn't missing during the fade in
					if not CharFadeIn == 1:
						state.add_fade(portraitpos)
					else:
						state.add_fade()
					fade = False
					
			#SHOW PORTRAIT									
			portrait = (
				f"$ update_portrait("
				f"'{folderName} {expression}', "
				f"'{alias}', "
				f"[{renpytransform}, light{flip}], "
				f"{zorder}"
				")"
			)
			state.add_line(f"{portrait}\n")
		
		else: state.update_portrait(portraitpos, None)

		#If fade was not done earlier because of portrait animations, do it here now
		if fade: 
			state.add_fade()
			fade = False
			
	#SOUND/VOICE
		#check for sfx
		if sfxID != 0:
			sfxname = sfx_dict[sfxID]['_sfxName']
			sfxname = sfxname.split('/')[-1]
			#play sfx
			state.add_line(f'play sfx2 "{sfxname}"\n')
			
		#check for voice
		if voiceID != 0:
			voicename = voice_dict[voiceID]['_voiceName']
			voicename = voicename.split('/')[-1]
			#play voice
			state.add_line(f'play sfxvoice "{voicename}"\n')
		
	#START OF SAY STATEMENT
		
		#figure out where namebox goes
		if speaker == 0: nameboxPos = ''
		elif charPos == 1: nameboxPos = 1
		else: nameboxPos = 3
		
		#convert dialogue string to display correctly
		dialogue = f"[textdict[{strID}]]"
		
		#start with the speaker and dialogue
		say = f"c{speaker}{nameboxPos} '{dialogue}'"
		
		#see if dialogue text needs to be resized
		#(20 is already the default)
		if contentSize != 20:
			#don't want to use the text size values for the scenes that are 
			#supposed to be "minimized" in the corner
			noresizelist = ['10134', '20002', '20112', '20113', '29135'] #NOTE - not 100% sure on 10134
			if contentSize <= 16 and template == 1: pass
			#the files in noresizelist don't have template set to 1, but still need to be filtered
			elif fname in noresizelist: pass
			
			#try to turn the "hard-coded" text size into a multiplier to make it work with different base sizes
			else: say+= f' (what_size=(gui.text_size*{contentSize/20}))'

		#then shake can be added if needed
		if effect == 1: say+=' with shake'
		
		state.add_line(f"{say}\n")
		
		#make sure it doesn't try to show the dark portrait after the portrait has left
		if CharFadeOut == 1:
			state.hide_portraits(portraitpos)
		

	#FIGURE OUT IF THERE ARE CHOICES
	if script_json["ending"]["type"] == 1:
		state.add_line('menu:\n')
		#keep dialogue displayed during choice menu:
		state.add_line('    extend ""\n')
		for choice in range(0, len(script_json["ending"]["options"])):
			choicestrID = script_json["ending"]["options"][choice]["strID"]
			choicetext = f"[textdict[{choicestrID}]]"
			choiceavgID = script_json["ending"]["options"][choice]["avgID"]
			state.add_line(f'    "{choicetext}":\n')
			#state.add_line(f'        jump avg{choiceavgID}\n')
			state.add_line(f'        call avg{choiceavgID}\n')

	state.write_file(targetdirec)
