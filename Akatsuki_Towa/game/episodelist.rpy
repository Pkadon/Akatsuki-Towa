init python:
    def convertstrid(key):
        if key in textdict:
            return textdict[key]
        else:
            return str(key)


    backbutton_width = 94
    backbutton_height = 37

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
                    size 25
                action Hide("episodelist")

            if add_jump_button:
                button:
                    xysize(backbutton_width,backbutton_height)
                    background Frame("backbutton", 16, 16)
                    text jumptext:
                        align (0.5, 1.0)
                        size 25
                    action Replay("codeinput", locked=False)

            if add_sprite_button:
                button:
                    xysize(backbutton_width,backbutton_height)
                    background Frame("backbutton", 16, 16)
                    text spritetext:
                        align (0.5, 1.0)
                        size 25
                    action Replay("spritetest", locked=False)
        vpgrid:
            rows 1
            xpos 94
            xsize 746
            draggable True
            scrollbars "horizontal"
            for chapter in menudata:
                vbox:
                    button:
                        xysize (tabwidth,backbutton_height)
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
                        xsize (tabwidth+25)
                        draggable True
                        mousewheel True
                        scrollbars "vertical"
                        vscrollbar_unscrollable "hide"
                        for quest in chapter['quests']:
                            button:
                                xysize (tabwidth,backbutton_height)
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
                size 25
            action Hide("quest")
        viewport:
            ypos 37
            xysize (114,443)
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
                            size 25
                        action ShowMenu("questlog", log)

        vbox:
            xpos 119
            xsize 720
            button:
                xysize (tabwidth,backbutton_height)
                xanchor 0.5
                xpos 350
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
                xsize 720
                draggable True
                mousewheel True
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"

                $rows = -(len(data['scenes']) // -2)
                grid 2 rows:
                    for scene in data['scenes']:
                        button:
                            xysize (350,pageheight)
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
                size 25
            action Hide("questlog")
        viewport:
            xpos 119
            xsize 680
            draggable True
            mousewheel True
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            button:
                background Frame("bookpage", 35, 35)
                xysize(650,None)
                left_padding 20
                right_padding 40
                text "[fulltext]":
                    yalign 0.2
                    text_align 0
                    size logtextsize
