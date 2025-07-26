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
		self.background = None
		self.memory = False
		self.avgimage = None
		
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
		if self.state[lit_pos]:
			lit_alias = self.state[lit_pos]['alias']
		else:
			lit_alias = None

		for key in self.state.keys():
			if key == lit_pos: continue
			
			elif self.state[key]:
				alias = self.state[key]['alias']
				if alias == lit_alias:
					#this would mean that the current lit portrait has changed sides from last frame
					#renpy will handle the actual hiding, just keeping track here
					self.hide_portraits(key, write=False)
				else:
					#then darken the existing portrait only if it isn't already dark
					#again, renpy is able to handle the hiding and updating for the moment
					if not self.state[key].get('dark'):
						line = self.unpack_portrait_dict(key, color='dark')
						self.add_line(line)
						self.state[key]['dark'] = True
		
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
			
	def update_background(self, newbackground):
		if self.background != newbackground:
			#generate scene line only if it's different from the last frame
			self.add_line(f"scene {newbackground}\n")
			self.background = newbackground
			
			#The "scene" statement will hide all portraits, so the state needs to track that
			self.hide_portraits('all', write=False)
			#The scene statement will also hide the memory overlay, so track that too:
			self.memory = False
			
			#then return True so the outside loop knows to add a fade effect later
			return True
		else: 
			return False
			
	def update_memory(self, is_memory):
		if is_memory == True and self.memory == False:
			state.add_line('show memoryoverlay zorder 2\n')
			self.memory = True
		elif is_memory == False and self.memory == True:
			state.add_line('hide memoryoverlay\n')
			self.memory = False
			
	def update_avgimage(self, newimage):
		if self.avgimage != newimage:
			if newimage == None:
				state.add_line(f'hide {self.avgimage}\n')
				self.avgimage = None
				
			else:
				if self.avgimage != None:
					state.add_line(f'hide {self.avgimage}\n')
				state.add_line(f'show {newimage} zorder 4\n')
				self.avgimage = newimage
			
	def add_fade(self, next_speaker, portraitpos=None):
		#Update the narrator to use the next speaker's character
		#so that the namebox can be present on fade-in
		self.add_line(f"$ update_narrator('{next_speaker}')\n")
		
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

def delete_frame(json, frame_index):
	#Delete the frame itself
	del json['dialogueFrames'][frame_index]
	
	#Then adjust all of the schedules to account for the missing frame
	frame_id = (frame_index + 1) #the schedules count starting from 1 instead of 0
	for key in ['backgrounds', 'bgm', 'memory']:
		if key in json:
			schedule = json[key]
			for copy in schedule[:]:
				entry_index = schedule.index(copy)
				entry = schedule[entry_index]
			#delete the entire entry if the deleted frame was the only frame in the schedule
				if frame_id == entry['start'] == entry['end']:
					schedule.remove(entry)
			#if the deleted frame was >= the start number, the start shouldn't move
			#just decrease the end frame by 1
				elif frame_id >= entry['start']:
					if frame_id <= entry['end']:
						entry['end'] -= 1
			#decrease both start and end of any schedules starting after the deleted frame
				elif frame_id < entry['start']: 
					entry['start'] -= 1
					entry['end'] -= 1	

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
	
#Changing backgrounds around for some of the scenes that were originally minimized
#or that originally used a transparent background
	#This scene has a footstep sound to indicate that they have moved location
	#So I added an indoor background/bgm to the first half to match the first scene of the quest
	elif fname == '12159':
		script_json['backgrounds'].insert(0, {'id': 38, 'start': 1, 'end': 3})
		script_json['backgrounds'][1]['start'] = 4
		script_json['bgm'].insert(0, {'id': 132, 'start': 1, 'end': 3})
		script_json['bgm'][1]['start'] = 4
	#This scene takes place at the harbor, so I changed the background to the harbor.
	elif fname == '20050':
		script_json['backgrounds'][0]['id'] = 28
		
	#This is adding a background to a transparent background scene so that it matches
	#the other scenes around it.  I may decide to change this again later.
	elif fname == '20052':
		script_json['backgrounds'].insert(0, {'id': 27, 'start': 1, 'end': 32}) 
		
	#Remove an extra redundant line - both lines are spoken by the same person, and say the same thing.
	#It is not a mis-set speaker name, because there is a third line that says the same thing spoken by the other person.
	#This could also be changed to remove line 15 instead, if preferred.
	elif fname == '12038':
		delete_frame(script_json, 14)
		
