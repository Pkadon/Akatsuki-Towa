init python:
    def convertstrid(key):
        if key in textdict:
            return textdict[key]
        else:
            return str(key)

    def fit_text(text, original_size, max_dimensions, color=gui.text_color):
        sized = Text(text, size=original_size, color=color, text_align=0.5)
        while sized.size()[0] > max_dimensions[0] or sized.size()[1] > max_dimensions[1]:
            #Guardrail to not let it get too crazy small
            if original_size <= 10: break

            original_size -= 1
            sized = Text(text, size=original_size, color=color, text_align=0.5)
        return sized

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


    # Style used for all buttons on the left sidebar, including the "Back" button
    style.backbutton = Style("button")
    style.backbutton.background = Frame("backbutton", 16, 16)
    style.backbutton.xysize = (backbutton_width,backbutton_height)

    style.backbutton_text = Style("text")
    style.backbutton_text.align = (0.5, 1.0)
    style.backbutton_text.size = backbutton_textsize

    # Styles used for the gold and silver "booktab" buttons/labels
    style.tabbutton = Style("button")
    style.tabbutton.xysize = (tabwidth,tabheight)

    style.tabbutton_text = Style("text")
    style.tabbutton_text.xalign = 0.5
    style.tabbutton_text.ypos = 0.5

    style.goldtab = Style("tabbutton")
    style.goldtab.background = Frame("booktab1")

    style.silvertab = Style("tabbutton")
    style.silvertab.background = Frame("booktab2")


# The very first menu you see when you click the "Scene Select" button.
screen episodelist():
    default chaptername = ''
    default questname = ''
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
                        if 'chaptername_fit' not in chapter:
                            chaptername = convertstrid(chapter['chaptername'])
                            chaptername_fit = fit_text(chaptername, tabtextsize, (tabwidth-16, tabheight))
                            chaptername_center = int(chaptername_fit.size()[1]*.55)

                            # Cache the result:
                            chapter['chaptername_fit'] = chaptername_fit
                            chapter['chaptername_center'] = chaptername_center

                        else:
                            chaptername_fit = chapter['chaptername_fit']
                            chaptername_center = chapter['chaptername_center']

                    textbutton chaptername_fit:
                        style "goldtab"
                        xpos 2
                        text_style "tabbutton_text"
                        text_yanchor chaptername_center
                            

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
                                if 'questname_fit' not in quest:
                                    questname = convertstrid(quest['questname'])
                                    if quest['add']: questname += quest['add']

                                    questname_fit = fit_text(questname, tabtextsize, (tabwidth-16, tabheight))
                                    questname_center = int(questname_fit.size()[1]*.55)

                                    # Cache the result:
                                    quest['questname_fit'] = questname_fit
                                    quest['questname_center'] = questname_center

                                else:
                                    questname_fit = quest['questname_fit']
                                    questname_center = quest['questname_center']

                            textbutton questname_fit:
                                style "silvertab"
                                text_style "tabbutton_text"
                                text_yanchor questname_center
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
                if 'questname_fit' not in data:
                    questname = convertstrid(data['questname'])
                    if data['add']: questname += quest['add']

                    questname_fit = fit_text(questname, tabtextsize, (tabwidth-16, tabheight))
                    questname_center = int(questname_fit.size()[1]*.55)

                    # Cache the result:
                    data['questname_fit'] = questname_fit
                    data['questname_center'] = questname_center

                else:
                    questname_fit = data['questname_fit']
                    questname_center = data['questname_center']

            textbutton questname_fit:
                style "silvertab"
                xanchor 0.5
                if renpy.variant('touch'):
                    xpos (pagewidth//2)
                else:
                    xpos pagewidth
                text_style "tabbutton_text"
                text_yanchor questname_center

            viewport:
                xsize (840 - side_width)
                draggable True
                mousewheel True
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"

                if pagecolumns == 1:
                    $pagerows = len(data['scenes'])
                else:
                    $pagerows = -(len(data['scenes']) // (-pagecolumns))
                grid pagecolumns pagerows:
                    # "Bookpage" buttons that play s cutscene when clicked
                    for scene in data['scenes']:
                        button:
                            xysize (pagewidth,pageheight)
                            left_padding 4
                            right_padding 20
                            background Frame("bookpage", 35, 35)
                            action Replay(scene['avg'], locked=False)

                            python:
                                if 'scenename_fit' not in scene:
                                    #title text
                                    scenename = convertstrid(scene['scenename'])
                                    if scene['add']: scenename += scene['add']

                                    scenename_fit = fit_text(scenename, pagetextsize, ((pagewidth-20), pageheight), color="#710905")

                                    #"info" text underneath
                                    if scene['sceneinfo']: 
                                        info = convertstrid(scene['sceneinfo'])
                                        info_fit = fit_text(info, (pagetextsize-2), ((pagewidth-20), pageheight), color="#34374b")
                                    else: info = None

                                    scene['scenename_fit'] = scenename_fit
                                    scene['info_fit'] = info_fit

                                else:
                                    scenename_fit = scene['scenename_fit']
                                    info_fit = scene['info_fit']

                            vbox:
                                align (0.5,0.5)
                                text scenename_fit:
                                    xalign 0.5

                                if info_fit:
                                    text info_fit:
                                        xalign 0.5

# The menu that opens when you click a "Log" button from within the "quest" menu
screen questlog(data):
    default fulltext = ''
    default prefix = ''
    python:

        if 'fulltext' not in data:
            if data['type'] == 1: prefix = logmain + ' '
            elif data['type'] == 2: prefix = logsub + ' '
            elif data['type'] == 16: prefix = logdaily + ' '

            fulltext += prefix + textdict[data['title']] + '\n'
            fulltext += loglevel + ' ' + str(data['level']) + '\n'
            fulltext += logclient + ' ' + textdict[data['client']] + '\n'
            fulltext += logdetails + ' ' + textdict[data['details']] + '\n'
        
            for step in data['steps']:
                fulltext += ' ' + logbullet + ' ' + textdict[step] + '\n'

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
            button:
                background Frame("bookpage", 35, 35)
                xsize (840 - backbutton_width - gui.scrollbar_size)
                left_padding 20
                right_padding 20
                text fulltext:
                    yalign 0.2
                    text_align 0
                    size logtextsize
