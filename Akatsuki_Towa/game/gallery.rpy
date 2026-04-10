image gallerybackground:
    "optionsmenuscreen"
    matrixcolor HueMatrix(-70) * BrightnessMatrix(0.25)

default gallery_background = "gallerybackground"
default show_buttons = True

default gallery_music = None
default gallery_object_counter = 0
default current_context = None
default current_slider = None

init python:
    import copy

    with renpy.open_file('gallery_data.json') as txt:
        gallery_data = json.load(txt)

    # Refresh each image 30 frames per second (so resizing and rotating looks smooth enough)
    def update_transform(trans, st, at):
        trans.update()
        return 0.033

    def spawn_gallery_object():
        global gallery_object_counter

        gallery_object_counter += 1
        id = str(gallery_object_counter)

        child_transform = Transform(
            child = None, 
            function = update_transform, 
            subpixel = True,
            align = (0.5,0.5) # Align the image to the center of the 5000x5000 box from the Fixed
        )

        #Initialize transform fields to make sure they are not None
        child_transform.zoom = 1.0
        child_transform.xzoom = 1.0
        child_transform.rotate = 0

        # Then the Transform needs to be contained inside of a Fixed 
        # so that it zoom will zoom into the center instead of the top left corner

        # Make the fixed as large as the largest image x3-5.
        # If the zoomed image's dimensions are larger than the Fixed's dimensions, 
        # pixels that go beyond the bounds will not be draggable.
        container = Fixed(child_transform, xysize=(5000,5000))

        new_drag = Drag(
            d = container,
            drag_name = id,
            draggable = True,
            droppable = False,
            drag_offscreen = True,
            drag_raise = False,
            focus_mask = True,
            activated = open_context_menu,
            alternate = toggle_buttons,
            anchor = (0.5,0.5),
            pos = (0.5,0.5)
        )

        #Initialize custom attributes for gallery
        new_drag.mode = 1
        new_drag.info = None
        new_drag.parent = None
        new_drag.index = None
        new_drag.expression = None

        group = renpy.get_displayable('gallery_menu', "drag_group")
        group.add(new_drag)

        renpy.show_screen('gallery_selector', id)

    def get_drag_by_id(id):
        drag = renpy.get_displayable('gallery_menu', "drag_group").get_child_by_name(id)
        return drag

    def duplicate_gallery_object(base_id):
        global gallery_object_counter

        gallery_object_counter += 1
        id = str(gallery_object_counter)

        base = get_drag_by_id(base_id)
        new_drag = copy.deepcopy(base)
        new_drag.drag_name = id

        group = renpy.get_displayable('gallery_menu', "drag_group")
        group.add(new_drag)

        new_drag.snap(new_drag.x+1,new_drag.y+1)

        open_context_menu(id, drag=False)

    def remove_drag(id, if_empty=False):
        global current_context

        # Check the gallery object, and only delete it if it's empty and invisible
        if if_empty: 
            drag = get_drag_by_id(id)
            if drag.child.child.child != None:
                return

        if current_context == id:
            hide_context_menu()

        group = renpy.get_displayable('gallery_menu', "drag_group")
        drag = group.get_child_by_name(id)
        group.remove(drag)

    def flip_drag(id):
        drag = get_drag_by_id(id)
        drag.child.child.xzoom *= -1     
    
    # Called by the gallery selector to change a drag's image
    def set_image(id, category, index):
        drag = get_drag_by_id(id)

        drag.parent = category
        drag.index = index
        drag.mode = 1  # mode 2 images are not selectable from the gallery selector, so always reset mode to 1

        drag.info = category[index]

        drag.child.child.set_child(drag.info['base'])

        # Type 2 is used for portraits specifically that have an expression list to cycle through
        if drag.info['type'] == 2: 
            drag.expression = drag.info['alt'][0]
            change_face(id)

    # Cycles through a file list in gallery_data, continuing until it finds a file that
    # is both present in the game's directory, and is not being filtered out by persistent.spoiler_filter.
    def cycle_file(index, parent, increment):
       index += increment

       # Let the cycle loop around to the other end of the image list
       if index >= len(parent):
           index = 0
       elif index < 0:
           index = (len(parent) - 1)
        
       # Keep moving in the same direction until the selected file is not being blocked by the spoiler filter
       # Looping around to the other end again if necessary
       while parent[index]['file'] in persistent.spoiler_filter or not renpy.loadable(parent[index]['file']):
           index += increment

           if index >= len(parent):
               index = 0
           elif index < 0:
               index = (len(parent) - 1)
       return index

    # This is called by the context menu when it changes or cycles a drag's image.
    # drag.index and/or drag.mode have already been cycled (or set) by a button or function at this point,
    # this is just updating the image now.
    def change_image(id, increment=0):
        drag = get_drag_by_id(id)

        drag.index = cycle_file(drag.index, drag.parent, increment)

        drag.info = drag.parent[drag.index]

        if drag.mode == 2 and 'cutin' in drag.info and renpy.loadable(drag.info['cutin']['file']):
            drag.info = drag.info['cutin']

        else:
            drag.mode = 1

        drag.child.child.set_child(drag.info['base'])

        if drag.info['type'] == 2: 
            drag.expression = drag.info['alt'][0]
            change_face(id)

    # drag.expression has already been cycled by a button at this point, this is just updating the image
    def change_face(id):
        drag = get_drag_by_id(id)

        new_img = f"{drag.info['base']} {drag.expression}"

        drag.child.child.set_child(new_img)
    
    def clear_gallery():
        global gallery_object_counter
        gallery_object_counter = 0

        hide_context_menu()

        renpy.free_memory()        

    def open_context_menu(id, drag=True):
        global current_context

        # When this is called by drag's "activated" property, it passes the drag itself,
        # so the id will be derived from the drag's "drag_name" field
        if drag:
            id = id[0].drag_name

        if current_context != id:
            current_context = id
            # The animation won't be played if it isn't hidden first
            renpy.hide_screen('context_menu')
            renpy.show_screen('context_menu', id)
            renpy.restart_interaction()

    def hide_context_menu():
        global current_context

        renpy.hide_screen('context_menu')
        current_context = None

    def toggle_slider(slider_value):
        global current_slider

        renpy.hide_screen('context_slider')
        renpy.restart_interaction()

        # If the current_slider variable is equal to the passed slider_value
        # then the button is being clicked to toggle the slider off and hide it
        # Set current_slider to None so that it will be shown again when next clicked
        if current_slider == slider_value or slider_value == None:
           current_slider = None

        else:
            renpy.show_screen('context_slider', slider_value)
            current_slider = slider_value

    def hide_slider():
        global current_slider

        renpy.hide_screen('context_slider')
        current_slider = None

    def set_background(img):
        global gallery_background
        gallery_background = img

    # Moves a drag up or down one place in the drag_group's zorder stack.
    # This used undocumented Ren'Py behavior and may stop working.
    # Working as of Ren'Py version 8.5.2
    def change_zorder(id, direction):
        drag_group = renpy.get_displayable('gallery_menu', "drag_group")
        drags = drag_group.get_children()

        if direction == 'up':
            drags.reverse()

        for drag in drags:
            if drag.drag_name == id:
                index = drags.index(drag)
                if index != 0:
                    drags.insert(index-1, drags.pop(index))
                break

        if direction == 'down':
            drag_group.raise_children(drags)
        elif direction == 'up':
            drag_group.lower_children(drags)

    # If a context menu is open, one click will hide it.
    # Each click after that will toggle the visibility of both the "X" and "Add" buttons
    def toggle_buttons():
        global current_context
        global current_slider
        global show_buttons

        if current_slider:
            toggle_slider(None)
        elif current_context:
            hide_context_menu()
        else:
            show_buttons = not show_buttons
            renpy.restart_interaction()

