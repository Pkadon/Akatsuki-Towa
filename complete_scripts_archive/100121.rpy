label avg100121:
stop music

stop music
scene placeholderbackground
with fade
show sc001_01 2 as p9 at l(-11), light, zorder 5
c91 '[textdict[1218074]]'
stop music
play sfxvoice "bcv_oc002_get_02.ogg"
hide p9
show sc001_01 2 as p9 at l(-11), dark, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218075]]'
stop music
hide p9
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc001_01 1 as p9 at l(-11), light, zorder 5
c91 '[textdict[1218076]]'
stop music
play sfxvoice "bcv_oc002_get_02.ogg"
hide p1
hide p9
show sc001_01 1 as p9 at l(-11), dark, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218077]]'
stop music
hide p9
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc001_01 4 as p9 at l(-11), light, zorder 5
c91 '[textdict[1218078]]'
stop music
play sfxvoice "bcv_oc002_arts_02.ogg"
hide p1
hide p9
show sc001_01 4 as p9 at l(-11), dark, zorder 6
show oc001_01 18 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218079]]'
menu:
    extend ""
    "[textdict[1218080]]":
        call avg100122
    "[textdict[1218081]]":
        call avg100123
    "[textdict[1218082]]":
        call avg100124
return