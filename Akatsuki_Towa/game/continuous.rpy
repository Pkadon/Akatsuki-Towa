default persistent.continuous = False
default clicked_quest_index = None

init python:

    def get_with_menu_index(indexes, return_type='scene'):
        if len(indexes) == 1:
            chapter_index = indexes
        if len(indexes) == 2:
            chapter_index, quest_index = indexes
        elif len(indexes) == 3:
            chapter_index, quest_index, scene_index = indexes

        if return_type == 'scene':
            return unlocked_menudata[chapter_index]['quests'][quest_index]['scenes'][scene_index]
        elif return_type == 'scenes':
            return unlocked_menudata[chapter_index]['quests'][quest_index]['scenes']
        elif return_type == 'quest':
            return unlocked_menudata[chapter_index]['quests'][quest_index]
        elif return_type == 'quests':
            return unlocked_menudata[chapter_index]['quests']
        elif return_type == 'chapter':
            return unlocked_menudata['chapter_index']

    def get_with_flow_index(indexes, return_type='group'):
        category_index, chapter_index, group_index, quest_index, step_index = indexes

        if return_type == 'category':
            return flow[category_index]
        if return_type == 'chapter':
            return flow[category_index]['chapters'][chapter_index]
        if return_type == 'group':
            return flow[category_index]['chapters'][chapter_index]['groups'][group_index]
        if return_type == 'quest':
            return flow[category_index]['chapters'][chapter_index]['groups'][group_index]['quests'][quest_index]
        if return_type == 'step':
            return flow[category_index]['chapters'][chapter_index]['groups'][group_index]['quests'][quest_index]['steps'][scene_index]

    def increment_flow(indexes):
        category_index, chapter_index, group_index, quest_index, step_index = indexes
        quest_index = 0
        step_index = 0

        current_chapter = get_with_flow_index(indexes, 'chapter')
        group_index += 1
        if group_index < len(current_chapter['groups']):
            return (category_index, chapter_index, group_index, quest_index, step_index)

        else:
            current_category = get_with_flow_index(indexes, 'category')
            chapter_index += 1
            group_index = 0
            quest_index = 0
            step_index = 0

            if chapter_index < len(current_category['chapters']):
                return (category_index, chapter_index, group_index, quest_index, step_index)

            else:
                return None





#clean slide from top-left corner
transform mission_select_transition_1():
    on show:
        anchor (0.5,0.5)
        pos (-0.5, -0.5)
        rotate -90

        ease .45:
            rotate 0
            pos (0.5, 0.5)
            zoom 1.0

#clean slide from top-right corner
transform mission_select_transition_2():
    anchor (0.5,0.5)
    pos (1.5, -0.5)
    rotate 90

    ease .45:
        rotate 0
        pos (0.5, 0.5)
        zoom 1.0

#clean slide from bottom-left corner
transform mission_select_transition_3():
    anchor (0.5,0.5)
    pos (-0.5, 1.5)
    rotate 90

    ease .45:
        rotate 0
        pos (0.5, 0.5)
        zoom 1.0

#clean slide from bottom-right corner
transform mission_select_transition_4():
    anchor (0.5,0.5)
    pos (1.5, 1.5)
    rotate -90

    ease .45:
        rotate 0
        pos (0.5, 0.5)
        zoom 1.0


#slide from bottom-right corner
transform mission_select_transition_5():
    anchor (0.5,0.5)
    pos (1.5, 1.0)
    rotate 90
    zoom 1.2

    ease .35:
        rotate -15
        pos (0.5, 0.5)
        zoom .9
    pause .15
    linear .2:
        rotate 0
        pos (0.5,0.5)
        zoom 1.0 


#drops in from middle of screen
transform mission_select_transition_6():
    anchor (0.5,0.5)
    pos (0.5, 0.5)
    zoom 1.5
    alpha .85

    linear .1:
        zoom .9
        rotate -7
        alpha 1.0
        pos (0.5,0.5)
    pause .3
    ease .1:
        rotate 0
        zoom 1.0
        pos (0.5,0.5)


#"page-turn" from right side of screen
transform mission_select_transition_7():
    anchor (0.0,0.5)
    pos (1.5, 0.5)
    xzoom 0.0

    ease .25:
        xzoom 1.0
        pos (0.0, 0.5)

#"page-turn" from left side of screen
transform mission_select_transition_8():
    anchor (1.0,0.5)
    pos (-0.5, 0.5)
    xzoom 0

    ease .25:
        xzoom 1.0
        pos (1.0, 0.5)
    ease .1:
        align (0.5,0.5)

