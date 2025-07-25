init python:
    def convertstrid(key):
        if key in textdict:
            return textdict[key]
        else:
            return str(key)

    def add_text_tags(text, tagdict):
        for tag in list(tagdict.keys()):
            val = tagdict[tag]
            if tag == 'style': tag = ''

            front_tag = '{' + f'{tag}={val}' + '}'
            end_tag = '{/' + tag + '}'
            text = front_tag + text + end_tag
        return text

    def fit_text(text, textsize, max_dimensions, tagdict={}, ret_type='Text'):
        sized = Text(text, size=textsize)
        while sized.size()[0] > max_dimensions[0] or sized.size()[1] > max_dimensions[1]:
            #Guardrail to not let it get too crazy small
            if textsize <= 10: break

            textsize -= 1
            sized = Text(text, size=textsize)

        tagdict['size'] = textsize
        tagged_text = add_text_tags(text, tagdict)

        if ret_type == 'Text': return Text(tagged_text)
        elif ret_type == 'string': return tagged_text

    if renpy.variant('touch'):
    # Both the PC and Mobile values can be set in CONFIG.rpy
        backbutton_width = touch_backbutton_width 
        backbutton_height = touch_backbutton_height
        backbutton_textsize = touch_backbutton_textsize

        tabwidth = touch_tabwidth
        tabheight = touch_tabheight
        tabtextsize = touch_tabtextsize

        pagewidth = touch_pagewidth
        pageheight = touch_pageheight
        pagetextsize = touch_pagetextsize
        pagecolumns = touch_pagecolumns

        logtextsize = touch_logtextsize


# Styles used for all buttons on the left sidebar, including the "Back" button
    style.backbutton = Style('button')
    style.backbutton.background = Frame("backbutton", 16, 16)
    style.backbutton.xysize = (backbutton_width,backbutton_height)

    style.backbutton_text = Style('text')
    style.backbutton_text.align = (0.5, 1.0)
    style.backbutton_text.size = backbutton_textsize
    style.backbutton_text.font = backbutton_font

# Styles used for the gold and silver "booktab" buttons/labels
    style.tabbutton = Style('button')
    style.tabbutton.xysize = (tabwidth,tabheight)

    style.tabbutton_text = Style('text')
    style.tabbutton_text.pos = (0.5,0.5)
    # tabtextsize needs to be changed from inside CONFIG.rpy
    tabbutton_texttags = {
        'font':  tabfont # is in CONFIG.rpy
    }

    style.goldtab = Style('tabbutton')
    style.goldtab.background = Frame("booktab1")

    style.silvertab = Style('tabbutton')
    style.silvertab.background = Frame('booktab2')

# Styles used for the "bookpage" buttons that play cutscenes when clicked
    style.bookpage = Style('button')
    style.bookpage.background = Frame("bookpage", 35, 35)
    style.bookpage.xysize = (pagewidth,pageheight)
    style.bookpage.padding = (4, 0, 20, 0) #(left, top, right, bottom)

    style.bookpage_text = Style('text')
    style.bookpage_text.align = (0.5, 0.5)
    style.bookpage_text.text_align = 0.5
    style.bookpage_text.font = pagefont
    # pagetextsize needs to be changed from inside CONFIG.rpy

# Styles used for the questlog screen
    style.questlog = Style('button')
    style.questlog.background = Frame("bookpage", 35, 35)
    style.questlog.xsize = (840 - backbutton_width - gui.scrollbar_size)
    style.questlog.padding = (20, 0, 20, 0) #(left, top, right, bottom)

    style.questlog_text = Style('text')
    style.questlog_text.yalign = 0.2
    style.questlog_text.text_align = 0
    style.questlog_text.size = logtextsize
    style.questlog_text.font = logfont


