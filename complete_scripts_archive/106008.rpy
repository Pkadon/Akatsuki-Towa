label avg106008:
stop music

scene placeholderbackground
show oc001_01 16 as p1 at r(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1219067]]'
hide p1
show oc001_01 16 as p1 at r(-2), dark, zorder 5
show sc053_01 1 as p60 at l(-32), light, zorder 6
c601 '[textdict[1219068]]'
hide p1
hide p60
show sc053_01 1 as p60 at l(-32), dark, zorder 6
show oc001_01 12 as p1 at r(-2), light, zorder 5
c13 '[textdict[1219069]]'
hide p60
hide p1
show oc001_01 12 as p1 at r(-2), dark, zorder 5
show sc053_01 5 as p60 at l(-32), light, zorder 6
c601 '[textdict[1219070]]'
menu:
    extend ""
    "[textdict[1219071]]":
        call avg106009
    "[textdict[1219072]]":
        call avg106010
    "[textdict[1219073]]":
        call avg106011
return