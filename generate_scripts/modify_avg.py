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

# Takes tuples or lists, where the first item is the schedule list's dictionary key, 
# and the second item is the schedule entry to be inserted
def insert_schedule(script_json, *args):
	for arg in args:
		key = arg[0]
		schedule = script_json[key]
	
		new_entry = arg[1]
		
		if not new_entry['end']: 
			new_entry['end'] = len(script_json['dialogueFrames'])
	
		if len(schedule) == 0:
			schedule.append(new_entry)
			
		else:
			start = new_entry['start']
			end = new_entry['end']
			new_span = range(start, end)
			
			placed = False
			for copy in schedule[:]:
				entry_index = schedule.index(copy)
				entry = schedule[entry_index]

				if entry['start'] in new_span:
					#remove the entire old entry if it would have started and ended during the new entry
					if entry['end'] in new_span:
						schedule.remove(entry)
					#or else keep the end, and push the start time back until after the new entry is over
					else:
						entry['start'] = (end+1)
						
				elif entry['start'] < start:
					#cut the old entry short, to end immediately before the new entry starts
					if entry['end'] in new_span:
						entry['end'] = (start-1)

				#Insert the new entry immediately before the first (adjusted) entry that starts after it
				if not placed:
					if entry['start'] > end:
						schedule.insert((entry_index-1), new_entry)
						placed = True
			#Append the new entry to the end of the list if it wasn't inserted into the middle earlier
			if not placed:
				schedule.append(new_entry)
				placed = True
			
	
##################################################################################################
#Modifies the original cutscene scripts, to make corrections or adjustments
def make_edits(script_json, avgID):
	avgID = str(avgID)

#Trying to group these into different priority levels so that they can be undone if they're stupid
#Don't know yet what I'm going to do when a single scene needs two different levels of changes made to it...

###########################################################################
# Purely corrective changes - no real reason to ever need to undo these
###########################################################################

#Fix unset charPos

	#詐欺事件の調査（1） 4/6
	if avgID == '10008':
		script_json['dialogueFrames'][98]['charPos'] = 1
		script_json['dialogueFrames'][98]['character']['mirror'] = 1
	
	#元マフィアの隠れ家を再捜索 1/4
	elif avgID == '12766':
		script_json['dialogueFrames'][16]['charPos'] = 1

#Apply corrections to script, found in mobile version files

	#Both of these are 防空訓練(2) 7/7
	elif avgID == '10330':
		script_json['dialogueFrames'][85]['strID'] = 1130996
		script_json['dialogueFrames'][115]['strID'] = 1130966
	elif avgID == '10331':
		script_json['dialogueFrames'][88]['strID'] = 1130996
		script_json['dialogueFrames'][88]['character']['charID'] = 4
		script_json['dialogueFrames'][88]['character']['speaker'] = 4
		script_json['dialogueFrames'][118]['strID'] = 1130966
	
#CharFadeOut was set on the wrong line

	#「絵空の記憶」　8/12
	elif avgID == '1138':
		script_json['dialogueFrames'][108]['CharFadeOut'] = 1
		script_json['dialogueFrames'][109]['CharFadeOut'] = 0
		
	#Bracer’s kitchen! 後日談
	elif avgID == '1209':
		script_json['dialogueFrames'][14]['CharFadeOut'] = 1
		script_json['dialogueFrames'][15]['CharFadeOut'] = 0
		
######################################################################################
# Subjective changes - up to interpretation, someone may want to change or undo these
######################################################################################

	#クロスベル市内の地図作成 2/7
	#Remove an extra redundant line - both lines are spoken by the same person, and say the same thing.
	#It is not a mis-set speaker name, because there is a third line that says the same thing again, spoken by the other person.
	#This could also be changed to remove line 15 instead, if preferred.
	elif avgID == '12038':
		delete_frame(script_json, 14)

	#爆弾の捜索（1） 8/13
	#This scene takes place at the harbor, so change it to use the harbor background
	elif avgID == '20050':
		script_json['backgrounds'][0]['id'] = 28
		
	#エルベ離宮への荷物配達 4/4
	#This scene has a footstep sound to indicate that they have moved location/gone back downstairs
	#So I added an indoor background/bgm to the first half to match the first scene of the quest
	elif avgID == '12159':
		insert_schedule(script_json,
			('backgrounds', {'id': 38, 'start': 1, 'end': 3}),
			('bgm', {'id': 132, 'start': 1, 'end': 3})
		)

	#Blue Air 5/7
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
	
#################################################################################
# Add backgrounds (and maybe music?) to scenes that did not originally have them
#################################################################################

#Chapter 1

	#爆弾の捜索（1） 9/13
	#Add a Grancel street background to match the surrounding scenes
	elif avgID == '20052':
		insert_schedule(script_json,
			('backgrounds', {'id': 27, 'start': 1, 'end': None})
		)

###########################################################################
	return script_json
