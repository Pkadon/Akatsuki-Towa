import json
from pathlib import Path
import os
import re

direc = Path.cwd()
exdirec = direc / 'extra_json'

outputdirec = direc / "Renpy_scripts"
if not os.path.exists(outputdirec):
	os.makedirs(outputdirec)

combinescenelist = [
	'new_story.json',
	'new_training.json',
	'EX_story_training.json',
	'EX12_event.json',
	'EX13_exploration.json',
	'EX14_daily.json',
	'EX15_unused.json'
]
combinescenedict = dict()

combinequestlist = [
	'new_quest.json',
	'EXQ_unusedquestlog.json'
]
combinequestdict = dict()

def scenejsonmerger(exjson):
	with open(exjson, 'r', encoding="utf-8")as txt:
		ex = json.load(txt)
		
	for category in list(ex.keys()):
		excategory = ex[category]
		if category not in combinescenedict:
			combinescenedict[category] = excategory 
			
			combinecategory = combinescenedict[category]
			
		else:
			combinecategory = combinescenedict[category]
			
			exlevel1 = excategory['level1']
			combinelevel1 = combinecategory['level1']
			for level1 in list(exlevel1.keys()):
				
				if level1 not in combinelevel1:
					combinelevel1[level1] = exlevel1[level1]
					
				else:
					exlevel2 = exlevel1[level1]['level2']
					combinelevel2 = combinelevel1[level1]['level2']
					for level2 in list(exlevel2.keys()):
						
						if level2 not in combinelevel2:
							combinelevel2[level2] = exlevel2[level2]
					
						else:
							buttonlist = []
							for button in  range(int(level2), len(combinelevel2)+1):
								buttonlist.append(button)
							buttonlist.reverse()
							
							#moving everything over one to make room for the entry being inserted
							for button in buttonlist:
								combinelevel2[str(button+1)] = combinelevel2[str(button)]
							
							combinelevel2[level2] = exlevel2[level2]
							
def questjsonmerger(questjson):
	with open(questjson, 'r', encoding="utf-8")as txt:
		ex = json.load(txt)
	for quest in list(ex.keys()):
		if quest not in combinequestdict:
			combinequestdict[quest] = ex[quest]


for f in combinescenelist:
	f = exdirec / f
	if os.path.isfile(f):
		scenejsonmerger(f)							
#with open(exdirec / 'combinedstory.json', 'w', encoding='utf-8') as f:
#	json.dump(combinescenedict, f, ensure_ascii=False, indent=4)
	

for f in combinequestlist:
	f = exdirec / f
	if os.path.isfile(f):
		questjsonmerger(f)	
#with open(exdirec / 'combinedquest.json', 'w', encoding='utf-8') as f:
#	json.dump(combinequestdict, f, ensure_ascii=False, indent=4)
					
########################################################
###now make menu from the new dictionaries

