####################################
# EFFECT KEY:
#    1 - Shakes the entire screen
#    202 - Shakes portrait, mainly used on left-side portraits
#    102 - Shakes portrait, mainly used on right-side portraits
#    203 - Animation that moves portrait from left-position, to the middle of the screen, then back to it starting point
#    103 - Animation that moves portrait from right-position, to the middle of the screen, then back to it starting point
#    'CharFadeIn' - Slides the portrait into position from off-screen
#    'ChaFadeOut' - Slides the portrait off-screen from its starting position
#    'isClearModle' - Fades to black, and hides all portraits that were shown before the current frame 
####################################


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

def insert_frame(script_json, frame_index, frame, edge_priority='first'):
	script_json['dialogueFrames'].insert(frame_index, frame)
	
	#Then adjust schedules
	#Schedules count from 1 instead of 0, so adjust to index + 1
	frame_id = (frame_index + 1)
	for key in ['backgrounds', 'bgm', 'memory']:
		if key in script_json:
			schedule = script_json[key]
			last_entry = (len(schedule) - 1)
			for copy in schedule[:]:
				entry_index = schedule.index(copy)
				entry = schedule[entry_index]
				
		#If the new frame is being inserted on the edge of two schedules: 
			#To include it in the first schedule (use edge_priority='first')
			#extend the "end" of the schedule before it, 
			#and delay the "start" of the second schedule by 1
			
			#To include the new frame in the second schedule instead, 
			#just insert the frame into the list, and move everything that comes after it up by 1 

				#This would extend the end of the first schedule to include the new frame
				if entry['end'] == (frame_id - 1) and edge_priority == 'first':
					entry['end'] += 1
				#All "end" values greater than the inserted frame's id need to be increased by 1 to account for the extra frame
				elif entry['end'] >= frame_id:
					entry['end'] += 1
				
				#If we aren't working on the very first schedule of the scene, this assumes
				#that the new frame was included in the earlier schedule, so this delays the second schedule by 1 to compensate
				if entry['start'] == frame_id and entry_index != 0:
					if edge_priority == 'first':
						entry['start'] += 1
				#If the "start" is the same as the inserted frame, it doesn't need to be adjusted
				elif entry['start'] > frame_id:
						entry['start'] += 1
						
			#Extend all of the schedules at the end if the frame is appended to the very end of the frame list
				if entry_index == last_entry and frame_id > entry['end']:
					entry['end'] += 1


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
			
def add_charpos(script_json, pos_dict, mode='frames'):
	keys = ['left', 'middle', 'right']
	ids = [1, 2, 3]
	for key, charPos in zip(keys, ids):
		if key in pos_dict:
			if mode == 'frames':
				frame_list = pos_dict[key]
				for frame_index in frame_list:
					script_json['dialogueFrames'][frame_index]['charPos'] = charPos
					if key == 'left':
						script_json['dialogueFrames'][frame_index]['character']['mirror'] = 1
			elif mode == 'speakers':
				speaker_list = pos_dict[key]
				for speaker in speaker_list:
					for frame in script_json['dialogueFrames']:
						if frame['character']['speaker'] == speaker:
							frame['charPos'] = charPos
							if key == 'left':
								frame['character']['mirror'] = 1

def add_effects(script_json, effect_dict):
	for effect in effect_dict.keys():
		if effect in  [1, 102, 202, 103, 203]:
			for frame_index in effect_dict[effect]:
				script_json['dialogueFrames'][frame_index]['effect'] = effect
		else:
			for frame_index in effect_dict[effect]:
				script_json['dialogueFrames'][frame_index][effect] = 1

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
		
#Missing portrait

	#中央工房の盗難事件(2) 4/7~ティオ
	elif avgID == '10088':
		script_json['dialogueFrames'][52]['character']['charID'] = 2

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

	#導力停止の異常事故(1) 1/9
	#Just remove this one, don't see anywhere else around that would make sense to have had one
	elif avgID == '10104': 
		script_json['dialogueFrames'][42]['CharFadeOut'] = 0
	
	#「絵空の記憶」　8/12
	elif avgID == '1138':
		script_json['dialogueFrames'][108]['CharFadeOut'] = 1
		script_json['dialogueFrames'][109]['CharFadeOut'] = 0
		
	#Bracer’s kitchen! 後日談
	elif avgID == '1209':
		script_json['dialogueFrames'][14]['CharFadeOut'] = 1
		script_json['dialogueFrames'][15]['CharFadeOut'] = 0
		