#slide in from bottom of screen
transform mission_select_transition_9():
    anchor (0.5,0.5)
    pos (0.5, 1.7)
    zoom 0.8

    ease .35:
        zoom 1.0
        pos (0.5, 0.5)

define mission_select_transitions = [
    mission_select_transition_1,
    mission_select_transition_2,
    mission_select_transition_3,
    mission_select_transition_4,
    mission_select_transition_5,
    mission_select_transition_6,
    mission_select_transition_7,
    mission_select_transition_8,
    mission_select_transition_9
]


transform next_ani():
    xoffset 0
    linear 0.5:
        xoffset 5
    linear 0.5:
        xoffset 0
    repeat

define start_marker = "START ▶    "
define start_marker_width = calculate_text_size(start_marker)[0]

define next_marker = "NEXT ▶    "
define next_marker_width = calculate_text_size(next_marker)[0]

define enter_marker = "ENTER ▶    "
define enter_marker_width = calculate_text_size(enter_marker)[0]

style mission_select_text:
    size mission_select_text_size
style mission_select_text:
    variant "touch"
    size touch_mission_select_text_size

default persistent.animate_mission_select = True

default mission_select_transition = mission_select_transition_1
screen mission_select(missions):
    tag mission_select
    modal True

    use toggle_language()

    on "show" action [Function(mute_typewriter), Play("sound", "other_7004.ogg")]

    python: 
        buttonlist = []
        buttonlist.append({'text': "Replay", 'properties': {'activate_sound': 'other_7004.ogg', 'action': [ShowMenu("episodelist", unlocked_menudata)]}})
        buttonlist.append({'text': "History", 'properties': {'action': ShowMenu('history')}})
        buttonlist.append({'text': "Save", 'properties': {'action': ShowMenu('save')}})
        buttonlist.append({'text': "Load", 'properties': {'action': ShowMenu('load')}})

    frame at mission_select_transition:
        padding (0,0)
        background None
        use book_background()

        use sidearea(buttonlist)

        use book_paper:
            vbox:
                align (0.5,0.5)
                spacing 10

                $ mission_count = 0
                for mission in missions:
                    python:
                        mission_count += 1
                        parent_quest = mission['parent_quest']
                        clickable_nodes = [node for node in mission['nodes'] if not node.get('locked', {}).get('hide')]
                    vbox:
                        vbox:
                            hbox:
                                spacing 5
                                xalign 0.5

                                python:
                                    title_strid = parent_quest['questname']
                                    mission_title = convertstrid(title_strid)
                                    mission_title_size, mission_title_anchors = size_text(mission_title, size=style.mission_select_text.size, max_dimensions=paper_inner_space, anchors=(0, tabfont_center), tag=False, tag_dict={})

                                text mission_title:
                                    style "mission_select_text"
                                    size mission_title_size
                                    yanchor mission_title_anchors[1]
                                    ypos 0.5
                                    if len(clickable_nodes) == 0:
                                        color "#777"
                                    else:
                                        color "#000"

                                $ questID = parent_quest.get('questID')
                                if questID != None and str(questID) in questlog_data:
                                    button:
                                        xysize (23,24)
                                        background "plus"
                                        hover_background "plus_hovered"
                                        hover_sound "common_tag.ogg"
                                        yalign 0.5
                                        activate_sound 'other_7004.ogg'
                                        action ShowMenu('questlog', parent_quest['questID'], step_limit=parent_quest['step_limit'], solid_background=True, yinitial=1.0, return_on_close=True)

                            if mission.get('complete'):
                                hbox:
                                    spacing 5
                                    text "COMPLETE":
                                        style "mission_select_text"
                                        color "#777"
                                    add "checkmark":
                                        yoffset 2

                        if not mission.get('complete'):
                            vbox:
                                spacing 5
                                for node in clickable_nodes:
                                    python:
                                        if not parent_quest.get('started'):
                                            marker = start_marker
                                            info_fit_width = ((paper_inner_space[0] - start_marker_width), paper_inner_space[1])

                                        elif 'in_dungeon' in mission and (dungeon == None):
                                            marker = enter_marker
                                            info_fit_width = ((paper_inner_space[0] - enter_marker_width), paper_inner_space[1])

                                        else:
                                            marker = next_marker
                                            info_fit_width = ((paper_inner_space[0] - next_marker_width), paper_inner_space[1])


                                        if node.get('info'):
                                            info = True
                                            mission_info = convertstrid(node['info'])
                                            mission_info_size, mission_info_anchors = size_text(mission_info, size=style.mission_select_text.size, max_dimensions=info_fit_width, anchors=(0, tabfont_center), tag=False, tag_dict={})
                                        else:
                                            info = False
                                    button:
                                        hover_background Solid('#E6D7D2')
                                        hbox:
                                            text marker:
                                                style "mission_select_text"
                                                at next_ani
                                                color "#000"

                                            if info:
                                                text mission_info:
                                                    style "mission_select_text"
                                                    color "#000"
                                        action [SetVariable('selected_node', node), Return()]

                        if mission_count != len(missions):
                             add "underline":
                                 xsize 400

