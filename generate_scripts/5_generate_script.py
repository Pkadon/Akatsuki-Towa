import json
from pathlib import Path
import os

direc = Path.cwd()
scriptdirec = direc / 'MonoBehaviour'
targetdirec = direc / 'Renpy_Scripts' / 'scripts'
if not os.path.exists(targetdirec):
	os.makedirs(targetdirec)
	
#IMPORT AVG ROLE
with open((scriptdirec / 'avg_role.json'), 'r', encoding="utf-8")as txt:
	avgrole_json = json.load(txt)
avgroledict = dict()
for i in range(0, len(avgrole_json['_rows'])):
	i = avgrole_json['_rows'][i]
	avgroleid = i['_id']
	avgroledict[avgroleid] = {
	'roleName': i["_roleName"],
	'folderName': i["_folderName"],
	'xPosition': i['_xPostion']
	}
#IMPORT BGM
with open((scriptdirec / 'bgm.json'), 'r', encoding="utf-8")as txt:
	bgm_json = json.load(txt)
bgmdict = dict()
for i in range(0, len(bgm_json['_rows'])):
	i = bgm_json['_rows'][i]
	bgmid = i['_id']
	bgmname = i['_bgmName']
	bgmdict[bgmid] = {
	'bgmname': bgmname,
	}
#IMPORT SFX
with open((scriptdirec / 'sfx.json'), 'r', encoding="utf-8")as txt:
	sfx_json = json.load(txt)
sfxdict = dict()
for i in range(0, len(sfx_json['_rows'])):
	i = sfx_json['_rows'][i]
	sfxid = i['_id']
	sfxName = i['_sfxName']
	sfxdict[sfxid] = {
	'sfxName': sfxName,
	}	
#IMPORT VOICE
with open((scriptdirec / 'voice.json'), 'r', encoding="utf-8")as txt:
	voice_json = json.load(txt)
voicedict = dict()
for i in range(0, len(voice_json['_rows'])):
	i = voice_json['_rows'][i]
	voiceid = i['_id']
	voiceName = i['_voiceName']
	voicedict[voiceid] = {
	'voiceName': voiceName,
	}	
	
###START
for cutscenepath in list(scriptdirec.glob('*.json')):
	fname = cutscenepath.stem
	#just to weed out the other files that were in the same folder
	if not fname[0].isdigit(): continue
	
	print(fname)
	#IMPORT SCRIPT JSON
	with open(cutscenepath, 'r', encoding="utf-8")as txt:
		script_json = json.load(txt)
	framedict = dict()

	#FIGURE OUT BACKGROUND SCHEDULE
	background_schedule = dict()
	for i in range(0, len(script_json['backgrounds'])):
		i = script_json['backgrounds'][i]
		backgroundid = i['id']
		start = i['start']
		end = i['end']
		for dframe in range(start, end+1):
			background_schedule[dframe] = backgroundid
			
	#FIGURE OUT BGM SCHEDULE
	bgm_schedule = dict()
	for i in range(0, len(script_json['bgm'])):
		i = script_json['bgm'][i]
		bgmid = i['id']
		start = i['start']
		end = i['end']
		for dframe in range(start, end+1):
			bgm_schedule[dframe] = bgmid
			
	#FIGURE OUT MEMORY SCHEDULE
	memory_schedule = dict()
	for i in range(0, len(script_json['memory'])):
		i = script_json['memory'][i]
		memoryid = i['id']
		start = i['start']
		end = i['end']
		for dframe in range(start, end+1):
			memory_schedule[dframe] = memoryid
		

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
		for i in range(0, len(script_json['dialogueFrames'])):
			framecount = i+1
			newscene = False

			i = script_json['dialogueFrames'][i]
			template = i['template']
			charID = i['character']['charID']
			speaker = i['character']['speaker']
			displayName = i['character']['displayName']
			mirror = i['character']['mirror']
			expression = i['expression']
			charPos = i['charPos']
			strID = i['strID']
			ifAphs = i['isApha']
			nameSize = i['nameSize']
			contentSize = i['contentSize']
			isClearModle = i['isClearModle']
			CharFadeIn = i['CharFadeIn']
			CharFadeOut = i['CharFadeOut']
			voiceID = i['voice']['id']
			voiceFirst = i['voice']['first']
			sfxID = i['sfx']['id']
			sfxFirst = i['sfx']['first']
			effect = i['effect']
			itemID = i['itemID']
			itemIconID = i['itemIconID']
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
					framebgm = bgmdict[bgm_schedule[framecount]]['bgmname']
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
				sfxname = sfxdict[sfxID]['sfxName']
				sfxname = sfxname.split('/')[-1]
				#play sfx
				f.write(f'play sfx2 "{sfxname}"\n')
				
			#check for voice
			if voiceID != 0:
				voicename = voicedict[voiceID]['voiceName']
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
				folderName = avgroledict[charID]['folderName']
				
			#figure out xoffset
			if folderName: 
				offset = str(int(avgroledict[charID]['xPosition']))
				folderAlias = f'c{speaker}portrait'
			else:
				offset = '0'
				
			
			#figure out where on the screen character portrait goes
			if charPos == 1: 
				portraitpos = 'leftside'
				if leftportrait:
					f.write(f"hide {leftalias}\n")
				if folderName: 
					leftportrait = folderName
					leftalias = folderAlias
					leftexpression = str(expression)
					leftoffset = offset
					
					#hoping this fixes when the character changes sides
					#but wasn't replaced on the other side by another portrait
					#(like chloe in avg 12049)
					if rightalias == leftalias: rightportrait = None
					
				else: leftportrait = None
				
				if rightportrait: 
					f.write(f"hide {rightalias}\n")
					f.write(f"show {rightportrait} {rightexpression} as {rightalias} at darkright({rightoffset}), zorder 5\n")
			
				
			elif charPos == 3: 
				portraitpos = 'rightside'
				if rightportrait:
					f.write(f"hide {rightalias}\n")
				if folderName: 
					rightportrait = folderName
					rightalias = folderAlias
					rightexpression = str(expression)
					rightoffset = offset
					
					
					#hoping this fixes when the character changes sides
					#but wasn't replaced on the other side by another portrait
					if leftalias == rightalias: leftportrait = None
					
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
				else: say+= f' (what_size={contentSize})'

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