#Fix text size 

	#中央工房の盗難事件(2) 5/7 (Tita version only)
	elif avgID == '10097':
		#Text size is too small for some reason.  This does not happen in the Tio version.
		script_json['dialogueFrames'][31]['contentSize'] = 20
		
######################################################################################
# Subjective changes - up to interpretation, someone may want to change or undo these
######################################################################################

	#クロスベル市内の地図作成 2/7
	#Remove an extra redundant line - both lines are spoken by the same person, and say the same thing.
	#It is not a mis-set speaker name, because there is a third line that says the same thing again, spoken by the other person.
	#This could also be changed to remove line 15 instead, if preferred.
	elif avgID == '12038':
		delete_frame(script_json, 14)
		
	#エルベ離宮への荷物配達 4/4
	#This scene has a footstep sound to indicate that they have moved location/gone back downstairs
	#So I added an indoor background/bgm to the first half to match the first scene of the quest
	elif avgID == '12159':
		insert_schedule(script_json,
			('backgrounds', {'id': 38, 'start': 1, 'end': 3}),
			('bgm', {'id': 132, 'start': 1, 'end': 3})
		)
		
	#異常事故の総合的調査(1) 2/16
	#The speakers are all jumbled up
	#This change also assumes that the dialogue is being edited by loadinfo.rpy on startup
	#Preston should be the Police Chief, and get all dialogue using 私
	#Hogarth should be the Guardian Force commander, and get all dialogue using 僕
	elif avgID == '10043':
		script_json['dialogueFrames'][15]['character']['charID'] = 242
		script_json['dialogueFrames'][15]['character']['speaker'] = 242
		script_json['dialogueFrames'][15]['character']['mirror'] = 1
		script_json['dialogueFrames'][15]['charPos'] = 1
		
		script_json['dialogueFrames'][16]['character']['charID'] = 241
		script_json['dialogueFrames'][16]['character']['speaker'] = 241
		script_json['dialogueFrames'][16]['character']['mirror'] = 0
		script_json['dialogueFrames'][16]['charPos'] = 3
		
		script_json['dialogueFrames'][17]['character']['charID'] = 242
		script_json['dialogueFrames'][17]['character']['speaker'] = 242
		script_json['dialogueFrames'][17]['character']['mirror'] = 1
		script_json['dialogueFrames'][17]['charPos'] = 1
		
	#魔獣に囲まれたバス停 1/4
	#A Guardian Force portrait is used for a Crossbell Police Officer character
	#just remove all portraits for that speaker
	elif avgID == '12246':
		script_json['dialogueFrames'][1]['character']['charID'] = 0
		script_json['dialogueFrames'][2]['character']['charID'] = 0
		script_json['dialogueFrames'][4]['character']['charID'] = 0
		script_json['dialogueFrames'][5]['character']['charID'] = 0
		script_json['dialogueFrames'][8]['character']['charID'] = 0
	
	#導力停止の異常事故(1) 3/9
	#Change the roles used for Leitner's dialogue in this scene to use （通信） variants instead
	elif avgID == '10106':
		script_json['dialogueFrames'][0]['character']['speaker'] = 1167
		for index in [3, 4, 12, 13, 15, 16, 17, 18, 20, 21, 24, 26, 27, 30, 31]:
			script_json['dialogueFrames'][index]['character']['speaker'] = 1449
	
	#導力停止の異常事故(2) 8/14
	#Background does not change early enough, move everything back by 1
	elif avgID == '10120':
		insert_schedule(script_json,
			('backgrounds', {'id': 12, 'start': 1, 'end': 3}),
			('backgrounds', {'id': 33, 'start': 4, 'end': 9}),
		)
		
	#導力停止の異常事故(2) 14/14
	#Dudley's darkened portrait overstays its welcome after he should have already left
	#Add a ClearModle
	elif avgID == '10122':
		script_json['dialogueFrames'][13]['isClearModle'] = 1

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

