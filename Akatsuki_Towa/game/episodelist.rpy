init python:

    #convertstrid implementation has been moved to deffunctions.rpy
    #def convertstrid(key):
    #    if key in textdict:
    #        return textdict[key]
    #    else:
    #        return str(key)

    def add_text_tags(text, tag_dict):
        for tag in list(tag_dict.keys()):
            val = tag_dict[tag]
            if tag == 'style': tag = ''

            front_tag = '{' + f'{tag}={val}' + '}'
            end_tag = '{/' + tag + '}'
            text = front_tag + text + end_tag
        return text

    def calculate_text_anchor(textobject, anchors):
        width, height = textobject.size()
        xanchor = int(width * anchors[0])
        yanchor = int(height * anchors[1])

        return (xanchor, yanchor)

    def size_text(text, size, max_dimensions, anchors=None, tag=False, tag_dict={}):
        sized = Text(text, size=size)
        while sized.size()[0] > max_dimensions[0] or sized.size()[1] > max_dimensions[1]:
            #Guardrail to not let it get too crazy small
            if size <= 10: break

            size -= 1
            sized = Text(text, size=size)

        if tag:
            tag_dict['size'] = size
            text = add_text_tags(text, tag_dict)
            if anchors:
                anchors = calculate_text_anchor(sized, anchors)
                return (text, anchors)
            else:
                return text
        else:
            if anchors:
                anchors = calculate_text_anchor(sized, anchors)
                return (size, anchors)
            else:
                return size

    def calculate_inner_space(style_name):
        style_object = style.get(style_name)
        horizontal = style_object.xmaximum - style_object.left_padding - style_object.right_padding - style_object.left_margin - style_object.right_margin
        vertical =  style_object.ymaximum - style_object.top_padding - style_object.bottom_padding - style_object.top_margin - style_object.bottom_margin
        return(horizontal,vertical) 

    if renpy.variant('touch'):
    # Both the PC and Mobile values can be set in CONFIG.rpy
        sidearea_button_width = touch_sidearea_button_width 
        sidearea_button_height = touch_sidearea_button_height
        sidearea_button_textsize = touch_sidearea_button_textsize

        tabwidth = touch_tabwidth
        tabheight = touch_tabheight
        tabtextsize = touch_tabtextsize

        scenebutton_width = touch_scenebutton_width
        scenebutton_height = touch_scenebutton_height
        scenebutton_textsize = touch_scenebutton_textsize
        scenebutton_columns = touch_scenebutton_columns

        logtextsize = touch_logtextsize

        add_gallery_button = add_gallery_button_mobile

# Styles used for all buttons on the left sidebar
    style.sidearea_button = Style('button')
    style.sidearea_button.background = Frame("sidearea_tab", 20,0)
    style.sidearea_button.xysize = (sidearea_button_width,sidearea_button_height)
    style.sidearea_button.align = (1.0,0)
    style.sidearea_button.padding = (12, 0, 2, 0)

    sidearea_button_inner_space = calculate_inner_space('sidearea_button')

    style.sidearea_button_text = Style('text')
    style.sidearea_button_text.pos = (0, 0.5)
    style.sidearea_button_text.font = sidearea_button_font
    style.sidearea_button_text.color = '#505050'
    style.sidearea_button_text.hover_color = "#656565"
    style.sidearea_button_text.selected_color = "#808080"
    #sidearea_button_textsize needs to be changed from CONFIG.rpy

# Styles used for the gold and silver "booktab" buttons/labels
    style.tabbutton = Style('button')
    style.tabbutton.xysize = (tabwidth,tabheight)

    style.tabbutton_text = Style('text')
    style.tabbutton_text.pos = (0.5,0.5)
    style.tabbutton_text.font = tabfont # is in CONFIG.rpy
    style.tabbutton_text.color = '#505050'
    # tabtextsize needs to be changed from inside CONFIG.rpy
    tabbutton_texttags = {
        'font':  tabfont, # is in CONFIG.rpy
        'color': '#505050'
    }

    style.goldtab = Style('tabbutton')
    style.goldtab.background = Frame("booktab1")
    #The gold tab has an extra "swoosh" 10% into the left side of the image that the text needs to try to avoid
    style.goldtab.left_padding = int(style.tabbutton.xmaximum * 0.1)
    style.goldtab.right_padding = int(style.tabbutton.xmaximum * 0.1)

    goldtab_inner_space = calculate_inner_space('goldtab')
    
    style.silvertab = Style('tabbutton')
    style.silvertab.background = Frame('booktab2')
    style.silvertab.activate_sound = "other_7004.ogg"
    #The silver tab just needs to keep text off of its edges/corners
    style.silvertab.left_padding = int(style.tabbutton.xmaximum * 0.04)
    style.silvertab.right_padding = int(style.tabbutton.xmaximum * 0.04)

    silvertab_inner_space = calculate_inner_space('silvertab')

