label avg19016:
stop music

scene avg_bg_023
show oc002_01 4 as p2 at r(-3), light, zorder 5
with fade
c23 '[textdict[1216147]]' (what_size=(gui.text_size*0.9))
hide p2
show oc002_01 4 as p2 at r(-3), dark, zorder 5
show sc049_01 5 as p56 at l(-8), light, zorder 6
c561 '[textdict[1216148]]' (what_size=(gui.text_size*0.9))
hide p2
hide p56
show sc049_01 5 as p56 at l(-8), dark, zorder 6
show oc001_01 8 as p1 at r(-2), light, zorder 5
c13 '[textdict[1216149]]' (what_size=(gui.text_size*0.9))
hide p56
hide p1
show oc001_01 8 as p1 at r(-2), dark, zorder 5
show sc049_01 1 as p56 at l(-8), light, zorder 6
c561 '[textdict[1216158]]' (what_size=(gui.text_size*0.9))
hide p56
hide p1
show oc001_01 8 as p1 at r(-2), dark, zorder 5
show sc049_01 1 as p56 at l(-8), light, zorder 6
c561 '[textdict[1216159]]' (what_size=(gui.text_size*0.9))
hide p56
hide p1
show oc001_01 8 as p1 at r(-2), dark, zorder 5
show sc049_01 1 as p56 at l(-8), light, zorder 6
c561 '[textdict[1216160]]' (what_size=(gui.text_size*0.9))
hide p56
hide p1
c0 '[textdict[1216161]]' (what_size=(gui.text_size*0.9))
menu:
    extend ""
    "[textdict[1216162]]":
        call avg19017
    "[textdict[1216163]]":
        call avg19018
    "[textdict[1216164]]":
        call avg19019
return