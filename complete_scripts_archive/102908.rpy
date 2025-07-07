label avg102908:
stop music

scene placeholderbackground
show oc001_01 4 as p1 at r(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1219917]]'
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show sc021_01 1 as p29 at l(-17), light, zorder 6
c291 '[textdict[1219918]]'
hide p29
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show sc021_01 1 as p29 at l(-17), light, zorder 6
c291 '[textdict[1219919]]'
menu:
    extend ""
    "[textdict[1219920]]":
        call avg102909
    "[textdict[1219921]]":
        call avg102910
    "[textdict[1219922]]":
        call avg102911
return