# Styles used for the buttons that play cutscenes when clicked
    style.scene_button = Style('button')
    style.scene_button.background = Frame("scenebutton", 41,41)
    style.scene_button.xysize = (scenebutton_width,scenebutton_height)
    style.scene_button.padding = (14, 13, 14, 13) #(left, top, right, bottom)
    style.scene_button.activate_sound = "common_select.ogg"

    scenebutton_inner_space = calculate_inner_space('scene_button')

    scene_button_texttags = {
        'font':  scenebutton_font, # is in CONFIG.rpy
        'text_align': 0.5
    }

# Styles used for the questlog screen
    style.questlog_text = Style('text')
    style.questlog_text.yalign = 0.0
    style.questlog_text.text_align = 0
    style.questlog_text.size = logtextsize
    style.questlog_text.font = logfont

# Styles used for the different parts of the book background
    #Needed to be separated from the image for the corners in order to be able to tile it
    #This goes on the bottom layer, and contains nothing
    style.book_backing = Style('frame')
    style.book_backing.background = Frame("book_backing", 55, 48, 95,95, tile="300")
    style.book_backing.padding = (0,0,0,0)
    style.book_backing.margin = (0,0,1,-1)
    
    style.book_corners = Style('frame')
    style.book_corners.background = Frame("book_corners", 60,60)
    style.book_corners.xysize = (840,480)
    style.book_corners.margin = (0,0,0,-1)

    style.book_paper_frame = Style('frame')
    style.book_paper_frame.background = Frame("book_paper", 48,48, tile=True)
    shadowless_paper = Frame("book_paper_cropped", 48,48, tile=True)
    style.book_paper_frame.xsize = (840 - style.sidearea_button.xmaximum - gui.scrollbar_size)
    style.book_paper_frame.xalign = 1.0
    style.book_paper_frame.ysize = 480
    style.book_paper_frame.padding = (16,12,22,12)
    style.book_paper_frame.margin = (0,2,17,3)

    paper_leftshadow_width = 12
    paper_bottomshadow_height = 12
    paper_strip_pos = 422
    paper_inner_space = calculate_inner_space('book_paper_frame')

# Style used for the x/back button
    style.x_button = Style('button')
    style.x_button.background = Frame("red_return_button_idle")
  #Renpy will "hover" over the top-left corner pixel in touch mode when nothing else is being touched,
  #causing unintended behavior and delays
    if not renpy.variant("touch"):
        style.x_button.hover_background = Frame("red_return_button_hover")
        style.x_button.hover_sound = "common_tag.ogg"
    style.x_button.activate_sound = "common_cancel.ogg"
    style.x_button.xsize = int(((840 - style.book_paper_frame.xmaximum) + paper_leftshadow_width) * 1.4)
    style.x_button.ysize = style.x_button.xmaximum
    style.x_button.anchor = (0.4,0.4)
    style.x_button.pos = (0,0)
    style.x_button.focus_mask = True

    x_button_height  = int(style.x_button.xmaximum * 0.6)

# Styles use for the sidearea menua itself
    style.sidearea_vpgrid = Style('vpgrid')
    style.sidearea_vpgrid.xsize = sidearea_button_width

    style.sidearea_side.xpos = (840 - style.book_paper_frame.xmaximum) + paper_leftshadow_width
    style.sidearea_side.xanchor = 1.0
    style.sidearea_side.yanchor = 0
    style.sidearea_side.ypos = x_button_height
    style.sidearea_side.ysize = 480 - x_button_height - paper_bottomshadow_height
    style.sidearea_side.spacing = 0


#Used as the bottom-level background
screen book_background():
    frame:
        xysize (840,480)
        background "#000"
        padding (0,0,0,0)

        #Only the leather back for the book
        #Purely decorative
        frame:
            style "book_backing"

        #Then this image needs to go underneath the book corner frame so it's going here
        image "bracer_emblem":
            yanchor 1.0
            ypos 450
            xpos 16

        frame:
            style "book_corners"


#Create a dictionary to store "found" text sizes for sidearea button labels.  
#It's going to be more efficient to reuse these by their string instead of storing each log's label in the meu data
default side_fit = dict()