################################################################
transform slider_appear:
    xzoom 0
    linear 0.1 xzoom 1.0
screen context_slider(slider_value):
    modal False
    tag context_slider

    button at slider_appear:
        xalign 0.5
        yanchor 1.0
        ypos 450
        background None
        padding (20, 10, 20, 0)
        action NullAction()

        hbox:
            textbutton 'Reset':
                yoffset -9
                hover_background Solid("#0005")

                text_size 22
                text_color "#FFF"
                text_outlines [ (1, "#262525", 0, 0) ]
                action SetField(
                    slider_value['bar_properties']['object'], 
                    slider_value['bar_properties']['field'], 
                    slider_value['default_value']
                )
            bar value FieldValue(**slider_value['bar_properties']):
                style "slider_slider"
                left_bar Frame("images_free/gui/slider/horizontal_slider_right.png", 3,3)

################################################################
transform context_appear:
    yoffset 50 
    ease 0.25 yoffset 0
screen context_menu(id):
    modal False
    tag context_menu

    on "hide" action Function(hide_slider)

    python:
        drag = get_drag_by_id(id)
        drag_transform = drag.child.child

        zoom_value = {
            'bar_properties': {
                'object': drag_transform,
                'field': 'zoom',
                'min': 0.1,
                'max': 3.0
            },
            'default_value': 1.0
        }

        rotate_value = {
            'bar_properties': {
                'object': drag_transform,
                'field': 'rotate',
                'min': -180,
                'max': 180
            },
            'default_value': 0
        }

        act_scale = Function(toggle_slider, zoom_value)
        act_rotate = Function(toggle_slider, rotate_value)
        act_flip = Function(flip_drag, id)

        act_z_up = Function(change_zorder, id, 'up')
        act_z_down = Function(change_zorder, id, 'down')
        act_z_top = Function(drag.top)
        act_z_bottom = Function(drag.bottom)

        act_change_image_left = Function(change_image, id, increment=-1)
        act_change_image_right = Function(change_image, id, increment=1)
        act_change_image = Function(renpy.show_screen, 'gallery_selector', id)

        if drag.info and drag.info['type'] == 2:
            act_change_face_right = [CycleField(drag, 'expression', drag.info['alt'], loop=True), Function(change_face, id)]
            act_change_face_left = [CycleField(drag, 'expression', drag.info['alt'], reverse=True, loop=True), Function(change_face, id)]

        act_set_background = [Function(set_background, drag.info['base']), Function(remove_drag, id)]
        act_cycle_portrait_cutin = [CycleField(drag, 'mode', [1, 2]), Function(change_image, id)]

        act_copy = Function(duplicate_gallery_object, id)
        act_delete = Function(remove_drag, id)

        act_hide = Function(hide_context_menu) 

    key "K_LEFT" action act_change_image_left
    key "K_RIGHT" action act_change_image_right
    if drag.info and drag.info['type'] == 2:
        key "K_UP" action act_change_face_right
        key "K_DOWN" action act_change_face_left

    key "z" action act_z_top
    key "repeat_z" action act_z_bottom
    
    key "K_SPACE" action act_cycle_portrait_cutin
    key "c" action act_copy
    key "x" action act_delete

    frame at context_appear:
        style_prefix "context"
        hbox:
            spacing 5

            textbutton "Scale":
                selected (current_slider == zoom_value)
                selected_background Solid('#555b')
                hover_background Solid('#333b')
                action act_scale

            textbutton "Rotate":
                selected (current_slider == rotate_value)
                selected_background Solid('#555b')
                hover_background Solid('#333b')
                action act_rotate

            textbutton "Flip":
                selected (drag.child.child.xzoom < 0)
                selected_background Solid('#555b')
                hover_background Solid('#333b')
                action act_flip

            hbox:
                textbutton " ▲ ":
                    hover_background Solid('#333b')
                    action act_z_up  
                textbutton "Z":
                    hover_background None
                    action NullAction()
                textbutton " ▼ ":
                    hover_background Solid('#333b')
                    action act_z_down

            hbox:
                textbutton " ◀ ":
                    hover_background Solid('#333b')
                    action act_change_image_left
                textbutton "Change":
                    hover_background Solid('#333b')
                    action act_change_image
                textbutton " ▶ ":
                    hover_background Solid('#333b')
                    action act_change_image_right

            if drag.info and drag.info['type'] == 3:
                hbox:
                    textbutton "Set Background":
                        hover_background Solid('#333b')
                        action act_set_background
                    null width 33

            else:
                if drag.info and drag.info['type'] == 2:
                    hbox:
                        textbutton " ◀ ":
                            hover_background Solid('#333b')
                            action act_change_face_left
                        textbutton "Face [(drag.info['alt'].index(drag.expression) + 1)]":
                            hover_background None
                            text_align 0.0
                            xsize 74
                            action NullAction()
                        textbutton " ▶ ":
                            hover_background Solid('#333b')
                            action act_change_face_right
                else:
                    null width 142

                if 'cutin' in drag.info and renpy.loadable(drag.info['cutin']['file']):
                    hbox:
                        null width 10
                        textbutton "Cutin":
                            hover_background Solid('#333b')
                            action act_cycle_portrait_cutin
                        null width 10
                elif drag.mode == 2 and renpy.loadable(drag.parent[drag.index]['file']):
                    textbutton "Portrait":
                        hover_background Solid('#333b')
                        action act_cycle_portrait_cutin
                else:
                    null width 79 # reserve the space so that buttons don't shift around

            textbutton "Copy":
                hover_background Solid('#333b')
                action act_copy

            textbutton "Delete":
                hover_background Solid('#333b')
                action act_delete

            textbutton "Hide ▼":
                hover_background Solid('#333b')
                action act_hide


