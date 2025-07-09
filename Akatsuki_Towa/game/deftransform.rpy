label deftransform:

### General Screen Transitions:
########################################
### used as a transition to shake the screen
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

### used as the transition to fade from the scene select menu to a cutscene
define fade_in = Fade(0,0,0.5)

### Portrait Transforms:
#######################################
### used to shake the portrait in place

transform l_shake:
    pause .1
    ease .1 xoffset -20
    ease .1 xoffset 20
    ease .05 xoffset -10
    ease .05 xoffset 10
    ease .05 xoffset 0


transform r_shake:
    pause .1
    ease .1 xoffset 20
    ease .1 xoffset -20
    ease .05 xoffset 10
    ease .05 xoffset -10
    ease .05 xoffset 0

#####################################################################
### used to light up the speaking portrait

transform light():
    yalign 1.0
    matrixcolor TintMatrix("#fff")
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)

#used to darken the non-speaking portrait
transform dark():
    yalign 1.0
    matrixcolor TintMatrix("#808080")
    zoom (1.0 if not renpy.variant('touch') else touch_portrait_scale)

#####################################################################
### used to flip the portrait on the left side of the screen

transform flip():
    xzoom -1.0

#####################################################################
### used for positioning
### charpos is the portrait's "_xPostion" value from avg_role.json 

transform r(charpos):
    xanchor 0.5
    xpos (680 + charpos)

transform l(charpos):
    xanchor 0.5
    xpos (160 - charpos)

### doesn't seem like xoffset is taken into account for center placement
transform mid(charpos):
    xanchor 0.5
    xpos 460

#####################################################################
### used for the animation where the portrait moves to the middle of the screen and returns starting position
### charpos is the portrait's "_xPostion" value from avg_role.json 

transform r_midback(charpos):
    xanchor 0.5
    xpos (680 + charpos)
    linear 0.1 xpos 0.40
    ease .1 xpos 0.45
    pause 0.5
    ease 0.5 xpos (680 + charpos)

transform l_midback(charpos):
    xanchor 0.5
    xpos (160 - charpos)
    linear 0.1 xpos 0.60
    ease .1 xpos 0.55
    pause 0.5
    ease 0.5 xpos (160 - charpos)


#####################################################################
### used to move the portrait in from offscreen
### charpos is the portrait's "_xPostion" value from avg_role.json 

transform r_entrance(charpos):
    xanchor 0.5
    xpos 1.50
    pause 0.1
    ease 0.5 xpos (680 + charpos)

transform l_entrance(charpos):
    xanchor 0.5
    xpos -0.50
    pause 0.1
    ease 0.5 xpos (160 - charpos)


#####################################################################
### there is ONE scene where entrance and midback are used at the same time

transform r_entrance_midback(charpos):
    xanchor 0.5
    xpos 1.50
    pause 0.1
    ease 0.5 xpos (680 + charpos)
    linear 0.1 xpos 0.40
    ease .1 xpos 0.45
    pause 0.5
    ease 0.5 xpos (680 + charpos)

transform l_entrance_midback(charpos):
    xanchor 0.5
    xpos -0.50
    pause 0.1
    ease 0.5 xpos (160 - charpos)
    linear 0.1 xpos 0.60
    ease .1 xpos 0.55
    pause 0.5
    ease 0.5 xpos (160 - charpos)


#####################################################################
### used to move portraits off screen
### charpos is the portrait's "_xPostion" value from avg_role.json 

transform r_exit(charpos):
    xanchor 0.5
    xpos (680 + charpos)
    pause 0.5
    ease .5 xpos 1.50

transform l_exit(charpos):
    xanchor 0.5
    xpos (160 - charpos)
    pause 0.5
    ease .5 xpos -0.50


#####################################################################
### there is ONE scene where midback and exit are used at the same time

transform r_exit_midback(charpos):
    xanchor 0.5
    xpos (680 + charpos)
    linear 0.1 xpos 0.40
    ease .1 xpos 0.45
    pause 0.5
    ease 0.5 xpos (680 + charpos)
    pause 0.5
    ease .5 xpos 1.50

transform l_exit_midback(charpos):
    xanchor 0.5
    xpos (160 - charpos)
    linear 0.1 xpos 0.60
    ease .1 xpos 0.55
    pause 0.5
    ease 0.5 xpos (160 - charpos)
    pause 0.5
    ease .5 xpos -0.50

#####################################################################
### midpos placeholder transforms
### there are references to them in cutscene files but they do not do anything

#placeholder so it doesn't crash 
#(these effects shouldn't be used on mid position hopefully)
transform mid_entrance(charpos):
    xanchor 0.5
    xpos 460

#placeholder so it doesn't crash
transform mid_exit(charpos):
    xanchor 0.5
    xpos 460

#placeholder so it doesn't crash
transform mid_midback(charpos):
    xanchor 0.5
    xpos 460

return