#This is where side-bar buttons end up.
#This screen is sandwiched above the book_background screen, but below the book_paper screen, in order to keep shadows consistent
screen sidearea(buttonlist=[]):
    style_prefix "sidearea"
    side "c l":
        vpgrid id "side":
            draggable True
            mousewheel True
            cols 1

            for b in buttonlist:
                python:
                    text = b['text']
                    properties = b['properties']

                    if text not in side_fit:
                        text_size, text_anchor = size_text(text, sidearea_button_textsize, sidearea_button_inner_space, anchors=(0, tabfont_center))

                        #Cache the result
                        side_fit[text] = {
                            'size': text_size,
                            'anchor': text_anchor,
                        }

                    else:
                        text_size = side_fit[text]['size']
                        text_anchor = side_fit[text]['anchor']

                textbutton text:
                    text_size text_size
                    text_anchor text_anchor
                    properties properties

            transclude

        vbar value YScrollValue("side"):
            style "vscrollbar"
            unscrollable "hide"

#Used as the background for the main viewport.
#Has a hide_shadow option to try to avoid stacking the transparency of shadows when multiple copies of this background are stacked on top of each other.
screen book_paper(hide_shadow=False):
        frame: #Paper
            style_prefix "book_paper"
            if hide_shadow:
                background shadowless_paper

            add Frame("book_paper_strip", tile=True):
                ysize 22
                xsize None
                ypos paper_strip_pos

            transclude

#The go-to close/back button
#Will hide [screen_title], and can be customized with additional actions to perform at the same time as hiding the menu.
screen x_button(screen_title, icon, additional_actions=[]):
    tag x
    button:
        style "x_button"
        action [Hide(screen_title), Return()] + additional_actions

        if icon == 'x':
            add Frame("images_free/gui/x.png"):
                anchor (0.5,0.5)
                pos (.53,.53)
                xsize int(style.x_button.xmaximum * .225)
                ysize int(style.x_button.xmaximum * .225)
        elif icon == 'arrow':
            add Frame("images_free/gui/arrow.png"):
                anchor (0.5,0.5)
                pos (.53,.53)
                xsize int(style.x_button.xmaximum * .225)
                ysize int(style.x_button.xmaximum * .225)


# The very first menu you see when you click the "Scene Select" button.
screen episodelist():
    modal True

    use book_background()

    python:
        buttonlist = []
        if not renpy.variant('touch'):
            if add_jump_button:
                buttonlist.append({'text': jumptext, 'properties': {'action': Replay("codeinput", locked=False)}})

        if add_gallery_button:
            buttonlist.append({'text': gallerytext, 'properties': {'action': Replay("gallery", locked=False)}})

    use sidearea(buttonlist)

    use book_paper():
        vpgrid:
            rows 1
            scrollbars "horizontal"

            if not renpy.variant('touch'):
                ysize (paper_strip_pos + gui.scrollbar_size)
                scrollbar_yoffset 7
            else:
                ysize paper_inner_space[1]

            # Create a separate column for each chapter/category
            for chapter in menudata:
                vbox:
                    # Gold chapter label button
                    python:
                        chaptername = convertstrid(chapter['chaptername'])

                        if 'name_size' not in chapter:
                            text_size, text_anchor = size_text(chaptername, tabtextsize, goldtab_inner_space, anchors=(0.5, tabfont_center))

                            # Cache the result:
                            chapter['name_size'] = text_size
                            chapter['name_anchor'] = text_anchor

                        else:
                            text_size = chapter['name_size']
                            text_anchor = chapter['name_anchor']

                    textbutton chaptername:
                        style "goldtab"
                        text_style "tabbutton_text"
                        text_size text_size
                        text_anchor text_anchor
                                
                    vpgrid:
                        cols 1
                        xsize (tabwidth + gui.scrollbar_size)
                        draggable True
                        mousewheel True
                        scrollbars "vertical"
                        vscrollbar_unscrollable "hide"
          
                        # Silver tab buttons that open "quest" menu
                        for quest in chapter['quests']:
                            python:
                                questname = convertstrid(quest['questname'])
                                if quest['add']: questname += quest['add']

                                if 'name_size' not in quest:
                                    text_size, text_anchor = size_text(questname, tabtextsize, silvertab_inner_space, anchors=(0.5,  tabfont_center))

                                    # Cache the result:
                                    quest['name_size'] = text_size
                                    quest['name_anchor'] = text_anchor

                                else:
                                    text_size = quest['name_size']
                                    text_anchor = quest['name_anchor']

                            textbutton questname:
                                style "silvertab"
                                text_style "tabbutton_text"
                                text_size text_size
                                text_anchor text_anchor
                                action ShowMenu("quest", quest)

    use x_button('episodelist', 'x')



#This will let the button whose log is being displayed light up, without lighting up all of the other log buttons
default showing_log = None