style context_frame:
    background Solid("#000b")
    padding (0,0)
    xfill True
    ysize 36
    align (0.5,1.0)

style context_textbutton:
    background None
style context_button_text:
    color "#fff"
    size 20

################################################################
screen gallery_menu():
    modal True

    on "show":
        if persistent.spoiler_filter_set == False:
            action Function(renpy.show_screen, 'spoiler_checkboxes')

        # The gallery will inherit the music that the main menu was playing
        # (until it's changed by the gallery selector
        action SetVariable('gallery_music', persistent.mainmenu_music)

    on "hide" action Function(clear_gallery)

    key "K_ESCAPE" action Function(renpy.show_screen, 'gallery_help')

    frame:
        padding (0,0)
        xysize (840,480)
        modal True

        background gallery_background

        # Makes the entire background sensitive to clicks
        button:
            xysize(840,480)
            background None
            alternate Function(toggle_buttons)
            action Function(toggle_buttons)

        draggroup id "drag_group":
            xysize (840,480)
            pos (0,0)

        if not renpy.get_screen('gallery_selector'):
            button:
                align (0.01,0.02)
                xysize (25,25)
                if show_buttons:
                    background Frame("images_free/gui/x.png")
                else:
                    hover_background Frame("images_free/gui/x.png")

                activate_sound "common_cancel.ogg"
                action [Hide('gallery_menu'), Return()]

            textbutton "Add":
                align(1.0,0.0)
                background None

                text_color "#FFF"
                text_outlines [ (1, "#262525", 0, 0) ]
                hover_background Solid("#0005")

                if not show_buttons:
                    text_idle_color "#FFF0"
                    text_idle_outlines [ (0, "#0000", 0, 0) ]
                    text_hover_color "#FFF"
                    text_hover_outlines [ (1, "#262525", 0, 0) ]

                action Function(spawn_gallery_object)

    # Could not for the life of me get `key "mousedown_4"` to work here (other keys worked but not mousewheel)
    # This seems to work for detecting mousewheel scrolls for now.
    viewport:
        mousewheel True
        xysize (840,480)
        yadjustment scroll_detection

        frame:
            background None
            ysize 481

