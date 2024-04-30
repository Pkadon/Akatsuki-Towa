label deftransform:

###general transforms###############################################

###Used to shake the screen
###copied from here: https://www.renpy.org/wiki/renpy/doc/cookbook/Shake_effect
init:
    python:

        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #

#

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


transform leftside(charpos):
    xanchor 0.5
    xzoom -1.0
    matrixcolor TintMatrix("#fff")
    xpos (160 - charpos)

###doesn't seem like xoffset is taken into account for center placement
transform centerpos(charpos):
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos 460


####################################
###used for the animation where the portrait moves to the middle of the screen and returns starting position
###charpos is the portrait's "_xPostion" value from avg_role.json 

transform rightsidemidback(charpos):
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos (680 + charpos)
    linear 0.1 xpos 0.40
    ease .1 xpos 0.45
    pause 0.5
    ease 0.5 xpos (680 + charpos)

transform leftsidemidback(charpos):
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
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos 1.50
    pause 0.1
    ease 0.5 xpos (680 + charpos)

transform leftsideentrance(charpos):
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
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos (680 + charpos)
    pause 0.5
    ease .5 xpos 1.50

transform leftsideexit(charpos):
    xanchor 0.5
    xzoom -1.0
    matrixcolor TintMatrix("#fff")
    xpos (160 - charpos)
    pause 0.5
    ease .5 xpos -0.50


####################################
###there is ONE scene where midback and exit are used at the same time

transform rightsideexitmidback(charpos):
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

transform darkleft(charpos): 
    xanchor 0.5
    xzoom -1.0
    xpos (160 - charpos)
    matrixcolor TintMatrix("#808080")


####################################
###midpos placeholder transforms
###there are references to them in cutscene files but they do not do anything

#placeholder so it doesn't crash 
#(these effects shouldn't be used on centerpos hopefully)
transform centerposentrance(charpos):
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos 460

#placeholder so it doesn't crash
transform centerposexit(charpos):
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos 460

#placeholder so it doesn't crash
transform centerposmidback(charpos):
    xanchor 0.5
    xzoom 1.0
    matrixcolor TintMatrix("#fff")
    xpos 460

return