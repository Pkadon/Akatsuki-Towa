label avg101504:
stop music

scene placeholderbackground
with fade
show sc007_01 2 as p15 at l(-17), light, zorder 6
c151 '[textdict[1221271]]'
hide p15
show sc007_01 2 as p15 at l(-17), dark, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1221272]]'
hide p15
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc007_01 1 as p15 at l(-17), light, zorder 6
c151 '[textdict[1221273]]'
menu:
    extend ""
    "[textdict[1221274]]":
        call avg101505
    "[textdict[1221275]]":
        call avg101506
    "[textdict[1221276]]":
        call avg101507
return