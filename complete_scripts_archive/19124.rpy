label avg19124:
stop music

play music "ed7150.ogg"
scene avg_bg_071
show sc001_01 2 as p9 at l(-11), light, flip, zorder 6
window show
with fade_out
c91 '[textdict[1218085]]' (what_size=(gui.text_size*0.9))
hide p9
show sc001_01 2 as p9 at l(-11), dark, flip, zorder 6
show oc001_01 1 as p1 at r(-2), light, zorder 5
play sfxvoice "bcv_oc002_win_02.ogg"
c13 '[textdict[1218086]]' (what_size=(gui.text_size*0.9))
hide p9
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc001_01 1 as p9 at l(-11), light, flip, zorder 6
c91 '[textdict[1218087]]' (what_size=(gui.text_size*0.9))
hide p9
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc001_01 5 as p9 at l(-11), light, flip, zorder 6
c91 '[textdict[1218088]]' (what_size=(gui.text_size*0.9))
hide p1
hide p9
show sc001_01 5 as p9 at l(-11), dark, flip, zorder 6
show oc001_01 1 as p1 at r(-2), light, zorder 5
play sfxvoice "bcv_oc002_win_02.ogg"
c13 '[textdict[1218089]]' (what_size=(gui.text_size*0.9))
menu:
    extend ""
    "[textdict[1218090]]":
        call avg19125
    "[textdict[1218091]]":
        call avg19126
    "[textdict[1218092]]":
        call avg19127
return