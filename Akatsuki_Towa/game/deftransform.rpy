label deftransform:

###general transforms###############################################


########################################
###used as a transition to shake the screen
transform shake(*, new_widget=None, old_widget=None):
    delay .3
    xcenter .5
    ycenter .5

    new_widget
    events True
    linear .025 rotate 15
    linear .025 rotate -12
    linear .03 rotate 10
    linear .03 rotate -8
    linear .04 rotate 6
    linear .04 rotate -5
    linear .03 rotate 4
    linear .03 rotate -3
    linear .025 rotate 2
    ease .025 rotate 0

#######################################
###used to shake the portrait in place

transform shakeleft:
    pause .1
    ease .1 xoffset -20
    ease .1 xoffset 20
    ease .05 xoffset -10
    ease .05 xoffset 10
    ease .05 xoffset 0


transform shakeright:
    pause .1
    ease .1 xoffset 20
    ease .1 xoffset -20
    ease .05 xoffset 10
    ease .05 xoffset -10
    ease .05 xoffset 0

####################################
###used for positioning
###charpos is the portrait's "_xPostion" value from avg_role.json 

transform rightside(charpos):
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos (680 + charpos)
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)

transform leftside(charpos):
    xanchor 0.5
    xzoom -1.0
    matrixcolor TintMatrix("#fff")
    xpos (160 - charpos)
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)

###doesn't seem like xoffset is taken into account for center placement
transform centerpos(charpos):
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos 460
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)


####################################
###used for the animation where the portrait moves to the middle of the screen and returns starting position
###charpos is the portrait's "_xPostion" value from avg_role.json 

transform rightsidemidback(charpos):
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos (680 + charpos)
    linear 0.1 xpos 0.40
    ease .1 xpos 0.45
    pause 0.5
    ease 0.5 xpos (680 + charpos)

transform leftsidemidback(charpos):
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)
    xanchor 0.5
    xzoom -1.0
    matrixcolor TintMatrix("#fff")
    xpos (160 - charpos)
    linear 0.1 xpos 0.60
    ease .1 xpos 0.55
    pause 0.5
    ease 0.5 xpos (160 - charpos)


####################################
###used to move the portrait in from offscreen
###charpos is the portrait's "_xPostion" value from avg_role.json 

transform rightsideentrance(charpos):
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos 1.50
    pause 0.1
    ease 0.5 xpos (680 + charpos)

transform leftsideentrance(charpos):
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)
    xanchor 0.5
    xzoom -1.0
    matrixcolor TintMatrix("#fff")
    xpos -0.50
    xzoom -1.0
    pause 0.1
    ease 0.5 xpos (160 - charpos)


############################
###there is ONE scene where entrance and midback are used at the same time

transform rightsideentrancemidback(charpos):
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos 1.50
    pause 0.1
    ease 0.5 xpos (680 + charpos)
    linear 0.1 xpos 0.40
    ease .1 xpos 0.45
    pause 0.5
    ease 0.5 xpos (680 + charpos)

transform leftsideentrancemidback(charpos):
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)
    xanchor 0.5
    xzoom -1.0
    matrixcolor TintMatrix("#fff")
    xpos -0.50
    xzoom -1.0
    pause 0.1
    ease 0.5 xpos (160 - charpos)
    linear 0.1 xpos 0.60
    ease .1 xpos 0.55
    pause 0.5
    ease 0.5 xpos (160 - charpos)


####################################
###used to move portraits off screen
###charpos is the portrait's "_xPostion" value from avg_role.json 

transform rightsideexit(charpos):
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos (680 + charpos)
    pause 0.5
    ease .5 xpos 1.50

transform leftsideexit(charpos):
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)
    xanchor 0.5
    xzoom -1.0
    matrixcolor TintMatrix("#fff")
    xpos (160 - charpos)
    pause 0.5
    ease .5 xpos -0.50


####################################
###there is ONE scene where midback and exit are used at the same time

transform rightsideexitmidback(charpos):
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos (680 + charpos)
    linear 0.1 xpos 0.40
    ease .1 xpos 0.45
    pause 0.5
    ease 0.5 xpos (680 + charpos)
    pause 0.5
    ease .5 xpos 1.50

transform leftsideexitmidback(charpos):
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)
    xanchor 0.5
    xzoom -1.0
    matrixcolor TintMatrix("#fff")
    xpos (160 - charpos)
    linear 0.1 xpos 0.60
    ease .1 xpos 0.55
    pause 0.5
    ease 0.5 xpos (160 - charpos)
    pause 0.5
    ease .5 xpos -0.50


####################################
###used to darken the non-speaking portrait onscreen
###charpos is the portrait's "_xPostion" value from avg_role.json 

transform darkright(charpos): 
    xanchor 0.5
    xzoom 1.0
    xpos (680 + charpos)
    matrixcolor TintMatrix("#808080")
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)

transform darkleft(charpos): 
    xanchor 0.5
    xzoom -1.0
    xpos (160 - charpos)
    matrixcolor TintMatrix("#808080")
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)


####################################
###midpos placeholder transforms
###there are references to them in cutscene files but they do not do anything

#placeholder so it doesn't crash 
#(these effects shouldn't be used on centerpos hopefully)
transform centerposentrance(charpos):
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos 460

#placeholder so it doesn't crash
transform centerposexit(charpos):
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos 460

#placeholder so it doesn't crash
transform centerposmidback(charpos):
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos 460

return