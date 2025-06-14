init python:
    def convertstrid(key):
        if key in textdict:
            return textdict[key]
        else:
            return str(key)

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

        logtextsize = touch_logtextsize

# The very first menu you see when you click the "Scene Select" button.
screen episodelist():
    default chaptername = ''
    default questname = ''
    window:
        xysize (840,480)
        background "sceneselect"
        vbox:
            pos (0,0)
            button:
                xysize(backbutton_width,backbutton_height)
                background Frame("backbutton", 16, 16)
                text backtext:
                    align (0.5, 1.0)
                    size backbutton_textsize
                action Hide("episodelist")

            if not renpy.variant('touch'):
                if add_jump_button:
                    button:
                        xysize(backbutton_width,backbutton_height)
                        background Frame("backbutton", 16, 16)
                        text jumptext:
                            align (0.5, 1.0)
                            size backbutton_textsize
                        action Replay("codeinput", locked=False)

                if add_sprite_button:
                    button:
                        xysize(backbutton_width,backbutton_height)
                        background Frame("backbutton", 16, 16)
                        text spritetext:
                            align (0.5, 1.0)
                            size backbutton_textsize
                        action Replay("spritetest", locked=False)
        vpgrid:
            rows 1
            xpos backbutton_width
            xsize (840 - backbutton_width)
            scrollbars "horizontal"
            for chapter in menudata:
                vbox:
                    button:
                        xysize (tabwidth,tabheight)
                        xpos 2
                        background Frame("booktab1")
                        bottom_padding 4
                        $chaptername = convertstrid(chapter['chaptername'])
                        text chaptername:
                            xalign (0.5)
                            ypos -2
                            size tabtextsize
                    vpgrid:
                        cols 1
                        xsize (tabwidth + gui.scrollbar_size)
                        draggable True
                        mousewheel True
                        scrollbars "vertical"
                        vscrollbar_unscrollable "hide"
  
                        for quest in chapter['quests']:
                            button:
                                xysize (tabwidth,tabheight)
                                background Frame("booktab2")
                                bottom_padding 4
                                action ShowMenu("quest", quest)

                                python:
                                    questname = convertstrid(quest['questname'])
                                    if quest['add']: questname += quest['add']

                                text questname:
                                    xalign 0.5
                                    ypos -2
                                    size tabtextsize

# The next menu you see after clicking a silver button
screen quest(data):
    modal True
    window:
        xysize (840,480)
        background "sceneselect"
        button:
            xysize(backbutton_width,backbutton_height)
            background Frame("backbutton", 16, 16)
            text backtext:
                align (0.5,1.0)
                size backbutton_textsize
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
                for log in data['logs']:
                    $lognumber = (data['logs'].index(log) + 1)
                    button:
                        xysize(backbutton_width,backbutton_height)
                        background Frame("backbutton", 16, 16)
                        text "[logtext] [lognumber]":
                            align (0.5,1.0)
                            size backbutton_textsize
                        action ShowMenu("questlog", log)

        vbox:
            xpos side_width + 3
            xsize (840 - side_width)
            button:
                xysize (tabwidth,tabheight)
                xanchor 0.5

                if renpy.variant('touch'):
                    xpos (pagewidth//2)
                else:
                    xpos pagewidth

                background Frame("booktab2")
                bottom_padding 4

                python:
                    questname = convertstrid(data['questname'])
                    if data['add']: questname += data['add']

                text questname:
                    xalign (0.5)
                    ypos -2
                    size tabtextsize

            viewport:
                xsize (840 - side_width)
                draggable True
                mousewheel True
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"

                if renpy.variant('touch'):
                    $rows = len(data['scenes'])
                    $columns = 1
                else:
                    $rows = -(len(data['scenes']) // -2)
                    $columns = 2

                grid columns rows:
                    for scene in data['scenes']:
                        button:
                            xysize (pagewidth,pageheight)
                            left_padding 4
                            right_padding 20
                            background Frame("bookpage", 35, 35)
                            action Replay(scene['avg'], locked=False)

                            python:
                                #title text
                                scenename = convertstrid(scene['scenename'])
                                if scene['add']: scenename += scene['add']

                                #"info" text underneath
                                if scene['sceneinfo']: info = convertstrid(scene['sceneinfo'])
                                else: info = None

                            vbox:
                                align (0.5,0.5)
                                text scenename:
                                    xalign 0.5
                                    text_align 0.5
                                    size pagetextsize
                                    color "#710905" #adds a red color to scene title text

                                if info:
                                    text info:
                                        xalign 0.5
                                        text_align 0.5
                                        size (pagetextsize - 2)
                                        color "#34374b" #adds a dark blue color to info text

# The menu that opens when you click a "Log" button from within the "quest" menu
screen questlog(data):
    default fulltext = ''
    default prefix = ''
    python:
        if data['type'] == 1: prefix = logmain + ' '
        elif data['type'] == 2: prefix = logsub + ' '
        elif data['type'] == 16: prefix = logdaily + ' '

        fulltext += prefix + textdict[data['title']] + '\n'
        fulltext += loglevel + ' ' + str(data['level']) + '\n'
        fulltext += logclient + ' ' + textdict[data['client']] + '\n'
        fulltext += logdetails + ' ' + textdict[data['details']] + '\n'
        
        for step in data['steps']:
            fulltext += ' ' + logbullet + ' ' + textdict[step] + '\n'
        
    modal True
    window:
        xysize (840,480)
        background "sceneselect"
        button:
            xysize(backbutton_width,backbutton_height)
            background Frame("backbutton", 16, 16)
            text backtext:
                align (0.5,1.0)
                size backbutton_textsize
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
                text "[fulltext]":
                    yalign 0.2
                    text_align 0
                    size logtextsize
