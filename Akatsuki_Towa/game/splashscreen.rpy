
###Splash Screen Image Definitions######################################

#akatsukilogo is defined in CONFIG.rpy

image startbutton:
    Crop((747,1990,175,48), "atlas_login.png")
image startbutton2:
    Crop((756,1994,166,44), "atlas_login.png")
    alpha 0
image startbuttonani:
    "startbutton" with Dissolve(0.5, alpha=True)
    alpha 1.0
    zoom 0.65
    pause 1.0
    "startbutton" with Dissolve(0.5, alpha=True)
    alpha .9
    zoom 0.65
    pause .05
    "startbutton" with Dissolve(0.5, alpha=True)
    alpha .8
    zoom 0.65
    pause .05
    "startbutton" with Dissolve(0.5, alpha=True)
    alpha .7
    zoom 0.65
    pause .05
    "startbutton" with Dissolve(0.5, alpha=True)
    alpha .6
    zoom 0.65
    pause .05
    "startbutton" with Dissolve(0.5, alpha=True)
    alpha .5
    zoom 0.65
    pause .05
    "startbutton" with Dissolve(0.5, alpha=True)
    alpha .4
    zoom 0.65
    pause .05
    "startbutton" with Dissolve(0.5, alpha=True)
    alpha .3
    zoom 0.65
    pause .05
    "startbutton" with Dissolve(0.5, alpha=True)
    alpha .2
    zoom 0.65
    pause .05
    "startbutton" with Dissolve(0.5, alpha=True)
    alpha .1
    zoom 0.65
    pause .05
    "startbutton2" with Dissolve(0.5, alpha=True)
    alpha 0
    zoom 0.65
    pause 1.0
    repeat
image startbuttonclicked:
    "startbutton" with Dissolve(0.25, alpha=True)
    alpha 1.0
    zoom 0.65
    pause .1
    "startbutton" with Dissolve(0.25, alpha=True)
    alpha .9
    zoom 0.65
    pause .025
    "startbutton" with Dissolve(0.25, alpha=True)
    alpha .8
    zoom 0.65
    pause .025
    "startbutton" with Dissolve(0.25, alpha=True)
    alpha .7
    zoom 0.65
    pause .025
    "startbutton" with Dissolve(0.25, alpha=True)
    alpha .6
    zoom 0.65
    pause .025
    "startbutton" with Dissolve(0.25, alpha=True)
    alpha .5
    zoom 0.65
    pause .025
    "startbutton" with Dissolve(0.25, alpha=True)
    alpha .4
    zoom 0.65
    pause .025
    "startbutton" with Dissolve(0.25, alpha=True)
    alpha .3
    zoom 0.65
    pause .025
    "startbutton" with Dissolve(0.25, alpha=True)
    alpha .2
    zoom 0.65
    pause .025
    "startbutton" with Dissolve(0.25, alpha=True)
    alpha .1
    zoom 0.65
    pause .025
    "startbutton2" with Dissolve(0.25, alpha=True)
    alpha 0
    zoom 0.65
    pause .1
    repeat

image splashscreen:
    "startbackground.png"
    xysize (840, 480)



###Splash Screen Start:######################################
label splashscreen:
    $ play_music("ed9999.ogg")
    scene splashscreen
    show splash_akatsukilogo:
        anchor splash_logo_anchor
        pos splash_logo_pos
        zoom splash_logo_zoom
    show startbuttonani:
        xcenter 0.72
        ycenter 0.74
    $ renpy.pause ()
    play sound "common_select.ogg"
    hide startbuttonani
    show startbuttonclicked:
        xcenter 0.72
        ycenter 0.74
    pause(2.0)
return