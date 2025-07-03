label avg100904:
stop music

stop music
scene placeholderbackground
with fade
show sc001_01 4 as p9 at l(-11), light, zorder 5
c91 '[textdict[1218021]]'
stop music
hide p9
show sc001_01 2 as p9 at l(-11), light, zorder 5
c91 '[textdict[1218022]]'
stop music
play sfxvoice "avg_vocal_na02.ogg"
hide p9
show sc001_01 2 as p9 at l(-11), dark, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218023]]'
stop music
hide p9
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc001_01 1 as p9 at l(-11), light, zorder 5
c91 '[textdict[1218024]]'
menu:
    extend ""
    "[textdict[1218025]]":
        call avg100905
    "[textdict[1218026]]":
        call avg100906
    "[textdict[1218026]]":
        call avg100907
return