init python:
    def scroll_zoom(adjust, val):
        global current_context

        if current_context:
            drag = get_drag_by_id(current_context)
            if drag.child.child:

                if val < 1:
                    change = -0.1
                elif val > 1:
                    change = 0.1

                drag.child.child.zoom += change
    scroll_detection = ui.adjustment(raw_changed=scroll_zoom)

################################################################
init python:
    #This is used to close and reopen the window to "reset" it when the category is changed, to free up RAM.
    def reopen_selector(id):
        renpy.hide_screen('gallery_selector')
        renpy.show_screen('gallery_selector', id)
        renpy.restart_interaction()

    def cycle_sound(dic, index, increment=0):

        index = cycle_file(index, dic['filtered_contents'], increment)

        dic['index'] = index

        f = dic['filtered_contents'][index]['file']
        if persistent.play_on_cycle:
            renpy.music.play(dic['filtered_contents'][index]['file'], channel="sound")
        
default persistent.play_on_cycle = True
default showing_category = 0
screen gallery_selector(id):
    modal True

    key "K_ESCAPE" action [Hide('gallery_selector'), Function(remove_drag, id, if_empty=True)]

    style_prefix "selector"
    frame:
        xysize (840,480)
        background Frame("dialoguewindow", 25,25)

        vbox:
            hbox:
                xfill True

                textbutton " ◀ ":
                    action [Hide('gallery_selector'), Function(remove_drag, id, if_empty=True)]

                for category in gallery_data:
                    $category_index = gallery_data.index(category)
                    textbutton category['name']:
                        action [SetVariable('showing_category', category_index), Function(reopen_selector, id)]

                textbutton 'Spoiler Filter':
                    xalign 1.0
                    # If the gallery_selector menu is not hidden, it will try to load the entire menu's contents
                    # before opening the spoiler selector menu, for some reason.
                    action [Hide('gallery_selector'), Function(renpy.show_screen, 'spoiler_checkboxes', id=id)]

            #Hbox contains the vpgrid, and then its scrollbar
            hbox:
                xfill True

                $data = gallery_data[showing_category]
                vpgrid id "selector":
                    draggable True
                    mousewheel True

                    if data['type'] in ['sound', 'music']:
                        xalign 0.5
                        cols 1

                        for item in data['contents']:

                            # Type 4 is for music that can loop
                            if item['type'] == 4:
                                if renpy.loadable(item['file']) and item['file'] not in persistent.spoiler_filter:
                                    textbutton item['title']:
                                        xfill True
                                        text_xalign 0.5
                                        text_text_align 0.5
                                        selected gallery_music == item['file']
                                        action [Function(play_music, item['file']), SetVariable('gallery_music', item['file'])]

                            # Type 5 is for a list of sound clips to cycle through
                            elif item['type'] == 5:
                                if item['keyword'] not in persistent.spoiler_filter:

                                    python:
                                        if 'index' not in item: item['index'] = 0

                                        item['filtered_contents'] = []
                                        for f in item['contents']:
                                            if renpy.loadable(f['file']) and f['file'] not in persistent.spoiler_filter:
                                                item['filtered_contents'].append(f)
                                        if item['index'] >= len(item['filtered_contents']): item['index'] = 0

                                    fixed:
                                        xfill True
                                        ysize 36
                                        hbox:
                                            xalign 0.5
                                            spacing 0
                                            null width 20
                                            textbutton item['title']:
                                                xsize 250
                                                text_color "#FFF"
                                                text_outlines [ (1, "#666", 0, 0) ]
                                                text_hover_color "#FFF"
                                                text_hover_outlines [ (1, "#666", 0, 0) ]
                                                action NullAction()

                                            if len(item['filtered_contents']) > 1:
                                                textbutton " ◀ ":
                                                    action [Function(cycle_sound, item, item['index'], increment=-1), Function(renpy.restart_interaction)]
                                            else:
                                                null width 33

                                            textbutton item['filtered_contents'][item['index']]['title']:
                                                xminimum 300
                                                text_xalign 0.5
                                                action Play('sound', item['filtered_contents'][item['index']]['file'])

                                            if len(item['filtered_contents']) > 1:
                                                textbutton " ▶ ":
                                                    action [Function(cycle_sound, item, item['index'], increment=1), Function(renpy.restart_interaction)]
                                            else:
                                                null width 33

                        #Add a blank spacer (yfill will make it fill one "space" in the vpgrid)
                        null yfill True

                        if data['type'] == 'music':
                            textbutton "Stop Music":
                                xfill True
                                text_xalign 0.5
                                text_text_align 0.5
                                action [Function(renpy.music.stop), SetVariable('gallery_music', None)]

                        elif data['type'] == 'sound':
                            fixed:
                                xfill True
                                textbutton "Play sound on page-turn":
                                    style "check_button"
                                    xalign 0.5
                                    action ToggleVariable('persistent.play_on_cycle')


                    elif data['type'] == 'image':
                        if renpy.variant('touch'):
                            cols (840 - gui.scrollbar_size) // data['mobile_dimensions'][0]
                        else:
                            cols (840 - gui.scrollbar_size) // data['dimensions'][0]

                        $index = -1
                        for item in data['contents']:
                            $index += 1
                            if renpy.loadable(item['file']) and item['file'] not in persistent.spoiler_filter:
                                button:
                                    padding (0,0)

                                    if renpy.variant('touch'):
                                        xysize data['mobile_dimensions']
                                    else:
                                        xysize data['dimensions']

                                    if renpy.variant('touch') and 'mobile_thumbnail' in item:
                                        add item['mobile_thumbnail']:
                                            align (0.5,1.0)
                                            fit "contain"
                                    elif 'thumbnail' in item:
                                        add item['thumbnail']:
                                            align (0.5,1.0)
                                            fit "contain"
                                    else:
                                        add item['base']:
                                            align (0.5,1.0)
                                            fit "contain"

                                    action [
                                               Function(set_image, id, category=data['contents'], index=index), 
                                               Hide('gallery_selector'), 
                                               Function(open_context_menu, id, drag=False)
                                           ]

                vbar value YScrollValue("selector"):
                    style "vscrollbar"
                    unscrollable "hide"
                    ysize 430
                    xalign 1.0