default flow = dict()
default flow_pos = None
default cleared_label_list = []
default cleared_quest_list = []
default unlocked_menudata = dict()
default selected_node = None
default dungeon = None

init python:
    def unlock_previous_scenes_replay(menu_index):
        global unlocked_menudata

        chapter_index, quest_index = menu_index[:2]

        for chapter in unlocked_menudata[:chapter_index]:
            chapter['unlocked'] = True
            for quest in chapter['quests']:
                quest['unlocked'] = True

        current_chapter = unlocked_menudata[chapter_index]
        current_chapter['unlocked'] = True
        for quest in current_chapter['quests'][:quest_index]:
            quest['unlocked'] = True

    def evaluate_locked(dic):
        global cleared_label_list
        global cleared_quest_list
        global flags

        locked = False
        if dic.get('locked'):
            locked = len(dic['locked']['flags'])
            for condition in dic['locked']['flags']:
                flag = condition['flag']
                value = condition['value']

                if flag == 'quest cleared':
                    questID = value
                    if questID in cleared_quest_list:
                        locked -= 1
                    continue
                elif flag == 'label viewed':
                    label = value
                    if label in cleared_label_list:
                        locked -= 1
                    continue
                else:
                    if flags[flag] == value:
                        locked -= 1
                    continue

            if locked:
                if dic['locked'].get('skip'):
                    dic['cleared'] = True
                if 'hide' not in dic['locked']:
                    dic['locked']['hide'] = True
            else:
                del dic['locked']
        return locked

# START
#####################################
label start():
python:
    import copy

    unlocked_menudata = copy.deepcopy(menudata)
    flow = copy.deepcopy(flowchart)
    cleared_label_list = []
    cleared_quest_list = []
    dungeon = None

    menu_pos, flow_pos = clicked_quest_index

    current_group = get_with_flow_index(flow_pos, 'group')
    selected_quest_index = flow_pos[3]
    for quest in current_group['quests'][:selected_quest_index]:
        quest['cleared'] = True

        questID = quest.get('questID')
        if questID not in cleared_quest_list:
            cleared_quest_list.append(questID)

    unlock_previous_scenes_replay(menu_pos)

    selected_quest = get_with_flow_index(flow_pos, 'quest')

    selected_step = selected_quest['steps'][0]
    selected_step['parent_quest'] = selected_quest

    selected_node = selected_step['nodes'][0]
    selected_node['parent_step'] = selected_step

