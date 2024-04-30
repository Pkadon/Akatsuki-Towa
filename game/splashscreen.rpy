
###Splash Screen Image Definitions######################################
image akatsuki_logo:
    Crop((8,1155,1304,216), "atlas_login.png")
    zoom 0.60
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
    play music "ed9999.ogg"
    scene splashscreen
    show akatsuki_logo:
        ycenter 0.54
        xcenter 0.84
    show startbuttonani:
        ycenter 0.74
        xcenter 0.72
    $ renpy.pause ()
    play sound "common_select.ogg"
    hide startbuttonani
    show startbuttonclicked:
        ycenter 0.74
        xcenter 0.72
    pause(2.0)
return