style selector_button_text:
    color "#eee"
    outlines [ (1, "#666", 0, 0) ]
    hover_outlines [ (1, "#2f97ba", 0, 0) ]
    selected_outlines [ (1, "#7ac5dd", 0, 0) ]

################################################################
default persistent.spoiler_checked = []
default persistent.spoiler_filter = []
default persistent.spoiler_filter_set = False

init python:
    def init_spoiler_filter():
        global spoiler_categories

        if persistent.spoiler_filter_set == False:
            persistent.spoiler_checked = []
            for key in spoiler_categories:
                persistent.spoiler_checked.append(key)

    def iter_spoiler_filter(function='check'):
        if function == 'check':
            for key in spoiler_categories:
                if key not in persistent.spoiler_checked:
                    persistent.spoiler_checked.append(key)

        elif function == 'uncheck':
            persistent.spoiler_checked = []

    def finalize_spoiler_filter():
        global spoiler_categories

        persistent.spoiler_filter = []
        for key in persistent.spoiler_checked:
            persistent.spoiler_filter += spoiler_categories[key]['contents']

        persistent.spoiler_filter_set = True

        renpy.restart_interaction

screen spoiler_checkboxes(id=None):
    modal True

    on "show" action Function(init_spoiler_filter)

    frame:
        xysize (840,480)
        align (0.5,0.5)
        left_padding 10

        background Frame(Solid('#000'))

        vbox:
            xalign 0.5
            xfill True

            python:
                if persistent.spoiler_filter_set == False:
                    notice = "SPOILER ALERT!\nPotential spoilers for checked titles will be hidden.\n(All titles will be checked by default.)"
                elif persistent.spoiler_filter_set == True:
                    notice = "Potential spoilers for checked titles will be hidden."

            text notice:
               text_align 0.5
               xalign 0.5

            null height 20

            vpgrid:
                cols 2
                xalign 0.5
                spacing 10
                for key in spoiler_categories:
                   button:
                        style "slider_button"
                        xsize 300

                        text spoiler_categories[key]['label']:
                            style "slider_button_text"

                        selected key in persistent.spoiler_checked

                        if key not in persistent.spoiler_checked:
                            action Function(persistent.spoiler_checked.append, key)
                        else:
                            action Function(persistent.spoiler_checked.remove, key)


        hbox:
            spacing 20
            align(0.5,1.0)

            button:
                text "check all"
                action Function(iter_spoiler_filter, 'check')

            button:
                text "uncheck all"
                action Function(iter_spoiler_filter, 'uncheck')

            button:
                text "confirm"

                #Reopen the closed gallery_selector window once finished
                if id:
                    action [Hide('spoiler_checkboxes'), Function(finalize_spoiler_filter), Function(renpy.show_screen, 'gallery_selector', id)]
                else:
                    action [Hide('spoiler_checkboxes'), Function(finalize_spoiler_filter)]