# Start loop
###################################
while True:

    python:
        selected_step = selected_node['parent_step']
        selected_quest = selected_step['parent_quest']
        if selected_step.get('in_dungeon'):
            dungeon = selected_step['parent_quest']

    # Intro labels *should* only be used for the Chapter bumper banners, or other overlay/popups.
    # They will be played -before- hiding the book menu, so that they appear over top of it.
    $ intro = selected_step.get('intro')
    if intro and not intro.get('cleared'):
        call play_through_label_list(intro, selected_quest)

    hide screen mission_select

    call play_through_label_list(selected_node, selected_quest)

    $ ending = selected_step.get('ending')
    if ending and selected_step['nodes'] == [selected_node]:
        call play_through_label_list(ending, selected_quest)

    python:
        selected_step['parent_quest']['started'] = True

        # Exit the dungeon by setting "dungeon" to None
        # If the parent step is marked "exit_dungeon" AND this is the final node of the step.
        if 'exit_dungeon' in selected_step and len(selected_step['nodes']) == 1:
            dungeon = None
    

    window hide

    label create_mission_list:
    python:
        current_group = get_with_flow_index(flow_pos, 'group')

        missions = []
        active_missions = 0

        # If a dungeon has been entered, only show the nodes for the current quest until the dungeon has been exited
        if dungeon:
            quests = [dungeon]
        else:
            quests = current_group['quests']

        for quest in quests:
            if evaluate_locked(quest):
                continue

            quest_menu_data = get_with_menu_index(quest['menu_index'], 'quest')
            if 'questname' not in quest:
                quest['questname'] = quest_menu_data['questname']

            if 'step_limit' not in quest:
                quest['step_limit'] = 0

            mission = False

            if quest.get('cleared'):
                pass
            else:
                for step in quest['steps']:
                    step['parent_quest'] = quest

                    if step.get('cleared'): continue

                    else:
                        # If step is locked, and it has been marked skippable,
                        # (if the conditions to unlock it are now impossible to meet)
                        # it will be marked cleared and skipped over in the next loop
                        if evaluate_locked(step):
                            continue

                        for node in step['nodes']:
                            node['parent_step'] = step

                            if node.get('cleared'):
                                continue
                            elif evaluate_locked(node):
                                continue

                            else:
                                mission = True
                                active_missions += 1

                            # Change the first label's transition to fade_in if it was previously set to use the full fade
                            if node['labels'][0].get('trans') == 'fade':
                                node['labels'][0]['fade'] = 'fade_in'

                            if 'info' not in node:
                                first_label = node['labels'][0]['label']

                                scene_menu_index = scene_map[first_label]
                                scene_menu_data = get_with_menu_index(scene_menu_index, 'scene')
                                menu_info = scene_menu_data.get('sceneinfo')
                                if menu_info != None:
                                    node['info'] = menu_info  

                        # Clear out nodes that were marked "cleared", either during the last loop, or by evaluate_locked
                        step['nodes'] = [node for node in step['nodes'] if not node.get('cleared')]

                        # If no nodes remain, then we're done with this step, move on to the next one in the list
                        if len(step['nodes']) == 0:
                            step['cleared'] = True
                            continue

                        if mission:
                            # If we're still in the middle of progressing through this quest, 
                            # then it should not appear in the replay menu yet
                            quest_menu_data['unlocked'] = False

                            if 'log_steps' in step:
                                if quest['step_limit'] < step['log_steps']:
                                    quest['step_limit'] = step['log_steps']

                            missions.append(step)
                            break

            if not mission:
                # Exit dungeon "tunnel-vision" mode and make any other quests in the current group visible again
                dungeon = None
                # Mark quest dictionary as cleared in the internal flowchart flowchart
                quest['cleared'] = True

                mission_dict = {
                    'parent_quest': quest,
                    'nodes': []
                }

                # Unlocks the completed questlog by default
                # If "end_log_steps" is present with an int, then the final questlog will only show up to that many steps
                # Otherwise it should default to None and show the whole thing.
                # "end_log_steps" is currently only used with the first half of the 機密医療データの配達 quest
                quest['step_limit'] = quest.get('end_log_steps')

                # "incomplete" is also currently only used with the first half of the 機密医療データの配達 quest
                if not quest.get('incomplete'): 
                    # Show a "quest complete" indicator on mission select screen
                    mission_dict['complete'] = True

                    # Store quest cleared flag
                    if quest.get('questID') not in cleared_quest_list:
                        cleared_quest_list.append(quest['questID'])

                        # Jump back to the start to reassess unlock conditions
                        renpy.jump('create_mission_list')

                    # Unlock scene Replay
                    quest_menu_data['unlocked'] = True

                missions.append(mission_dict)

        if active_missions == 0:
            flow_pos = increment_flow(flow_pos)

            if flow_pos == None:
                renpy.jump('end_continuous')
            else:
                renpy.jump('create_mission_list')

    window hide
    python:
        quick_menu = False

        if persistent.animate_mission_select == False or renpy.is_skipping():
            mission_select_transition = None
        else:
            mission_select_transition = (renpy.random.choice(mission_select_transitions))

        renpy.stop_skipping()
    show screen mission_select(missions)
    pause
    $quick_menu = True

label end_continuous:
return

label play_through_label_list(node_dict, parent_quest):
$ labels = node_dict['labels']
$ index = 0
while index < len(labels):
    python:
        label_dict = labels[index]

        label = label_dict['label']

        pass_transition = False
        if 'trans' in label_dict:
            pass_transition = True
            transition_string = label_dict['trans']
            transition = globals().get(transition_string)

    if pass_transition:
        call expression label pass (trans=transition)
    else:
        call expression label

    python:
        # Updade quest log steps after viewing the scene (if applicable)
        if 'log_steps' in label_dict:
            if parent_quest['step_limit'] < label_dict['log_steps']:
                parent_quest['step_limit'] = label_dict['log_steps']

        if _return in set_flags:
            flag = set_flags[_return]['flag']
            value = set_flags[_return]['value']

            flags[flag] = value

        if _return in decline_list:
            dungeon = None
            # Player will be booted back to the mission select screen.
            # Start the next play as close to the confirmation choice as possible
            node_dict['labels'] = node_dict['labels'][index:]
            renpy.jump('create_mission_list')
        else:
            index += 1
        cleared_label_list.append(label)

$ node_dict['cleared'] = True
return