###########################################################################

	#FIGURE OUT BACKGROUND SCHEDULE
	background_schedule = make_schedule_dict(script_json, 'backgrounds')
		
	#FIGURE OUT BGM SCHEDULE
	bgm_schedule = make_schedule_dict(script_json, 'bgm')
			
	#FIGURE OUT MEMORY SCHEDULE
	memory_schedule = make_schedule_dict(script_json, 'memory')

	state = GameState(fname)
	
	framecount = 0
	for frame in script_json['dialogueFrames']:
		framecount += 1
		
		fade = False

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
		if len(bgm_schedule) > 0 and framecount in bgm_schedule:
			#filter out the unused bgm id -1
			if bgm_schedule[framecount] == -1:
				bgmName = None
			#Otherwise figure out the name of the bgm that should be playing
			else:
				bgmName = bgm_dict[bgm_schedule[framecount]]['_bgmName']
		#Stop the music if framecount is not listed in the bgm schedule
		else: bgmName = None
		
		#update the bgm
		state.update_bgm(bgmName)
			
	#Check background schedule, and update if needed
		if len(background_schedule) > 0 and framecount in background_schedule:
				backgroundid = str(background_schedule[framecount]).zfill(3)
				framebackground = 'avg_bg_'+backgroundid
		#Some scenes/frames would have just had a transparent background
		#So there is a predefined placeholder background for those
		else: framebackground = 'placeholderbackground'
		
		#Update the background.
		#If the background was changed, then a "with fade" statement will need to be added later
		if state.update_background(framebackground):
			fade = True

	#Check memory schedule, and update if needed
		if len(memory_schedule) > 0 and framecount in memory_schedule:
			is_memory = True
		else:
			is_memory = False
		state.update_memory(is_memory)
			
	#Misc
		#The fade will be written later
		#This is just to merge it with the fade from the background change up above
		if isClearModle == 1:
			fade = True
			
		#Both isClearModle and the green-text speaker 0 hide all portraits
		if isClearModle == 1 or speaker == 0:
			state.hide_portraits('all')

	#Check for avgimage to display
		if avgImageID == 0:
			avgimagename = None
		else:
			avgimagename = "Image"+str(avgImageID)
		state.update_avgimage(avgimagename)
		
	#Speaker name
		#Figure out where the namebox goes
		if speaker == 0: nameboxPos = ''
		elif charPos == 1: nameboxPos = 1
		else: nameboxPos = 3
		
		#Then figure out what renpy speaker to use.
		#This is also used in fade transitions, so it needs to be figured out up here.
		renpyspeaker = f'c{speaker}{nameboxPos}'
		
	#Portrait
		#figure out if a portrait needs to be displayed 
		if charID == 0:
			folderName = None
		else:
			folderName = avg_role_dict[charID]['_folderName']
		
		#figure out where on the screen character portrait goes
		if charPos == 1: 
			portraitpos = 'l'
			zorder = 6
			if folderName:
				state.hide_portraits('mid')
		elif charPos == 3: 
			portraitpos = 'r'
			zorder = 5
			if folderName:
				state.hide_portraits('mid')
		elif charPos in [2, 0]: 
			portraitpos = 'mid'
			zorder = 5
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

			#check if portrait does the forward lunge animation	
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
						state.add_fade(renpyspeaker, portraitpos)
					else:
						state.add_fade(renpyspeaker)
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
			state.add_fade(renpyspeaker)
			fade = False
			
	#Sound/Voice
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

		#renpyspeaker name needed to be moved higher up to account for fade
		
		#convert dialogue string to display correctly
		dialogue = f"[textdict[{strID}]]"
		
		#start with the speaker and dialogue
		say = f"{renpyspeaker} '{dialogue}'"
		
		#see if dialogue text needs to be resized
		#(20 is already the default)
		if contentSize != 20:
			#don't want to use the text size values for the scenes that are 
			#supposed to be "minimized" in the corner (template = 1)
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
			state.add_line(f'        call avg{choiceavgID}\n')

	state.write_file(targetdirec)
