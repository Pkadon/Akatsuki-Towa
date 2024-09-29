screen questlog(logtext):
    default fulltext = ''
    default prefix = ''
    python:
        if logtext[0] == 1: prefix = logmain + ' '
        elif logtext[0] == 2: prefix = logsub + ' '

        fulltext += prefix + textdict[logtext[1]] + '\n'
        fulltext += loglevel + ' ' + str(logtext[2]) + '\n'
        fulltext += logclient + ' ' + textdict[logtext[3]] + '\n'
        fulltext += logdetails + ' ' + textdict[logtext[4]] + '\n'
        
        for step in logtext[5:]:
            fulltext += ' ' + logbullet + ' ' + textdict[step] + '\n'
        
    modal True
    window:
        xysize (840,480)
        background "sceneselect"
        button:
            xysize(94,37)
            background Frame("backbutton", 16, 16)
            text "Back":
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
return