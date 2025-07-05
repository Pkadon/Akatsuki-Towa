label avg19107:
stop music

play music "ed7150.ogg"
scene avg_bg_071
with fade
play sfxvoice "avg_vocal_na02.ogg"
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218031]]' (what_size=(gui.text_size*0.9))
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc001_01 1 as p9 at l(-11), light, zorder 6
c91 '[textdict[1218032]]' (what_size=(gui.text_size*0.9))
play sfxvoice "avg_vocal_na21.ogg"
hide p1
hide p9
show sc001_01 1 as p9 at l(-11), dark, zorder 6
show oc001_01 12 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218033]]' (what_size=(gui.text_size*0.9))
hide p9
hide p1
show oc001_01 12 as p1 at r(-2), dark, zorder 5
show sc001_01 1 as p9 at l(-11), light, zorder 6
c91 '[textdict[1218034]]' (what_size=(gui.text_size*0.9))
hide p9
hide p1
show oc001_01 12 as p1 at r(-2), dark, zorder 5
show sc001_01 5 as p9 at l(-11), light, zorder 6
c91 '[textdict[1218035]]' (what_size=(gui.text_size*0.9))
play sfxvoice "avg_vocal_na02.ogg"
hide p1
hide p9
show sc001_01 5 as p9 at l(-11), dark, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218036]]' (what_size=(gui.text_size*0.9))
menu:
    extend ""
    "[textdict[1218037]]":
        call avg19108
    "[textdict[1218038]]":
        call avg19109
    "[textdict[1218039]]":
        call avg19110
return