################################################################  
screen gallery_help():

    tag menu

    key "K_ESCAPE" action Hide('gallery_help')

    python:
        buttons = [
            {
                'text': "Help",
                'properties': {
                    'action': ShowMenu("gallery_help")
                }
            }
        ]
    use game_menu(_("Help"), scroll="viewport", nav_buttons=buttons, return_act=Hide('gallery_help')):

        style_prefix "help"

        vbox:
            spacing 10

        null height 10

        hbox:
            label _("Right-click")
            text _("Hides UI elements.")
        hbox:
            label _("Mousewheel")
            text _("Resizes the selected image.")
        hbox:
            label _("Left/Right Arrow")
            text _("Cycles the selected image.")
        hbox:
            label _("Up/Down Arrow")
            text _("Cycles the selected portrait's expression (if applicable).")
        hbox:
            label _("Spacebar")
            text _("Cycles between selected image's portrait/cutin (if applicable).")
        hbox:
            label _("Z")
            text _("Moves selected image to top of Z stack.")
        hbox:
            label _("Z (long press)")
            text _("Moves selected image to bottom of Z stack.")
        hbox:
            label _("C")
            text _("Creates a copy of the selected image.")
        hbox:
            label _("X")
            text _("Deletes the selected image.")

################################################################
label gallery:
if persistent.mainmenu_music != 'none':
    $play_music(persistent.mainmenu_music)
$quick_menu = False
call screen gallery_menu
$quick_menu = True
return