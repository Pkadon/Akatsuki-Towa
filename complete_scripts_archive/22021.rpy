label avg22021:
stop music

play music "ed7105.ogg"
scene placeholderbackground
with fade
show sc049_01 5 as p56 at mid(-8), light, zorder 5
c563 '[textdict[1120002]]'
hide p56
show oc001_01 8 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1120003]]'
play sfx2 "other_7091.ogg"
hide p1
show sc049_01 1 as p56 at mid(-8), light, zorder 5
c563 '[textdict[1120004]]'
hide p56
show sc050_01 1 as p57 at mid(-19), light, zorder 5
c573 '[textdict[1120005]]'
hide p57
show sc052_01 5 as p59 at mid(-25), light, zorder 5
c593 '[textdict[1120006]]'
hide p59
show oc002_01 12 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1120007]]'
menu:
    extend ""
    "[textdict[1120008]]":
        call avg22022
    "[textdict[1120009]]":
        call avg22023
return