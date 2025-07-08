label avg101704:
stop music

scene placeholderbackground
show sc009_01 1 as p17 at l(-13), light, flip, zorder 6
window show
with fade_in
c171 '[textdict[1221883]]'
hide p17
show sc009_01 1 as p17 at l(-13), dark, flip, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1221884]]'
hide p17
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc009_01 1 as p17 at l(-13), light, flip, zorder 6
c171 '[textdict[1221885]]'
hide p1
hide p17
show sc009_01 1 as p17 at l(-13), dark, flip, zorder 6
show oc001_01 12 as p1 at r(-2), light, zorder 5
c13 '[textdict[1221886]]'
menu:
    extend ""
    "[textdict[1221887]]":
        call avg101705
    "[textdict[1221888]]":
        call avg101706
    "[textdict[1221889]]":
        call avg101707
return