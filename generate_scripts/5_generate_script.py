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
def make_schedule_dict(json, key):
	d = dict()
	for index in range(0, len(json[key])):
		entry = script_json[key][index]
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
		
	#Apply corrections found in mobile version files
	if fname == '10330':
		script_json['dialogueFrames'][85]['strID'] = 1130996
		script_json['dialogueFrames'][115]['strID'] = 1130966

	if fname == '10331':
		script_json['dialogueFrames'][88]['strID'] = 1130996
		script_json['dialogueFrames'][88]['character']['charID'] = 4
		script_json['dialogueFrames'][88]['character']['speaker'] = 4
		script_json['dialogueFrames'][118]['strID'] = 1130966

	#FIGURE OUT BACKGROUND SCHEDULE
	background_schedule = make_schedule_dict(script_json, 'backgrounds')
			
	#FIGURE OUT BGM SCHEDULE
	bgm_schedule = make_schedule_dict(script_json, 'bgm')
			
	#FIGURE OUT MEMORY SCHEDULE
	memory_schedule = make_schedule_dict(script_json, 'memory')
		

	with open((targetdirec / f"{fname}.rpy"), 'w', encoding="utf-8")as f:
		#PRINT START LABEL 
		f.write(f"label avg{fname}:\n")
		f.write('stop music\n')
		f.write('\n')

		lastplayed = ''
		lastbackground = ''
		leftportrait = None
		leftalias = None
		rightportrait = None
		rightalias = None
		centerportrait = None
		centeralias = None
		showingimage = None
		memory = False
		for i in range(0, len(script_json['dialogueFrames'])):
			framecount = i+1
			newscene = False
			
			#Skip duplicate line 
			#(if we skip it any earlier, it's going to screw up bgm and background scheduling)
			if fname == '12038' and framecount == 15: continue

			i = script_json['dialogueFrames'][i]
			template = i['template']
			charID = i['character']['charID']
			speaker = i['character']['speaker']
			displayName = i['character']['displayName']
			expression = i['expression']
			charPos = i['charPos']
			strID = i['strID']
			contentSize = i['contentSize']
			isClearModle = i['isClearModle']
			CharFadeIn = i['CharFadeIn']
			CharFadeOut = i['CharFadeOut']
			voiceID = i['voice']['id']
			voiceFirst = i['voice']['first']
			sfxID = i['sfx']['id']
			sfxFirst = i['sfx']['first']
			effect = i['effect']
			avgImageID = i['avgImageID']
			
			#check if there is suposed to be bgm
			if len(bgm_schedule) > 0:
				#see if music is supposed to stop
				if framecount not in bgm_schedule:
					f.write('stop music\n')
				#filter out the -1 bgm id
				elif bgm_schedule[framecount] == -1: 
					f.write('stop music\n')
				#then go back to normal
				else:
					framebgm = bgm_dict[bgm_schedule[framecount]]['_bgmName']
					if lastplayed != framebgm:
						#generate music line only if it's different from the last frame
						f.write(f'play music "{framebgm}"\n')
						lastplayed = framebgm
				
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
				f.write(f"scene {framebackground}\n")
				lastbackground = framebackground
				newscene = True
				#this might be dumb.  hoping it's a quick fix
				leftportrait = None
				rightportrait = None
			#check for memory overlay
			if len(memory_schedule) > 0:
				if framecount in memory_schedule:
					f.write('show memoryoverlay zorder 2\n')
					memory = True
				else:
					if memory:
						f.write('hide memoryoverlay\n')
						memory = False
			#moved the "scene with fade" down here to account for memory overlay
			if newscene and isClearModle != 1: f.write('with fade\n')


			if isClearModle == 1:
				if leftportrait:
					f.write(f"hide {leftalias}\n")
					leftportrait = None
				if rightportrait:
					f.write(f"hide {rightalias}\n")
					rightportrait = None
				if centerportrait:
					f.write(f"hide {centeralias}\n")
					centerportrait = None
				
			#check for sfx
			if sfxID != 0:
				sfxname = sfx_dict[sfxID]['_sfxName']
				sfxname = sfxname.split('/')[-1]
				#play sfx
				f.write(f'play sfx2 "{sfxname}"\n')
				
			#check for voice
			if voiceID != 0:
				voicename = voice_dict[voiceID]['_voiceName']
				voicename = voicename.split('/')[-1]
				#play voice
				f.write(f'play sfxvoice "{voicename}"\n')
				
			#check for image to display
			if avgImageID == 0:
				if showingimage:
					f.write(f'hide {avgimagename}\n')
					showingimage = None
			else:
				avgimagename = "Image"+str(avgImageID)
				if showingimage != avgimagename:
					f.write(f'show {avgimagename} zorder 4\n')
					showingimage = avgimagename
				
			#convert dialogue string to display correctly
			dialogue = f"[textdict[{strID}]]"

			#figure out if a namebox needs to be displayed
			if speaker == 0:
				if leftportrait:
					f.write(f"hide {leftalias}\n")
					leftportrait = None
				if rightportrait:
					f.write(f"hide {rightalias}\n")
					rightportrait = None
				if centerportrait:
					f.write(f"hide {centeralias}\n")
					centerportrait = None
			
			#figure out where namebox goes
			if speaker == 0: nameboxPos = ''
			elif charPos == 1: nameboxPos = 1
			else: nameboxPos = 3
			
			#figure out if a portrait needs to be displayed 
			if charID == 0:
				folderName = None
			else:
				folderName = avg_role_dict[charID]['_folderName']
				
			#figure out xoffset
			if folderName: 
				offset = str(int(avg_role_dict[charID]['_xPostion']))
				folderAlias = f'c{speaker}portrait'
			else:
				offset = '0'
				
			
			#figure out where on the screen character portrait goes
			if charPos == 1: 
				portraitpos = 'leftside'
				if leftportrait:
					f.write(f"hide {leftalias}\n")
					leftportrait = None
				if folderName: 
					leftportrait = folderName
					leftalias = folderAlias
					leftexpression = str(expression)
					leftoffset = offset
					
					#hoping this fixes when the character changes sides
					#but wasn't replaced on the other side by another portrait
					#(like chloe in avg 12049)
					if leftalias == rightalias and rightportrait: 
						f.write(f"hide {rightalias}\n")
						rightportrait = None
					
				else: leftportrait = None
				
				if rightportrait: 
					f.write(f"hide {rightalias}\n")
					f.write(f"show {rightportrait} {rightexpression} as {rightalias} at darkright({rightoffset}), zorder 5\n")
			
				
			elif charPos == 3: 
				portraitpos = 'rightside'
				if rightportrait:
					f.write(f"hide {rightalias}\n")
					rightportrait = None
				if folderName: 
					rightportrait = folderName
					rightalias = folderAlias
					rightexpression = str(expression)
					rightoffset = offset
					
					
					#hoping this fixes when the character changes sides
					#but wasn't replaced on the other side by another portrait
					if rightalias == leftalias and leftportrait: 
						f.write(f"hide {leftalias}\n")
						leftportrait = None
					
				else: rightportrait = None
				
				if leftportrait: 
					f.write(f"hide {leftalias}\n")
					f.write(f"show {leftportrait} {leftexpression} as {leftalias} at darkleft({leftoffset}), zorder 6\n")
				
			elif charPos == 2: 
				portraitpos = 'centerpos'
				if centerportrait:
					f.write(f"hide {centeralias}\n")
				if folderName: 
					centerportrait = folderName
					centeralias = folderAlias
					centerexpression = str(expression)
					centeroffset = offset
				else: centerportrait = None
			
			#this is mostly for the extra unused scenes that don't have charpos set
			#but need to make sure it doesn't screw up system messages that also use charPos 0
			elif charPos == 0:
				portraitpos = 'centerpos'
				if rightportrait and isClearModle != 1:
					f.write(f"hide {rightalias}\n")
					rightportrait = None
				if leftportrait and isClearModle != 1:
					f.write(f"hide {leftalias}\n")
					leftportrait = None
				if centerportrait and isClearModle != 1:
					f.write(f"hide {centeralias}\n")
					centerportrait = None
				if folderName:
					centerportrait = folderName
					centeralias = folderAlias			
				
			#check if portrait is entering or exiting:
			if CharFadeIn == 1: portraitpos += 'entrance'
			if CharFadeOut == 1:  portraitpos += 'exit'
				
			#moved midback up here so it can get the xoffset added to it	
			if effect == 103 or effect == 203: portraitpos += 'midback'
			
			portraitpos += f'({offset})'

			#then get effects figured out
			if effect == 102: portraitpos += ', shakeright'
			elif effect == 202: portraitpos += ', shakeleft'

			#SHOW PORTRAIT
			if folderName:									
				portrait = f'show {folderName} {expression} as {folderAlias} at {portraitpos}, zorder 5' 
				f.write(f"{portrait}\n")
			#need the fade after all images are set up, before dialogue appears
			if isClearModle == 1: f.write(f"with fade\n")
			
			#START OF SAY STATEMENT
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
			
			f.write(f"{say}\n")
			
			#make sure it doesn't try to show the dark portrait after the portrait has left
			if CharFadeOut == 1:
				f.write(f"hide {folderAlias}\n")
				if charPos == 1: leftportrait = None
				elif charPos == 2 or charPos == 3: rightportrait = None
			

		#FIGURE OUT IF THERE ARE CHOICES
		if script_json["ending"]["type"] == 1:
			f.write('menu:\n')
			#keep dialogue displayed during choice menu:
			f.write('    extend ""\n')
			for choice in range(0, len(script_json["ending"]["options"])):
				choicestrID = script_json["ending"]["options"][choice]["strID"]
				choicetext = f"[textdict[{choicestrID}]]"
				choiceavgID = script_json["ending"]["options"][choice]["avgID"]
				f.write(f'    "{choicetext}":\n')
				#f.write(f'        jump avg{choiceavgID}\n')
				f.write(f'        call avg{choiceavgID}\n')
				
		#END OF SCRIPT)
		f.write('return')
		
	f.close()



