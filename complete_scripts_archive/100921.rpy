label avg100921:
stop music

scene placeholderbackground
show sc001_01 2 as p9 at l(-11), light, flip, zorder 6
window show
with fade_out
c91 '[textdict[1218074]]'
hide p9
show sc001_01 2 as p9 at l(-11), dark, flip, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
play sfxvoice "bcv_oc002_get_02.ogg"
c13 '[textdict[1218075]]'
hide p9
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc001_01 1 as p9 at l(-11), light, flip, zorder 6
c91 '[textdict[1218076]]'
hide p1
hide p9
show sc001_01 1 as p9 at l(-11), dark, flip, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
play sfxvoice "bcv_oc002_get_02.ogg"
c13 '[textdict[1218077]]'
hide p9
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc001_01 4 as p9 at l(-11), light, flip, zorder 6
c91 '[textdict[1218078]]'
hide p1
hide p9
show sc001_01 4 as p9 at l(-11), dark, flip, zorder 6
show oc001_01 18 as p1 at r(-2), light, zorder 5
play sfxvoice "bcv_oc002_arts_02.ogg"
c13 '[textdict[1218079]]'
menu:
    extend ""
    "[textdict[1218080]]":
        call avg100922
    "[textdict[1218081]]":
        call avg100923
    "[textdict[1218082]]":
        call avg100924
return