#Prologue

	#遊撃士の認定試験 4/12, 5/12, 6/12, 7/12, 8/12
	elif avgID in ['20003', '20142', '29010', '20004', '20005']:
		#Add geofront background
		insert_schedule(script_json,
			('backgrounds', {'id': 71, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [2],
			'right': [1]
		}, mode='speakers')
		
		#Add bgm to 5/12, 6/12
		if avgID in ['20142', '29010']:
			insert_schedule(script_json,
				('bgm', {'id': 19, 'start': 1, 'end': None})
			)
			
		#Add effects to 4/12
		if avgID == '20003':
			add_effects(script_json, {
				'CharFadeIn': [0, 1],
				202: [10, 15, 24],
				102: [8]
			})
		#Add effect to 5/12
		elif avgID == '20142':
			add_effects(script_json, {
				202: [0]
			})
		#Add effect to 6/12
		elif avgID == '29010':
			add_effects(script_json, {
				202: [0]
			})
		#Add effect to 7/12
		elif avgID == '20004':
			add_effects(script_json, {
				202: [4],
				102: [0]
			})
		#Add effect to 8/12
		elif avgID == '20005':
			add_effects(script_json, {
				202: [0, 2, 4]
			})

	#紛失物の捜索願い 1/7
	elif avgID == '20010':
		#Add guild background
		insert_schedule(script_json,
			('backgrounds', {'id': 23, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'right': [1]
		}, mode='speakers')
	
	#《メゾン・イメルダ》の手配魔獣
	#1/4
	elif avgID == '20011':
		#Add guild background
		insert_schedule(script_json,
			('backgrounds', {'id': 23, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'right': [1]
		}, mode='speakers')
	#3/4, 4/4
	elif avgID in ['22001', '12002']:
		#Add apartment background
		insert_schedule(script_json,
			('backgrounds', {'id': 212, 'start': 1, 'end': None})
		)
		if avgID == '22001':
			#Add charpos to 3/4
			add_charpos(script_json, {
				'left': [2],
				'right': [1]
			}, mode='speakers')
			#Add effect to 3/4
			add_effects(script_json, {
				202: [1]
			})
		
	#詐欺事件の調査（2）
	#1/9
	elif avgID == '20012':
		#Hide the Michel portraits, since he's talking over the phone
		#(in the original game it just showed his head, so it made a little more sense)
		for frame_index in [14, 20, 22, 23, 24, 25, 27]:
			script_json['dialogueFrames'][frame_index]['character']['charID'] = 0
		#Add charpos
		add_charpos(script_json, {
			'left': [0, 2, 6, 8, 10, 12, 13, 15, 16, 18, 22, 23, 24, 25, 27, 28],
			'right': [1, 3, 4, 5, 7, 9, 11, 14, 19, 20, 21, 26]
		}, mode='frames')
		#Add effects
		add_effects(script_json, {
			202: [2, 6, 12],
			102: [9, 22]
		})
	#2/9
	elif avgID == '20013':
		#Add charpos
		add_charpos(script_json, {
			'left': [2],
			'right': [1]
		}, mode='speakers')
		#Add effect
		add_effects(script_json, {
			102: [2]
		})
	#3/9 (+ Choice #1, Choice #2)
	elif avgID in ['20014', '20015', '20016']:
		#Add airport background to all of these
		insert_schedule(script_json,
			('backgrounds', {'id': 8, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [2, 517],
			'right': [1]
		}, mode='speakers')
		
		#Add effect to 2/8
		if avgID == '20014':
			add_effects(script_json, {
				202: [1]
			})
		#Add effect to Choice #2
		elif avgID == '20016':
			add_effects(script_json, {
				202: [0]
			})
	#5/9, 6/9
	elif avgID in ['20017', '20018']:
		#Add Bose background to all of these
		insert_schedule(script_json,
			('backgrounds', {'id': 64, 'start': 1, 'end': None})
		)
		#Add charpos to all of these
		add_charpos(script_json, {
			'left': [2],
			'right': [1]
		}, mode='speakers')
		if avgID == '20017':
			#Add effect to 5/9
			add_effects(script_json, {
				'CharFadeIn': [0]
			})
		elif avgID == '20018':
			#Add effects to 6/9
			add_effects(script_json, {
				202: [2],
				'CharFadeOut': [3]
			})
	#7/9
	elif avgID == '20019':
		#Add roadway background
		insert_schedule(script_json,
			('backgrounds', {'id': 10, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [2],
			'right': [1]
		}, mode='speakers')
		#Add effects
		add_effects(script_json, {
			'CharFadeIn': [0],
			202: [2, 14, 20, 31, 35],
			102: [6, 25, 34],
			'isClearModle': [37],
			103: [3, 37]
			
		})
		
	#詐欺事件の調査（3） 6/6
	elif avgID == '20141':
		#Add airport background + bgm
		insert_schedule(script_json,
			('backgrounds', {'id': 8, 'start': 1, 'end': None}),
			('bgm', {'id': 140, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [4, 2],
			'right': [1]
		}, mode='speakers')
		
	#未認可店舗の調査協力 9/10
	elif avgID == '22115':
		#Add administrative district background
		insert_schedule(script_json,
			('backgrounds', {'id': 18, 'start': 1, 'end': None}),
			('bgm', {'id': 101, 'start': 1, 'end': None})
		)		
		#Add charpos
		add_charpos(script_json, {
			'right': [1]
		}, mode='speakers')
		
	#協会からの挑戦状
	#1/2 (+ Choice #1, Choice #2)
	elif avgID in ['22021', '22022', '22023']:
		#Add guild background to all of these
		insert_schedule(script_json,
			('backgrounds', {'id': 23, 'start': 1, 'end': None}),
		)
		#Add charpos to all of these
		add_charpos(script_json, {
			'left': [56, 57, 59],
			'right': [1, 2]
		}, mode='speakers')
		#Add animation to 1/2
		if avgID == '22021':
			add_effects(script_json, {
			203: [0]
		})
	#2/2
	elif avgID == '12024':
		#Add the eastern district background to the first frame:
		insert_schedule(script_json,
			('backgrounds', {'id': 13, 'start': 1, 'end': 1}),
		)
		
	#カプア特急便のお礼
	#1/3
	elif avgID == '12025':
		#Change background to use the crossbell station background instead of airport
		script_json['backgrounds'][0]['id'] = 16
		
	#Extra/Unknown
	#受付嬢トリア
	elif avgID == '20023':
		#Add harbor district background
		insert_schedule(script_json,
			('backgrounds', {'id': 19, 'start': 1, 'end': None}),
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [536],
			'right': [535]
		}, mode='speakers')
	#スラッシュ
	elif avgID == '20024':
		#Add downtown background
		insert_schedule(script_json,
			('backgrounds', {'id': 20, 'start': 1, 'end': None}),
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [538],
			'right': [232]
		}, mode='speakers')
	#キャンベル議員
	elif avgID == '20026':
		#Add residential district background
		insert_schedule(script_json,
			('backgrounds', {'id': 22, 'start': 1, 'end': None}),
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [542, 1],
			'right': [541, 2]
		}, mode='speakers')
	#フェルナンド
	elif avgID == '20028':
		#Add Genten background
		insert_schedule(script_json,
			('backgrounds', {'id': 6, 'start': 1, 'end': None}),
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [208, 207, 203],
			'right': [2, 1]
		}, mode='speakers')
		#Add effect
		add_effects(script_json, {
			'CharFadeIn': [0]
		})

################################################################################
#Chapter 1

	#女王生誕祭の支援（1）
	#6/6
	elif avgID == '20033':
		#Add guild background
		insert_schedule(script_json,
			('backgrounds', {'id': 23, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [11, 12, 22, 23,  25, 26, 28, 30],
			'right': [10, 13, 20, 21, 24, 27, 29, 31]
		}, mode='frames')
		#Add effect
		add_effects(script_json, {
			202: [25, 26]
		})

	#キルシェ通り・街道灯の交換
	#2/7
	elif avgID == '22124':
		#Add outdoor background, and bgm
		insert_schedule(script_json,
			('backgrounds', {'id': 36, 'start': 1, 'end': None}),
			('bgm', {'id': 134, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [2],
			'right': [1]
		}, mode='speakers')
	#3/7
	elif avgID == '22128':
		#Add bgm
		insert_schedule(script_json,
			('bgm', {'id': 134, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [2, 3],
			'right': [1]
		}, mode='speakers')
		#Add effects
		add_effects(script_json, {
			202: [7]
		})
	#4/7
	elif avgID == '22130':
		#Add the "danger" music
		insert_schedule(script_json,
			('bgm', {'id': 122, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [1, 2],
			'right': [3]
		}, mode='speakers')
		#Add effects
		add_effects(script_json, {
			202: [0],
			102: [2]
		})
	#5/7, 6/7
	elif avgID in ['22131', '22132']:
		#Add outdoor background, and bgm
		insert_schedule(script_json,
			('backgrounds', {'id': 36, 'start': 1, 'end': None}),
			('bgm', {'id': 134, 'start': 1, 'end': None})
		)
		#5/7
		if avgID == '22131':
			#Add charpos
			add_charpos(script_json, {
				'left': [1],
				'right': [2, 3]
			}, mode='speakers')
			#Add effect
			add_effects(script_json, {
				102: [0]
			})
		#6/7
		elif avgID == '22132':
			#Add charpos
			add_charpos(script_json, {
				'left': [1],
				'right': [2]
			}, mode='speakers')
			#Add effect
			add_effects(script_json, {
				102: [0]
			})

	#女王生誕祭の支援（3）
	#never found a suitable background to use for Grancel Sewers
	#20040, 20041, 20042, 20043, 20044
	
	#指名手配犯の捜索
	#never found a suitable background to use for Grancel Sewers
	#12188, 12189, 12191 (partial)
	
	#爆弾の捜索（1） 
	#2/13
	elif avgID == '20051':
		#A fade will be shown here to show that the location has changed
		#Change the portrait to show here to match 11/13
		script_json['dialogueFrames'][2]['character']['charID'] = 1
		script_json['dialogueFrames'][2]['expression'] = 4
		#Add charpos
		add_charpos(script_json, {
			'left': [3, 5, 10, 12],
			'right': [0, 1, 2, 4, 6, 7, 11, 13 ]
		}, mode='frames')
		#Add effect
		add_effects(script_json, {
			202: [6],
			102: [3, 5],
			103: [4],
			'isClearModle': [2],
			'CharFadeIn': [10]
		})
	#4/13
	elif avgID == '20047':
		#Add charpos
		add_charpos(script_json, {
			'left': [2],
			'right': [1]
		}, mode='speakers')
	#6/13
	elif avgID == '20048':
		#Add charpos
		add_charpos(script_json, {
			'left': [1, 4],
			'right': [595]
		}, mode='speakers')
	#7/13
	elif avgID == '20049':
		#Add charpos
		add_charpos(script_json, {
			'left': [2, 597, 598],
			'right': [1, 596]
		}, mode='speakers')
	#8/13
	elif avgID == '20050':
		#This scene takes place at the harbor, so change it to use the harbor background
		script_json['backgrounds'][0]['id'] = 28
		#Add charpos
		add_charpos(script_json, {
			'left': [1, 2, 7],
			'right': [0, 3, 4, 5, 6, 8, 9]
		}, mode='frames')
	#9/13
	elif avgID == '20052':
		#Add a Grancel street background to match the surrounding scenes
		insert_schedule(script_json,
			('backgrounds', {'id': 27, 'start': 1, 'end': None})
		)
	#10/13
	elif avgID == '20053':
		#A fade will be shown here to show that the location has changed
		#Change the portrait to show here to match 11/13
		script_json['dialogueFrames'][5]['character']['charID'] = 1
		script_json['dialogueFrames'][5]['expression'] = 4
		
		#Add charpos
		add_charpos(script_json, {
			'left': [2, 3, 6, 8, 10, 11, 13, 15, 17, 18, 19, 21],
			'right': [0, 4, 5, 7, 9, 12, 14, 16, 20]
		}, mode='frames')
		#Add effect
		add_effects(script_json, {
			'isClearModle': [5],
			102: [14],
			'CharFadeIn': [6, 8, 9]
		})
	#12/13
	elif avgID == '20055':
		#Add charpos
		add_charpos(script_json, {
			'left': [2, 4],
			'right': [1, 3]
		}, mode='speakers')
		#Add effects
		add_effects(script_json, {
			202: [3, 5],
			102: [12],
			103: [4]
		})

	#リッター街道・安全性調査
	#2/4, 3/4, 4/4
	elif avgID in ['22142', '22143', '22144']:
		#Add roadway background to all
		insert_schedule(script_json,
			('backgrounds', {'id': 10, 'start': 1, 'end': None}),
		)
		#2/4
		if avgID == '22142':
			#Add missing music that would have played during the dungeon
			insert_schedule(script_json,
				('bgm', {'id': 134, 'start': 1, 'end': 4})
		)
		
	#爆弾の捜索（2）
	#1/6
	elif avgID == '20056':
		#Add grancel street background
		insert_schedule(script_json,
			('backgrounds', {'id': 27, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [1, 3, 4, 5],
			'right': [0, 2, 6, 7]
		}, mode='frames')
		#Add effects
		add_effects(script_json, {
			202: [5]
		})
	#2/6
	elif avgID == '20057':
		#Add grancel street background
		insert_schedule(script_json,
			('backgrounds', {'id': 27, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [497],
			'right': [1]
		}, mode='speakers')
		#Add effects
		add_effects(script_json, {
			102: [4]
		})
	#3/6
	elif avgID == '20058':
		#Add ainsel background
		insert_schedule(script_json,
			('backgrounds', {'id': 1, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [497],
			'right': [1]
		}, mode='speakers')
		#Add effects
		add_effects(script_json, {
			102: [2]
		})
	#4/6
	elif avgID == '20059':
		#Add harbor background
		insert_schedule(script_json,
			('backgrounds', {'id': 28, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [2, 497],
			'right': [1, 3]
		}, mode='speakers')
		#Add effects
		add_effects(script_json, {
			102: [5]
		})
	#5/6
	elif avgID == '20060':
		#Add grancel street background
		insert_schedule(script_json,
			('backgrounds', {'id': 27, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [497],
			'right': [1]
		}, mode='speakers')
		#Add effects
		add_effects(script_json, {
			102: [5]
		})
		
	#爆弾の捜索（3）
	#7/9
	elif avgID == '20066':
		#Add grancel street background
		insert_schedule(script_json,
			('backgrounds', {'id': 27, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [1, 2],
			'right': [3, 4]
		}, mode='speakers')
		#Add effects
		add_effects(script_json, {
			'CharFadeOut': [11, 12]
		})

################################################################################
#Chapter 2

	#異常事故の総合的調査(1)
	#2/16~SP
	elif avgID == '20139':
		#Add crossbell plaza background
		insert_schedule(script_json,
			('backgrounds', {'id': 14, 'start': 1, 'end': None})
		)
		
	#古戦場の調査協力
	#2/3, 3/3
	elif avgID in ['22205', '22206']:
		#Add outdoor background to both
		insert_schedule(script_json,
			('backgrounds', {'id': 36, 'start': 1, 'end': None})
		)
	
		if avgID == '22206':
			#Add bgm to 3/3
			insert_schedule(script_json,
				('bgm', {'id': 120, 'start': 1, 'end': None})
			)
		
	#異常事故の総合的調査(2) 
	#4/15, 5/15, 6/15, 7/15
	elif avgID in ['20081', '10201', '10202', '10203']:
		#Add geofront background to all
		insert_schedule(script_json,
			('backgrounds', {'id': 71, 'start': 1, 'end': None})
		)
	
		if avgID == '20081':
			#Add bgm to 4/15
			insert_schedule(script_json,
				('bgm', {'id': 19, 'start': 1, 'end': None})
			)
			#Fix 4/15 charpos
			add_charpos(script_json, {
				'left': [3, 5, 7, 9],
				'right': [1, 2, 4, 6, 8]
			}, mode='frames')
			#Add effects to 4/15
			add_effects(script_json, {
				102: [8],
				'CharFadeIn': [1, 3]
			})
	#9/15~SP3
	elif avgID == '20087':
		#Add crossbell plaza background
		insert_schedule(script_json,
			('backgrounds', {'id': 14, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [1],
			'right': [0]
		}, mode='frames')
	#9/15~SP4
	elif avgID == '20088':
		#Add harbor district background
		insert_schedule(script_json,
			('backgrounds', {'id': 19, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [652],
			'right': [1]
		}, mode='speakers')
	#14/15
	elif avgID == '20096':
		#Add crossbell plaza background
		insert_schedule(script_json,
			('backgrounds', {'id': 14, 'start': 1, 'end': None})
		)
	
	#ツァイス支部の応援要請(2)
	#1/3
	elif avgID == '20097':
		#Add ainsel background
		insert_schedule(script_json,
			('backgrounds', {'id': 1, 'start': 1, 'end': None})
		)
	#2/3~SP1
	elif avgID == '20098':
		#Change background to the zeiss street one
		insert_schedule(script_json,
			('backgrounds', {'id': 37, 'start': 1, 'end': None})
		)
	
	#エルモ温泉の魔獣退治
	#2/3 (x2)
	elif avgID in ['22209', '22210']:
		#Add outdoor background and bgm
		insert_schedule(script_json,
			('backgrounds', {'id': 36, 'start': 1, 'end': None}),
			('bgm', {'id': 164, 'start': 1, 'end': None})
		)
	#3/3 (x2)
	elif avgID in ['22211', '22212']:
		#Add indoor background and bgm
		insert_schedule(script_json,
			('backgrounds', {'id': 39, 'start': 1, 'end': None}),
			('bgm', {'id': 112, 'start': 1, 'end': None})
		)
	
	#エルモ温泉の魔獣退治(2)
	#2/2
	elif avgID == '12223':
		#Change the first part to use outdoor background and bgm
		insert_schedule(script_json,
			('backgrounds', {'id': 36, 'start': 1, 'end': 5}),
			('bgm', {'id': 164, 'start': 1, 'end': 5})
		)
	#unused 2/2's
	elif avgID in ['20108', '20109']:
		#Change Mrs. Mao's lines to show her portrait
		script_json['dialogueFrames'][0]['character']['charID'] = 700
		script_json['dialogueFrames'][0]['expression'] = 5
		script_json['dialogueFrames'][16]['character']['charID'] = 700
		script_json['dialogueFrames'][16]['expression'] = 1
		#Add indoor background and bgm
		insert_schedule(script_json,
			('backgrounds', {'id': 39, 'start': 1, 'end': None}),
			('bgm', {'id': 112, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [0, 2, 3, 5, 7, 8, 10, 12, 15, 17],
			'right': [1, 4, 6,  9, 11, 13, 14, 16, 18]
		}, mode='frames')
		#Add effects
		add_effects(script_json, {
			202: [7, 15],
			102: [1, 13, 14]
		})

	#中央工房の盗難事件(2)
	#3/7 (x2)
	elif avgID in ['10086', '10087']:
		#Add army room background and bgm
		insert_schedule(script_json,
			('backgrounds', {'id': 41, 'start': 1, 'end': None}),
			('bgm', {'id': 107, 'start': 1, 'end': None})
		)
	#5/7~SP1 (Tita conversation)
	elif avgID == '20115':
		#Add indoor (russel lab) background and bgm
		insert_schedule(script_json,
			('backgrounds', {'id': 38, 'start': 1, 'end': None}),
			('bgm', {'id': 108, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [0, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 25],
			'right': [1, 2, 3, 5, 6, 19, 21, 22, 23, 24]
		}, mode='frames')
		#Add effects
		add_effects(script_json, {
			202: [3, 7, 12, 16],
			102: [1],
			203: [11],
			'CharFadeOut': [18]
		})
	#5/7~SP2 (Prometheus conversation)
	elif avgID == '20116':
		#Add office room background and bgm
		insert_schedule(script_json,
			('backgrounds', {'id': 38, 'start': 1, 'end': None}),
			('bgm', {'id': 108, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [696, 697],
			'right': [1, 2, 46]
		}, mode='speakers')
	#5/7~SP3 (Murdock conversation)
	elif avgID == '20118':
		#Add zeiss factory background and bgm
		insert_schedule(script_json,
			('backgrounds', {'id': 35, 'start': 1, 'end': None}),
			('bgm', {'id': 108, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [691],
			'right': [1]
		}, mode='speakers')
		#Change Murdock's lines to show his portrait
		for frame_index in [0, 2, 6, 8, 10]:
			script_json['dialogueFrames'][frame_index]['character']['charID'] = 691
		#Add expressions
		script_json['dialogueFrames'][0]['expression'] = 2
		script_json['dialogueFrames'][2]['expression'] = 1
		script_json['dialogueFrames'][6]['expression'] = 1
		script_json['dialogueFrames'][8]['expression'] = 2
		script_json['dialogueFrames'][10]['expression'] = 1
	#5/7~SP4 (Wong/Gundolf conversation)
	elif avgID == '20119':
		#Add guild background, and zeiss bgm
		insert_schedule(script_json,
			('backgrounds', {'id': 23, 'start': 1, 'end': None}),
			('bgm', {'id': 108, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [2, 6, 7, 8, 11, 15, 20, 23],
			'right': [0, 1, 3, 4, 5, 9, 10, 12, 13, 14, 16, 17, 18, 19, 21, 22, 24]
		}, mode='frames')
		#Add effects
		add_effects(script_json, {
			'CharFadeIn': [0]
		})
	#7/7~SP (Jillian/Ronaldo conversation)
	elif avgID == '20120':
		#Add crossbell police department office background bgm
		insert_schedule(script_json,
		('backgrounds', {'id': 47, 'start': 1, 'end': None}),
		('bgm', {'id': 102, 'start': 1, 'end': None})
		)
		#Add charpos
		add_charpos(script_json, {
			'left': [1, 5],
			'right': [2, 3, 4]
		}, mode='speakers')
		#Add effects
		add_effects(script_json, {
			102: [5],
			'isClearModle': [27]
		})
		
	#導力停止の異常事故(2)
	#6/14 (Choice #1, Choice #2)
	elif avgID in ['20127', '20128', '20129']:
		
		#Choice #1's last line should be at the end of Choice #2 instead
		if avgID == '20128':
			delete_frame(script_json, 2)
		elif avgID == '20129':
			insert_frame(script_json, 1,
			    {
				  "template": 1,
				  "character": {
					"charID": 51,
					"speaker": 51,
					"displayName": 1,
					"mirror": 0
				  },
				  "expression": 1,
				  "charPos": 2,
				  "strID": 1006632,
				  "isApha": 0,
				  "nameSize": 18,
				  "contentSize": 16,
				  "isClearModle": 0,
				  "CharFadeIn": 0,
				  "CharFadeOut": 0,
				  "voice": {
					"id": 0,
					"first": 0
				  },
				  "sfx": {
					"id": 0,
					"first": 0
				  },
				  "effect": 0,
				  "itemID": 0,
				  "itemIconID": 0,
				  "avgImageID": 0
				}
			)
		#Add harbor district background, and bgm to all
		insert_schedule(script_json,
			('backgrounds', {'id': 19, 'start': 1, 'end': None}),
			('bgm', {'id': 10, 'start': 1, 'end': None})
		)
		#Add charpos to all
		add_charpos(script_json, {
			'left': [2, 51],
			'right': [1]
		}, mode='speakers')
		
	#7/14, 9/14, 10/14, 10/14~SP1, 10/14~SP2, 10/14~SP3
	elif avgID in ['20130', '20131', '20132', '20133', '20134', '20135']:
		#Add geofront bgm to all of these
		insert_schedule(script_json,
			('bgm', {'id': 19, 'start': 1, 'end': None})
		)
	
		if avgID in ['20132', '20133', '20134', '20135']:
			#Add geofront background to 10/14, 10/14~SP1, 10/14~SP2, 10/14~SP3
			insert_schedule(script_json,
				('backgrounds', {'id': 71, 'start': 1, 'end': None})
			)

###########################################################################
	return script_json