with open((outputdirec / "episodelist.rpy"),'w', encoding="utf-8") as f:
	#screen label
	f.write('label episodelist:\n')
	
	#workaround to be able to use substrings 
	#they need to be predefined or they make renpy crash
	#this is now only used to fix three story quest typos
	f.write('init python:\n')
	for categorynumber in range(1, (len(combinescenedict)+1)):
		category = combinescenedict[str(categorynumber)]
		categorynumber = str(categorynumber)
		while len(categorynumber) < 2: categorynumber = '0'+categorynumber
		#quest name
		for questnumber in range(1, (len(category['level1'])+1)):
			quest = category['level1'][str(questnumber)]
			questnumber = str(questnumber)
			while len(questnumber) < 2: questnumber = '0'+questnumber
			
			if 'strID' in quest and quest['strID'] != None:
				if 'sub' in quest: 
					sub=fr'[:-{quest["sub"]}]'
					if 'add' in quest: add=fr'+"{quest["add"]}"'
					else: add=''
					f.write(f'    text{categorynumber+questnumber} = textdict[{quest["strID"]}]{sub}{add}\n')
			#scene name
			for scenenumber in range(1, (len(quest['level2'])+1)):
				scene = quest['level2'][str(scenenumber)]
				
				if 'strID' in scene and scene['strID'] != None:
					if 'sub' in scene: 
						sub=fr'[:-{scene["sub"]}]'
						if 'add' in scene: add=fr'+"{scene["add"]}"'
						else: add = ''
						f.write(f'    text{categorynumber+questnumber+str(scenenumber)} = textdict[{scene["strID"]}]{sub}{add}\n')	

				
	f.write('    \n')

	#define window
	f.write('screen episodelist():\n')
	f.write('    window:\n')
	f.write('        xysize (840,480)\n')
	f.write('        background "sceneselect"\n')

	#back button
	f.write('        button:\n')
	f.write('            xysize(94,37)\n')
	f.write('            background Frame("backbutton", 16, 16)\n')
	f.write('            text "Back":\n')
	f.write('                align (0.5, 1.0)\n')
	f.write('                size 25\n')
	f.write('            action Hide("episodelist")\n')
	
	#open Jump/Code Input menu
	f.write('        button:\n')
	f.write('            xysize(94,37)\n')
	f.write('            ypos 37\n')
	f.write('            background Frame("backbutton", 16, 16)\n')
	f.write('            text "Jump":\n')
	f.write('                align (0.5, 1.0)\n')
	f.write('                size 25\n')
	f.write('            action Replay("codeinput", locked=False)\n')
	
	#open Extra/Sprite Test menu
	f.write('        button:\n')
	f.write('            xysize(94,37)\n')
	f.write('            ypos 74\n')
	f.write('            background Frame("backbutton", 16, 16)\n')
	f.write('            text "Extra":\n')
	f.write('                align (0.5, 1.0)\n')
	f.write('                size 25\n')
	f.write('            action Replay("spritetest", locked=False)\n')

	#horizontal viewport to hold menu columns
	f.write('        viewport:\n')
	f.write('            xpos 94\n')
	f.write('            xsize 740\n')
	f.write('            draggable True\n')
	f.write('            scrollbars "horizontal"\n')
	f.write('            hbox:\n')
	
	for categorynumber in range(1, (len(combinescenedict)+1)):
		category = combinescenedict[str(categorynumber)]
		categorynumber = str(categorynumber)
		while len(categorynumber) < 2: categorynumber = '0'+categorynumber
		
		if 'strID' in category and category['strID'] != None: 
			level0 = f"[textdict[{category['strID']}]]"
		else: level0 = category['name']

		f.write('                vbox:\n')
		f.write('                    button:\n')
		f.write('                        xysize(330,37)\n')
		f.write('                        xpos 2\n')
		f.write('                        background Frame("booktab1")\n')
		f.write('                        bottom_padding 4\n')
		f.write(f'                        text "{level0}":\n')
		f.write('                            xalign (0.5)\n')
		f.write('                            ypos -2\n')
		f.write('                             #size 10\n')
		f.write('                    viewport:\n')
		f.write('                        xsize 355\n')
		f.write('                        ysize 0.96\n')
		f.write('                        draggable True\n')
		f.write('                        mousewheel True\n')
		f.write('                        scrollbars "vertical"\n')
		f.write('                        vbox:\n')
		
		for questnumber in range(1, (len(category['level1'])+1)):
			quest = category['level1'][str(questnumber)]
			questnumber = str(questnumber)
			while len(questnumber) < 2: questnumber = '0'+questnumber
			
			scenemenu = "quest"+categorynumber+questnumber
			
			if 'strID' in quest and quest['strID'] != None:
				if 'add' in quest: add=fr'{quest["add"]}'
				else: add = ''
				level1 = f"[textdict[{quest['strID']}]]{add}"	
				if 'sub' in quest: level1 = f'[text{categorynumber+questnumber}]'
			else: level1 = quest['name']
			
			f.write('                            button:\n')
			f.write('                                xysize(330,37)\n')
			f.write('                                background Frame("booktab2")\n')
			f.write('                                bottom_padding 4\n')
			f.write(f'                                text "{level1}":\n')
			f.write('                                    xalign 0.5\n')
			f.write('                                    ypos -2\n')
			f.write('                                    #size 10\n')
			f.write(f'                                action ShowMenu("{scenemenu}")\n')


	f.write('\n')
	f.write('#QUEST MENUS###################################################\n')
	f.write('\n')
	
	for categorynumber in range(1, (len(combinescenedict)+1)):
		category = combinescenedict[str(categorynumber)]
		categorynumber = str(categorynumber)
		while len(categorynumber) < 2: categorynumber = '0'+categorynumber
		for questnumber in range(1, (len(category['level1'])+1)):
			quest = category['level1'][str(questnumber)]
			questnumber = str(questnumber)
			while len(questnumber) < 2: questnumber = '0'+questnumber
			menuname = "quest"+categorynumber+questnumber
			
			#define window
			f.write(f'screen {menuname}():\n')
			f.write('    modal True\n')
			f.write('    window:\n')
			f.write('        xysize (840,480)\n')
			f.write('        background "sceneselect"\n')
			#back button
			f.write('        button:\n')
			f.write('            xysize(94,37)\n')
			f.write('            background Frame("backbutton", 16, 16)\n')
			f.write('            text "Back":\n')
			f.write('                align (0.5,1.0)\n')
			f.write('                size 25\n')
			f.write(f'            action Hide("{menuname}")\n')
			
			#BUTTONS TO VIEW QUESTLOG(S)
			if 'questID' in quest and len(quest['questID']) > 0:
				f.write('        viewport:\n')
				f.write('            ypos 37\n')
				f.write('            xysize (114,443)\n')
				if len(quest['questID']) > 12:
					f.write('            draggable True\n')
					f.write('            mousewheel True\n')
					f.write('            scrollbars "vertical"\n')
				f.write('            vbox:\n')
				logcount = 0
				for log in quest['questID']:
					logcount+=1
					logname = f"log{log}"
					f.write('                button:\n')
					f.write('                    xysize(94,37)\n')
					f.write('                    background Frame("backbutton", 16, 16)\n')
					f.write(f'                    text "Log {str(logcount)}":\n')
					f.write('                        align (0.5,1.0)\n')
					f.write('                        size 25\n')
					f.write(f'                    action ShowMenu("{logname}")\n')

			#start of menu
			f.write('        viewport:\n')
			f.write('            xpos 119\n')
			f.write('            xsize 720\n')
			#don't add a scrollbar if there aren't enough buttons to fill the screen
			if len(quest['level2']) > 8:
				f.write('            draggable True\n')
				f.write('            mousewheel True\n')
				f.write('            scrollbars "vertical"\n')	
			f.write('            vbox:\n')
			f.write('                xsize 700\n')

			#make a label at the top
			if 'strID' in quest and quest['strID'] != None:
				if 'add' in quest: add=fr'{quest["add"]}'
				else: add = ''
				level1 = f"[textdict[{quest['strID']}]]{add}"	
				if 'sub' in quest: level1 = f'[text{categorynumber+questnumber}]'
			else: level1 = quest['name']
			
			f.write('                button:\n')
			f.write('                    xysize(330,37)\n')
			f.write('                    xalign 0.5\n')
			f.write('                    background Frame("booktab2")\n')
			f.write('                    bottom_padding 4\n')
			f.write(f'                    text "{level1}":\n')
			f.write('                        xalign (0.5)\n')
			f.write('                        ypos -2\n')
			f.write('                         #size 10\n')
			
			f.write('                hbox:\n')
			hboxcount = 0	
			
			for scenenumber in range(1, (len(quest['level2'])+1)):
				scene = quest['level2'][str(scenenumber)]

				#scene name
				if 'strID' in scene and scene['strID'] != None:
					if 'add' in scene: add=fr'{scene["add"]}'
					else: add = ''
					scenename = f'[textdict[{scene["strID"]}]]{add}'
					if 'sub' in scene: scenename = f'[text{categorynumber+questnumber+str(scenenumber)}]'	
				else: scenename = scene['name']
			
				#scene info
				if 'infostrID' in scene and scene['infostrID'] != None:
					sceneinfo = fr"\n[textdict[{scene['infostrID']}]]"
				elif 'info' in scene and scene['info'] != None:
					sceneinfo = r'\n'+scene['info']
				else: sceneinfo = ''
				
				#combine name and info into one line
				level2 = fr"{scenename}{sceneinfo}"
				
				#avgfile
				avgnumber = scene['avgID']
				
				#back to making menu
				if hboxcount == 2:
					f.write('                hbox:\n')
					hboxcount = 0
					
				f.write('                    button:\n')
				f.write('                        xysize(350,108)\n')
				f.write('                        left_padding 4\n')
				f.write('                        right_padding 20\n')
				f.write('                        background Frame("bookpage", 35, 35)\n')
				f.write(f'                        text "{level2}":\n')
				f.write('                            align (0.5,0.5)\n')
				f.write('                            size 18\n')
				f.write(f'                        action Replay("avg{avgnumber}", locked=False)\n')
				
				hboxcount+=1
	f.write('return')
