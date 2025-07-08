label avg103025:
stop music

scene placeholderbackground
show sc022_01 1 as p30 at l(-9), light, flip, zorder 6
window show
with fade_out
c301 '[textdict[1222484]]'
hide p30
show sc022_01 1 as p30 at l(-9), dark, flip, zorder 6
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1222485]]'
hide p30
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc022_01 1 as p30 at l(-9), light, flip, zorder 6
c301 '[textdict[1222486]]'
menu:
    extend ""
    "[textdict[1222487]]":
        call avg103026
    "[textdict[1222488]]":
        call avg103027
    "[textdict[1222489]]":
        call avg103028
return