# The very first menu you see when you click the "Scene Select" button.
screen episodelist():
    window:
        xysize (840,480)
        background "sceneselect"
        vbox:
            pos (0,0)
            # "Back" button
            textbutton backtext:
                style "backbutton"
                text_style "backbutton_text"
                action Hide("episodelist")

            if not renpy.variant('touch'):
                # "Jump" button
                if add_jump_button:
                    textbutton jumptext:
                        style "backbutton"
                        text_style "backbutton_text"
                        action Replay("codeinput", locked=False)

                # "Sprite" button
                if add_sprite_button:
                    textbutton spritetext:
                        style "backbutton"
                        text_style "backbutton_text"
                        action Replay("spritetest", locked=False)

        vpgrid:
            rows 1
            xpos backbutton_width
            xsize (840 - backbutton_width)
            scrollbars "horizontal"

            # Create a separate column for each chapter/category
            for chapter in menudata:
                vbox:
                    # Gold chapter label button
                    python:
                        if 'name_fit' not in chapter:
                            chaptername = convertstrid(chapter['chaptername'])

                            # Stores the text as a Text object, 
                            # so the style needs to be added as a tag here for certain things like font to be applied correctly
                            chaptername_fit = fit_text(chaptername, tabtextsize, (tabwidth-16, tabheight), tagdict=tabbutton_texttags)
                            chaptername_xcenter = int(chaptername_fit.size()[0]*.5)
                            chaptername_ycenter = int(chaptername_fit.size()[1]*tabfont_center)

                            # Cache the result:
                            chapter['name_fit'] = chaptername_fit
                            chapter['name_xcenter'] = chaptername_xcenter
                            chapter['name_ycenter'] = chaptername_ycenter

                        else:
                            chaptername_fit = chapter['name_fit']
                            chaptername_xcenter = chapter['name_xcenter']
                            chaptername_ycenter = chapter['name_ycenter']

                    textbutton chaptername_fit:
                        style "goldtab"
                        text_style "tabbutton_text"
                        text_anchor (chaptername_xcenter, chaptername_ycenter)
                        

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
                                if 'name_fit' not in quest:
                                    questname = convertstrid(quest['questname'])
                                    if quest['add']: questname += quest['add']

                                    # Stores the text as a Text object, 
                                    # so the style needs to be added as a tag here for certain things like font to be applied correctly
                                    questname_fit = fit_text(questname, tabtextsize, (tabwidth-16, tabheight), tagdict=tabbutton_texttags)
                                    questname_xcenter = int(questname_fit.size()[0]*.5)
                                    questname_ycenter = int(questname_fit.size()[1]*tabfont_center)

                                    # Cache the result:
                                    quest['name_fit'] = questname_fit
                                    quest['name_xcenter'] = questname_xcenter
                                    quest['name_ycenter'] = questname_ycenter

                                else:
                                    questname_fit = quest['name_fit']
                                    questname_xcenter = quest['name_xcenter']
                                    questname_ycenter = quest['name_ycenter']

                            textbutton questname_fit:
                                style "silvertab"
                                text_style "tabbutton_text"
                                text_anchor (questname_xcenter, questname_ycenter)
                                action ShowMenu("quest", quest)



