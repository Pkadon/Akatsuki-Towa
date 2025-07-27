def delete_frame(script_json, frame_index):
	#Delete the frame itself
	del script_json['dialogueFrames'][frame_index]
	
	#Then adjust all of the schedules to account for the missing frame
	frame_id = (frame_index + 1) #the schedules count starting from 1 instead of 0
	for key in ['backgrounds', 'bgm', 'memory']:
		if key in script_json:
			schedule = script_json[key]
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

##################################################################################################
#Modifies the original cutscene scripts, to fix corrections or to make improvements
def make_edits(script_json, avgID):
	avgID = str(avgID)

#Trying to group these into different priority levels so that they can be undone if they're stupid
#Don't know yet what I'm going to do when a single scene needs multiple changes made to it...

###########################################################################
# Purely corrective changes - no real reason to ever need to undo these
###########################################################################
	#Fix unset charPos
	if avgID == '10008':
		script_json['dialogueFrames'][98]['charPos'] = 1
		script_json['dialogueFrames'][98]['character']['mirror'] = 1
	elif avgID == '12766':
		script_json['dialogueFrames'][16]['charPos'] = 1

	#Apply corrections to script, found in mobile version files
	elif avgID == '10330':
		script_json['dialogueFrames'][85]['strID'] = 1130996
		script_json['dialogueFrames'][115]['strID'] = 1130966
	elif avgID == '10331':
		script_json['dialogueFrames'][88]['strID'] = 1130996
		script_json['dialogueFrames'][88]['character']['charID'] = 4
		script_json['dialogueFrames'][88]['character']['speaker'] = 4
		script_json['dialogueFrames'][118]['strID'] = 1130966
	
	#The CharFadeOut was on the wrong line
	elif avgID == '1138':
		script_json['dialogueFrames'][108]['CharFadeOut'] = 1
		script_json['dialogueFrames'][109]['CharFadeOut'] = 0
	elif avgID == '1209':
		script_json['dialogueFrames'][14]['CharFadeOut'] = 1
		script_json['dialogueFrames'][15]['CharFadeOut'] = 0
		
######################################################################################
# Subjective changes - up to interpretation, someone may want to change or undo these
######################################################################################
	#This one was all kinds of messed up.
	#It would also be possible to change it to hide the Nacht portrait on line 94,
	#and interpret all of the dialogue after that as occuring "off-screen".
	#But since they had already set up the animations in the files,
	#I changed it to show the portraits that were "missing" here instead
	elif avgID == '1226':
		#missing portrait and expression
		script_json['dialogueFrames'][96]['character']['charID'] = 1
		script_json['dialogueFrames'][96]['expression'] = 14 #expression was unset so this is a guess
		
		#missing portrait and expression, and misplaced CharFadeOut
		script_json['dialogueFrames'][98]['character']['charID'] = 1
		script_json['dialogueFrames'][98]['expression'] = 12 #expression was unset so this is a guess
		script_json['dialogueFrames'][98]['CharFadeOut'] = 1
		script_json['dialogueFrames'][99]['CharFadeOut'] = 0

	#This scene has a footstep sound to indicate that they have moved location/gone back downstairs
	#So I added an indoor background/bgm to the first half to match the first scene of the quest
	elif avgID == '12159':
		script_json['backgrounds'].insert(0, {'id': 38, 'start': 1, 'end': 3})
		script_json['backgrounds'][1]['start'] = 4
		script_json['bgm'].insert(0, {'id': 132, 'start': 1, 'end': 3})
		script_json['bgm'][1]['start'] = 4
		
	#This scene takes place at the harbor, so this gives it the harbor background
	elif avgID == '20050':
		script_json['backgrounds'][0]['id'] = 28
		
	#Remove an extra redundant line - both lines are spoken by the same person, and say the same thing.
	#It is not a mis-set speaker name, because there is a third line that says the same thing again, spoken by the other person.
	#This could also be changed to remove line 15 instead, if preferred.
	elif avgID == '12038':
		delete_frame(script_json, 14)
	
#################################################################################
# Add backgrounds (and maybe music?) to scenes that did not originally have them
#################################################################################
	#Changed from no background to Grancel background to match surrounding scenes
	elif avgID == '20052':
		script_json['backgrounds'].insert(0, {'id': 27, 'start': 1, 'end': 32}) 
		
		
###########################################################################
	return script_json
