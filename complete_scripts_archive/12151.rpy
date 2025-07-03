label avg12151:
stop music

play music "ED6505.ogg"
scene avg_bg_027
with fade
play sfx2 "other_7060.ogg"
show uc004_02 1 as p960 at l(-9), light, zorder 5
c9601 '[textdict[1128367]]'
hide p960
show uc004_02 1 as p960 at l(-9), dark, zorder 6
show uc004_02 2 as p961 at r(-9), light, zorder 5
c9613 '[textdict[1128368]]'
hide p961
hide p960
show uc004_02 1 as p960 at l(-9), dark, zorder 6
show oc001_01 1 as p1 at r_entrance(-2), light, zorder 5
c13 '[textdict[1128369]]'
hide p1
hide p960
show uc004_02 1 as p960 at l(-9), dark, zorder 6
show oc002_01 2 as p2 at r(-3), light, zorder 5
c23 '[textdict[1128370]]'
hide p960
hide p2
show oc002_01 2 as p2 at r(-3), dark, zorder 5
show uc004_02 1 as p960 at l(-9), light, zorder 5
c9601 '[textdict[1128371]]'
play music "ED6107.ogg"
scene avg_bg_070
with fade
play sfx2 "other_7021.ogg"
c0 '[textdict[1128373]]'
scene avg_bg_038
with fade
c9621 '[textdict[1128374]]'
c9621 '[textdict[1128375]]'
show oc002_01 2 as p2 at r(-3), light, zorder 5
c23 '[textdict[1128376]]'
hide p2
show oc002_01 2 as p2 at r(-3), dark, zorder 5
c9621 '[textdict[1128377]]'
hide p2
show oc002_01 2 as p2 at r(-3), dark, zorder 5
c9621 '[textdict[1128378]]'
menu:
    extend ""
    "[textdict[1100001]]":
        call avg12154
    "[textdict[1100002]]":
        call avg12153
return