# The next menu you see after clicking a silver button
screen quest(data):
    modal True

    use book_background()

    python:
        # Left sidebar "Log" buttons
        buttonlist = []
        for log_index in range(0, len(data['logs'])):
            log = data['logs'][log_index]
            if 'loglabel_fit' not in log:
                lognumber = (log_index + 1)

                loglabel = f'{logtext} {lognumber}'

                buttonlist.append(
                    {
                        'text': loglabel, 
                        'properties': {
                            'selected': (showing_log == log_index),
                            'activate_sound': 'other_7004.ogg',
                            'action': [
                                ShowMenu("questlog", data['logs'], log_index),
                                SetVariable('showing_log', log_index)
                            ]
                        }
                    }
                )
    use sidearea(buttonlist)


    use book_paper():
        style_prefix "book_paper"
        vbox:
            # Silver tab quest name label at the top of the screen
            python:
                questname = convertstrid(data['questname'])
                if data['add']: questname += data['add']

                text_size = data['name_size']
                text_anchor = data['name_anchor']

            textbutton questname:
                style "silvertab"
                xanchor 0.5
                # Center the button over the scenebutton columns, without taking into account the scrollbar width
                xpos paper_inner_space[0] //2
                text_style "tabbutton_text"
                text_size text_size
                text_anchor text_anchor

            vpgrid:
                cols scenebutton_columns
                draggable True
                mousewheel True
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"

                ysize paper_strip_pos - tabheight

                # buttons that play a cutscene when clicked
                for scene in data['scenes']:
                    python:
                        if 'scenename_fit' not in scene:
                            # Title text
                            scenename = convertstrid(scene['scenename'])
                            if scene['add']: scenename += scene['add']

                            # Stores the tagged text as a string, so the style will be applied in the textbutton block
                            scenename_fit = size_text(scenename, scenebutton_textsize, scenebutton_inner_space, tag=True, tag_dict={'color': '#710905'})

                            #"info" text underneath
                            if scene['sceneinfo']: 
                                # Info text
                                info = convertstrid(scene['sceneinfo'])

                                # Stores the tagged text as a string, so the style will be applied in the textbutton block
                                info_fit = size_text(info, (scenebutton_textsize-2), scenebutton_inner_space, tag=True, tag_dict={'color':'#34374b'})

                                scenename_fit += f'\n{info_fit}'

                            combined_fit = Text(scenename_fit, **scene_button_texttags)
                            combined_anchor = calculate_text_anchor(combined_fit, (0.5, 0.5))

                            # Cache the result
                            scene['combined_fit'] = combined_fit
                            scene['combined_anchor'] = combined_anchor

                        else:
                            combined_fit = scene['combined_fit']
                            combined_anchor = scene['combined_anchor']

                    button:
                        style_prefix "scene"
                        text combined_fit:
                            anchor combined_anchor
                            pos ((scenebutton_inner_space[0]//2), (scenebutton_inner_space[1]//2))
                        action Replay(scene['avg'], locked=False)

    use x_button('quest', 'arrow')


# The menu that opens when you click a "Log" button from within the "quest" menu
screen questlog(log_list, current_index):
    #modal True

    tag log
    python:
        data = log_list[current_index]

        if data['type'] == 1: prefix = logmain + ' '
        elif data['type'] == 2: prefix = logsub + ' '
        elif data['type'] == 16: prefix = logdaily + ' '
        else: prefix = '   '

        log_line_length = int(paper_inner_space[0] * .85)

    use book_paper(hide_shadow=True):
        style_prefix "book_paper"

        #Keep the scrollbar's position consistent with the "quest" menu's
        $textbox_width = int((style.scene_button.xmaximum * scenebutton_columns))

        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"

            ysize paper_strip_pos
            xsize (textbox_width + gui.scrollbar_size)

            vbox:
                spacing 5
                vbox:
                    xsize textbox_width

                    #Add spacing to the top to add spacing
                    null height 10

                    hbox:
                        text prefix:
                            color "#415866"
                        text [convertstrid(data['title'])]:
                            color "#1C3051"
                    hbox:
                        text [loglevel + ' ']:
                            color "#415866"
                        text [str(data['level'])]:
                            color "#1C3051"
                    hbox:
                        text [logclient + ' ']:
                            color "#415866"
                        text [convertstrid(data['client'])]:
                            color "#1C3051"
                    hbox:
                        text [logdetails + ' ']:
                            color "#415866"
                        text [convertstrid(data['details'])]:
                            color "#1C3051"
                add "underline":
                    xsize log_line_length
                    xalign 0.5
                vbox:
                    for step in data['steps']:
                        hbox:
                            #Add spacing to the left of all bullet points
                            null width 10

                            text [' ' + logbullet + ' ']:
                                color "#415866"
                            text [convertstrid(step)]:
                                color "#1C3051"

    use x_button('questlog', 'arrow', [SetVariable('showing_log', None)])
