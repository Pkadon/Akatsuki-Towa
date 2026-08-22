
image chapter_banner_transparent:
    "images_free/chapter_banner.png"
    alpha .85

image prologue:
    Crop((0, 0, 515, 111), "images_free/chapter_titles.png")
    zoom 0.45

layeredimage chapter1:
    always:
        Crop((628, 0, 412, 111), "images_free/chapter_titles.png")
    always:
        Crop((1262, 0, 50, 111), "images_free/chapter_titles.png")
        xpos 447
    zoom 0.45

layeredimage chapter2:
    always:
        Crop((628, 0, 412, 111), "images_free/chapter_titles.png")
    always:
        Crop((1554, 0, 81, 111), "images_free/chapter_titles.png")
        xpos 447
    zoom 0.45

layeredimage chapter3:
    always:
        Crop((628, 0, 412, 111), "images_free/chapter_titles.png")
    always:
        Crop((1868, 0, 78, 111), "images_free/chapter_titles.png")
        xpos 447
    zoom 0.45

layeredimage chapter4:
    always:
        Crop((628, 0, 412, 111), "images_free/chapter_titles.png")
    always:
        Crop((2178, 0, 81, 111), "images_free/chapter_titles.png")
        xpos 447
    zoom 0.45

layeredimage chapter5:
    always:
        Crop((628, 0, 412, 111), "images_free/chapter_titles.png")
    always:
        Crop((2493, 0, 80, 111), "images_free/chapter_titles.png")
        xpos 447
    zoom 0.45

layeredimage chapter6:
    always:
        Crop((628, 0, 412, 111), "images_free/chapter_titles.png")
    always:
        Crop((2810, 0, 75, 111), "images_free/chapter_titles.png")
        xpos 447
    zoom 0.45

layeredimage chapter7:
    always:
        Crop((628, 0, 412, 111), "images_free/chapter_titles.png")
    always:
        Crop((3124, 0, 76, 111), "images_free/chapter_titles.png")
        xpos 447
    zoom 0.45

layeredimage chapter8:
    always:
        Crop((628, 0, 412, 111), "images_free/chapter_titles.png")
    always:
        Crop((3430, 0, 80, 111), "images_free/chapter_titles.png")
        xpos 447
    zoom 0.45

image epilogue:
    Crop((3740, 0, 475, 111), "images_free/chapter_titles.png")
    zoom 0.45

image after_future:
    Crop((4350, 0, 721, 111), "images_free/chapter_titles.png")
    zoom 0.45

transform dropin_header:
    subpixel True
    zoom 1.2
    alpha 0.0
    xoffset 100
    ease 0.25:
        zoom .95
        alpha 1.0
        xoffset 0
    linear 0.1:
        zoom 1.0

transform dropin_title:
    subpixel True
    zoom 1.2
    alpha 0.0
    xoffset -50
    pause .25
    ease 0.15:
        zoom .95
        alpha 1.0
        xoffset 0
    linear 0.1:
        zoom 1.0


transform dropin_end(trans=None):
    subpixel True
    zoom 1.2
    alpha 0.0
    yoffset -5
    pause .30
    ease 0.15:
        zoom .95
        alpha 1.0
        yoffset 0
    linear 0.1:
        zoom 1.0
        
screen chapter_bumper(chapter_image, chapter_title, ending=False):
    tag bumper
    use toggle_language()

    if renpy.loadable("bat_craft_inhale_01.ogg"):
        on "show" action Play("audio", "bat_craft_inhale_01.ogg")

    frame:
        background Frame("chapter_banner_transparent", 0, 5)
        xfill True
        ysize 125
        yalign 0.5
        add "[chapter_image]" at dropin_header:
            yanchor 1.0
            ypos 0.55
            xalign 0.40
        hbox:
            yanchor 1.0
            ypos 0.95
            xalign 0.65
            spacing 10
            text "{i}[convertstrid(chapter_title)]{/i}" at dropin_title:
                size 25
                yalign 1.0

            if ending == True:
                text "{i}[cont_chapter_end_text[preferences.language]]{/i}" at dropin_end(trans=None):
                    size 50
                    yanchor 1.0
                    ypos 1.0
                    yoffset 10

    button:
        xfill True
        yfill True
        background None
        action [Return(), Hide("chapter_bumper")]


#Templates
label chapter_start_bumper(chapter_image, chapter_title):
window hide
$quick_menu = False
show screen chapter_bumper(chapter_image, chapter_title, ending=False)
pause 15
hide screen chapter_bumper
$quick_menu = True
return

#I originally had the ending fade to black, that's why they're separate
#Maybe a better idea'll pop up later
label chapter_end_bumper(chapter_image, chapter_title):
window hide
$quick_menu = False
show screen chapter_bumper(chapter_image, chapter_title, ending=True)
pause 15
hide screen chapter_bumper
$quick_menu = True
return


#Probably won't use this intro one for the Prologue
label prologue_start(trans=None):
call chapter_start_bumper("prologue", 19501)
return
label prologue_end(trans=None):
call chapter_end_bumper("prologue", 19501)
return

label chapter1_start(trans=None):
call chapter_start_bumper("chapter1", 19502)
return
label chapter1_end(trans=None):
call chapter_end_bumper("chapter1", 19502)
return

label chapter2_start(trans=None):
call chapter_start_bumper("chapter2", 19503)
return
label chapter2_end(trans=None):
call chapter_end_bumper("chapter2", 19503)
return

label chapter3_start(trans=None):
call chapter_start_bumper("chapter3", 19504)
return
label chapter3_end(trans=None):
call chapter_end_bumper("chapter3", 19504)
return

label chapter4_start(trans=None):
call chapter_start_bumper("chapter4", 19505)
return
label chapter4_end(trans=None):
call chapter_end_bumper("chapter4", 19505)
return

label chapter5_start(trans=None):
call chapter_start_bumper("chapter5", 19506)
return
label chapter5_end(trans=None):
call chapter_end_bumper("chapter5", 19506)
return

label chapter6_start(trans=None):
call chapter_start_bumper("chapter6", 19507)
return
label chapter6_end(trans=None):
call chapter_end_bumper("chapter6", 19507)
return

label chapter7_start(trans=None):
call chapter_start_bumper("chapter7", 19508)
return
label chapter7_end(trans=None):
call chapter_end_bumper("chapter7", 19508)
return

label chapter8_start(trans=None):
call chapter_start_bumper("chapter8", 19509)
return
label chapter8_end(trans=None):
call chapter_end_bumper("chapter8", 19509)
return

label epilogue_start(trans=None):
call chapter_start_bumper("epilogue", 19510)
return
label epilogue_end(trans=None):
call chapter_end_bumper("epilogue", 19510)
return

label after_future_start(trans=None):
call chapter_start_bumper("after_future", "")
return
label after_future_end(trans=None):
call chapter_end_bumper("after_future", "")
return


#####################################################################


image animated_quest_complete:
    "complete_stamp"
    anchor (0.5,0.5)
    align (0.95, 0.95)
    alpha 0
    zoom 1.4
    yoffset -50
    linear 0.1:
        alpha 1.0
        zoom 1.2
        yoffset 0

    
label quest_complete(trans=None):
window hide
$quick_menu = False
show animated_quest_complete zorder 10
if renpy.loadable("common_stamp.ogg"):
    play audio "common_stamp.ogg"
pause 1.5
hide screen quest_complete
$quick_menu = True
return
