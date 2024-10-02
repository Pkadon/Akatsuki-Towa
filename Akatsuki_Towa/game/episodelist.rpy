init python:
    def convertstrid(text):
        if isinstance(text, int): 
            return textdict[text]
        else: 
            return text

screen episodelist(data):
    default chaptername = ''
    default questname = ''
    window:
        xysize (840,480)
        background "sceneselect"
        button:
            xysize(94,37)
            background Frame("backbutton", 16, 16)
            text backtext:
                align (0.5, 1.0)
                size 25
            action Hide("episodelist")
        button:
            xysize(94,37)
            ypos 37
            background Frame("backbutton", 16, 16)
            text jumptext:
                align (0.5, 1.0)
                size 25
            action Replay("codeinput", locked=False)
        button:
            xysize(94,37)
            ypos 74
            background Frame("backbutton", 16, 16)
            text spritetext:
                align (0.5, 1.0)
                size 25
            action Replay("spritetest", locked=False)
        viewport:
            xpos 94
            xsize 740
            draggable True
            scrollbars "horizontal"
            hbox:
                for chapter in data:
                    vbox:
                        button:
                            xysize (tabwidth,37)
                            xpos 2
                            background Frame("booktab1")
                            bottom_padding 4
                            $chaptername = convertstrid(chapter['chaptername'])
                            text chaptername:
                                xalign (0.5)
                                ypos -2
                                size tabtextsize
                        viewport:
                            xsize (tabwidth+25)
                            ysize 0.96
                            draggable True
                            mousewheel True
                            scrollbars "vertical"
                            vscrollbar_unscrollable "hide"
                            vbox:
                                for quest in chapter['quests']:
                                    button:
                                        xysize (tabwidth,37)
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
            xysize(94,37)
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
                        xysize(94,37)
                        background Frame("backbutton", 16, 16)
                        text "[logtext] [lognumber]":
                            align (0.5,1.0)
                            size 25
                        action ShowMenu("questlog", log)
        viewport:
            xpos 119
            xsize 720
            draggable True
            mousewheel True
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            vbox:
                xsize 700
                button:
                    xysize (tabwidth,37)
                    xalign 0.5
                    background Frame("booktab2")
                    bottom_padding 4

                    python:
                        questname = convertstrid(data['questname'])
                        if data['add']: questname += data['add']

                    text questname:
                        xalign (0.5)
                        ypos -2
                        size tabtextsize

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
                                scenename = convertstrid(scene['scenename'])
                                if scene['add']: scenename += scene['add']
                                if scene['sceneinfo']: scenename += '\n' + convertstrid(scene['sceneinfo'])

                            text scenename:
                                align (0.5,0.5)
                                text_align 0.5
                                size pagetextsize

screen questlog(data):
    default fulltext = ''
    default prefix = ''
    python:
        if data['type'] == 1: prefix = logmain + ' '
        elif data['type'] == 2: prefix = logsub + ' '

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
            xysize(94,37)
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
