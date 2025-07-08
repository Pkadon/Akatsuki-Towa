label avg101525:
stop music

scene placeholderbackground
show sc007_01 6 as p15 at l(-17), light, flip, zorder 6
window show
with fade_out
c151 '[textdict[1221331]]'
hide p15
show sc007_01 6 as p15 at l(-17), dark, flip, zorder 6
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1221332]]'
hide p15
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc007_01 1 as p15 at l(-17), light, flip, zorder 6
c151 '[textdict[1221333]]'
hide p1
hide p15
show sc007_01 1 as p15 at l(-17), dark, flip, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1221334]]'
menu:
    extend ""
    "[textdict[1221335]]":
        call avg101526
    "[textdict[1221336]]":
        call avg101527
    "[textdict[1221337]]":
        call avg101528
return