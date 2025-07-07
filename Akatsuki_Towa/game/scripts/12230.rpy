label avg12230:
stop music

play music "ed7105.ogg"
scene avg_bg_023
with fade
c6891 '[textdict[1121103]]'
show oc001_01 1 as p1 at r(-2), light, zorder 5
play sfxvoice "avg_vocal_na15.ogg"
c13 '[textdict[1121104]]'
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
c6891 '[textdict[1121105]]'
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc030_01 4 as p38 at l(-12), light, zorder 6
c381 '[textdict[1121106]]'
hide p38
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc031_01 2 as p39 at l(-14), light, zorder 6
c391 '[textdict[1121107]]'
hide p39
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc032_01 5 as p40 at l(-17), light, zorder 6
c401 '[textdict[1121108]]'
hide p1
hide p40
show sc032_01 5 as p40 at l(-17), dark, zorder 6
show oc002_01 2 as p2 at r(-3), light, zorder 5
c23 '[textdict[1121109]]'
hide p40
hide p2
show oc002_01 2 as p2 at r(-3), dark, zorder 5
c6891 '[textdict[1121110]]'
hide p2
show oc001_01 18 as p1 at r(-2), light, zorder 5
c13 '[textdict[1121111]]'
hide p1
show oc001_01 18 as p1 at r(-2), dark, zorder 5
show sc030_01 2 as p38 at l(-12), light, zorder 6
c381 '[textdict[1121112]]'
menu:
    extend ""
    "[textdict[1121113]]":
        call avg12231
    "[textdict[1121114]]":
        call avg12232
return