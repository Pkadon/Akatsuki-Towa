label avg19103:
stop music

play music "ed7150.ogg"
scene avg_bg_071
with fade
show sc001_01 4 as p9 at l(-11), light, zorder 6
c91 '[textdict[1218020]]'
hide p9
show sc001_01 1 as p9 at l(-11), light, zorder 6
c91 '[textdict[1218021]]'
play sfxvoice "avg_vocal_na02.ogg"
hide p9
show sc001_01 1 as p9 at l(-11), dark, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218022]]'
hide p9
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc001_01 4 as p9 at l(-11), light, zorder 6
c91 '[textdict[1218023]]'
menu:
    extend ""
    "[textdict[1218024]]":
        call avg19104
    "[textdict[1218025]]":
        call avg19105
    "[textdict[1218026]]":
        call avg19106
return