f.close()

#QUEST LOG MENUS
with open((outputdirec / "questlog.rpy"),'w', encoding="utf-8") as f:	
	f.write(f'label questlog:\n')
	
	for key in list(combinequestdict.keys()):
		log = combinequestdict[key]
		logname = "log"+str(key)
		#define window
		f.write(f'screen {logname}():\n')
		f.write('    modal True\n')
		f.write('    window:\n')
		f.write('        xysize (840,480)\n')
		f.write('        background "sceneselect"\n')
		
		#back button
		f.write('        button:\n')
		f.write('            xysize(94,37)\n')
		f.write('            background Frame("backbutton", 16, 16)\n')
		f.write('            text "Back":\n')
		f.write('                align (0.5,1.0)\n')
		f.write('                size 25\n')
		f.write(f'            action Hide("{logname}")\n')
		
		#start of menu
		f.write('        viewport:\n')
		f.write('            xpos 119\n')
		f.write('            xsize 680\n')
		f.write('            draggable True\n')
		f.write('            mousewheel True\n')
		f.write('            scrollbars "vertical"\n')
		f.write('            vscrollbar_unscrollable "hide"\n')
		f.write('            vbox:\n')
		f.write('                button:\n')
		f.write('                    xysize(650,None)\n')
		f.write('                    left_padding 20\n')
		f.write('                    right_padding 40\n')
		f.write('                    background Frame("bookpage", 35, 35)\n')
		
		#build log
		#prefix
		if log['type'] == 1: titleprefix = '(MAIN)'
		elif log['type'] == 2: titleprefix = '(SUB)'
		elif log['type'] == 0: titleprefix = ''
		#title
		title = f'[textdict[{log["strID"]}]]'
		fulltext = fr'{titleprefix} {title} \n'
		#level
		fulltext += fr'【推奨レベル】 {str(log["level"])}\n'
		#client
		fulltext += fr'【依頼人】 [textdict[{log["client"]}]]\n'
		#description
		fulltext += fr'【内容】 [textdict[{log["description"]}]]\n'
		#steps
		for step in log['steps']:
			fulltext += fr' ● [textdict[{step}]]\n'
		
		#write log
		f.write(f'                    text "{fulltext}":\n')
		f.write('                        align (0.5,0.2)\n')
		f.write('                        size 16\n')
				
	f.write('return')