# The next menu you see after clicking a silver button
screen quest(data):
    modal True
    window:
        xysize (840,480)
        background "sceneselect"

        # "Back" button
        textbutton backtext:
            style "backbutton"
            text_style "backbutton_text"
            action Hide("quest")

        $side_width = (backbutton_width + gui.scrollbar_size)
        viewport:
            ypos backbutton_height
            xsize side_width
            ysize (480 - backbutton_height)
            draggable True
            mousewheel True
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            vbox:
                # Left sidebar "Log" buttons
                for log in data['logs']:
                    python:
                        if 'loglabel' not in log:
                            lognumber = (data['logs'].index(log) + 1)
                            loglabel = f'{logtext} {lognumber}'

                            # Cache the result
                            log['loglabel'] = loglabel

                        else:
                            loglabel = log['loglabel']

                    textbutton loglabel:
                        style "backbutton"
                        text_style "backbutton_text"
                        action ShowMenu("questlog", log)

        vbox:
            xpos side_width + 3
            xsize (840 - side_width)

            # Silver tab quest name label at the top of the screen
            python:
                if 'name_fit' not in data:
                    questname = convertstrid(data['questname'])
                    if data['add']: questname += quest['add']

                    # Stores the text as a Text object, 
                    # so the style needs to be added as a tag here for certain things like font to be applied correctly
                    questname_fit = fit_text(questname, tabtextsize, (tabwidth-16, tabheight), tagdict=tabbutton_texttags)
                    questname_xcenter = int(questname_fit.size()[0]*.5)
                    questname_ycenter = int(questname_fit.size()[1]*tabfont_center)

                    # Cache the result:
                    data['name_fit'] = questname_fit
                    data['name_xcenter'] = questname_xcenter
                    data['name_ycenter'] = questname_ycenter

                else:
                    questname_fit = data['name_fit']
                    questname_xcenter = data['name_xcenter']
                    questname_ycenter = data['name_ycenter']

            textbutton questname_fit:
                style "silvertab"
                xanchor 0.5
                # Center the button over the bookpage columns, without taking into account the scrollbar width
                xpos (pagecolumns*pagewidth) //2
                text_style "tabbutton_text"
                text_anchor (questname_xcenter, questname_ycenter)

            vpgrid:
                cols pagecolumns
                xsize (840 - side_width)
                draggable True
                mousewheel True
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"

                # "Bookpage" buttons that play a cutscene when clicked
                for scene in data['scenes']:
                    python:
                        if 'scenename_fit' not in scene:
                            # Title text
                            scenename = convertstrid(scene['scenename'])
                            if scene['add']: scenename += scene['add']

                            # Stores the tagged text as a string, so the style will be applied in the textbutton block
                            scenename_fit = fit_text(scenename, pagetextsize, ((pagewidth-20), pageheight), tagdict={'color': '#710905'}, ret_type='string')

                            #"info" text underneath
                            if scene['sceneinfo']: 
                                # Info text
                                info = convertstrid(scene['sceneinfo'])

                                # Stores the tagged text as a string, so the style will be applied in the textbutton block
                                info_fit = fit_text(info, (pagetextsize-2), ((pagewidth-20), pageheight), tagdict={'color':'#34374b'}, ret_type='string')

                                scenename_fit += f'\n{info_fit}'

                            # Cache the result
                            scene['scenename_fit'] = scenename_fit

                        else:
                            scenename_fit = scene['scenename_fit']

                    textbutton scenename_fit:
                        style "bookpage"
                        text_style "bookpage_text"
                        action Replay(scene['avg'], locked=False)



# The menu that opens when you click a "Log" button from within the "quest" menu
screen questlog(data):
    python:
        if 'fulltext' not in data:
            fulltext = ''
            prefix = ''

            if data['type'] == 1: prefix = logmain + ' '
            elif data['type'] == 2: prefix = logsub + ' '
            elif data['type'] == 16: prefix = logdaily + ' '

            fulltext += prefix + convertstrid(data['title']) + '\n'
            fulltext += loglevel + ' ' + str(data['level']) + '\n'
            fulltext += logclient + ' ' + convertstrid(data['client']) + '\n'
            fulltext += logdetails + ' ' + convertstrid(data['details']) + '\n'
        
            for step in data['steps']:
                fulltext += ' ' + logbullet + ' ' + convertstrid(step) + '\n'

            data['fulltext'] = fulltext

        else:
            fulltext = data['fulltext']

    modal True
    window:
        xysize (840,480)
        background "sceneselect"

        # "Back" button
        textbutton backtext:
            style "backbutton"
            text_style "backbutton_text"
            action Hide("questlog")

        viewport:
            xpos backbutton_width
            xsize (840 - backbutton_width)
            draggable True
            mousewheel True
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            textbutton fulltext:
                style "questlog"
                text_style "questlog_text"
