label avg100125:
stop music

stop music
scene placeholderbackground
with fade
show sc001_01 2 as p9 at mid(-11), light, zorder 5
c93 '[textdict[1218088]]'
stop music
play sfxvoice "bcv_oc002_win_02.ogg"
hide p9
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218089]]'
stop music
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc001_01 1 as p9 at l(-11), light, zorder 6
c91 '[textdict[1218090]]'
stop music
hide p9
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc001_01 5 as p9 at l(-11), light, zorder 6
c91 '[textdict[1218091]]'
stop music
play sfxvoice "bcv_oc002_win_02.ogg"
hide p1
hide p9
show sc001_01 5 as p9 at l(-11), dark, zorder 6
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218092]]'
menu:
    extend ""
    "[textdict[1218093]]":
        call avg100126
    "[textdict[1218094]]":
        call avg100127
    "[textdict[1218095]]":
        call avg100128
return