label avg10336:
stop music

play music "ed7105.ogg"
scene avg_bg_003
show oc004_01 2 as p4 at l(-5), light, zorder 6
with fade
c41 '[textdict[1130999]]'
hide p4
show oc004_01 2 as p4 at l(-5), dark, zorder 6
show oc001_01 11 as p1 at r(-2), light, zorder 5
c13 '[textdict[1131024]]'
hide p1
hide p4
show oc004_01 2 as p4 at l(-5), dark, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1131025]]'
hide p4
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show oc002_01 2 as p2 at l(-3), light, zorder 6
c21 '[textdict[1131026]]'
hide p2
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show oc004_01 2 as p4 at l(-5), light, zorder 6
c41 '[textdict[1131027]]'
hide p4
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show oc003_01 6 as p3 at l(-6), light, zorder 6
c31 '[textdict[1131028]]'
hide p1
hide p3
show oc003_01 6 as p3 at l(-6), dark, zorder 6
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1131029]]'
menu:
    extend ""
    "[textdict[1131030]]":
        call avg10338
    "[textdict[1131031]]":
        call avg10339
return