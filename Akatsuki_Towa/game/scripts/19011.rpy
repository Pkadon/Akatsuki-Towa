label avg19011:
stop music

scene avg_bg_023
show oc002_01 4 as p2 at r(-3), light, zorder 5
window show
with fade_out
c23 '[textdict[1216095]]' (what_size=(gui.text_size*0.9))
hide p2
show oc001_01 8 as p1 at r(-2), light, zorder 5
c13 '[textdict[1216096]]' (what_size=(gui.text_size*0.9))
hide p1
show oc002_01 1 as p2 at r(-3), light, zorder 5
c23 '[textdict[1216097]]' (what_size=(gui.text_size*0.9))
hide p2
show oc002_01 18 as p2 at r(-3), light, zorder 5
c23 '[textdict[1216098]]' (what_size=(gui.text_size*0.9))
hide p2
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1216099]]' (what_size=(gui.text_size*0.9))
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc049_01 5 as p56 at l(-8), light, zorder 6
c561 '[textdict[1216100]]' (what_size=(gui.text_size*0.9))
hide p1
hide p56
show sc049_01 5 as p56 at l(-8), dark, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1216101]]' (what_size=(gui.text_size*0.9))
hide p56
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc049_01 10 as p56 at l(-8), light, zorder 6
c561 '[textdict[1216102]]' (what_size=(gui.text_size*0.9))
hide p1
hide p56
show sc049_01 10 as p56 at l(-8), dark, zorder 6
show oc002_01 21 as p2 at r(-3), light, zorder 5
c23 '[textdict[1216103]]' (what_size=(gui.text_size*0.9))
hide p56
hide p2
c0 '[textdict[1216104]]' (what_size=(gui.text_size*0.9))
show sc049_01 1 as p56 at l(-8), light, zorder 6
c561 '[textdict[1216105]]' (what_size=(gui.text_size*0.9))
hide p56
c0 '[textdict[1216106]]' (what_size=(gui.text_size*0.9))
c0 '[textdict[1216107]]' (what_size=(gui.text_size*0.9))
menu:
    extend ""
    "[textdict[1216108]]":
        call avg19012
    "[textdict[1216109]]":
        call avg19013
    "[textdict[1216110]]":
        call avg19014
return