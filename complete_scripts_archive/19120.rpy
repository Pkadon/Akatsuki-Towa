label avg19120:
stop music

play music "ed7150.ogg"
scene avg_bg_071
show sc001_01 2 as p9 at l(-11), light, flip, zorder 6
window show
with fade_out
c91 '[textdict[1218072]]' (what_size=(gui.text_size*0.9))
hide p9
show sc001_01 2 as p9 at l(-11), dark, flip, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
play sfxvoice "bcv_oc002_get_02.ogg"
c13 '[textdict[1218073]]' (what_size=(gui.text_size*0.9))
hide p9
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc001_01 1 as p9 at l(-11), light, flip, zorder 6
c91 '[textdict[1218074]]' (what_size=(gui.text_size*0.9))
hide p1
hide p9
show sc001_01 1 as p9 at l(-11), dark, flip, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
play sfxvoice "bcv_oc002_get_02.ogg"
c13 '[textdict[1218075]]' (what_size=(gui.text_size*0.9))
hide p9
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc001_01 4 as p9 at l(-11), light, flip, zorder 6
c91 '[textdict[1218076]]' (what_size=(gui.text_size*0.9))
hide p1
hide p9
show sc001_01 4 as p9 at l(-11), dark, flip, zorder 6
show oc001_01 18 as p1 at r(-2), light, zorder 5
play sfxvoice "bcv_oc002_arts_02.ogg"
c13 '[textdict[1218077]]' (what_size=(gui.text_size*0.9))
menu:
    extend ""
    "[textdict[1218078]]":
        call avg19121
    "[textdict[1218079]]":
        call avg19122
    "[textdict[1218080]]":
        call avg19123
return