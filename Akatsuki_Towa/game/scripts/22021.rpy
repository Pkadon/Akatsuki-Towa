label avg22021:
stop music

play music "ed7105.ogg"
scene placeholderbackground
with fade
show sc049_01 5 as c56portrait at centerpos(-8), zorder 5
c563 '[textdict[1120002]]'
hide c56portrait
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1120003]]'
play sfx2 "other_7091.ogg"
hide c1portrait
show sc049_01 1 as c56portrait at centerpos(-8), zorder 5
c563 '[textdict[1120004]]'
hide c56portrait
show sc050_01 1 as c57portrait at centerpos(-19), zorder 5
c573 '[textdict[1120005]]'
hide c57portrait
show sc052_01 5 as c59portrait at centerpos(-25), zorder 5
c593 '[textdict[1120006]]'
hide c59portrait
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1120007]]'
menu:
    extend ""
    "[textdict[1120008]]":
        call avg22022
    "[textdict[1120009]]":
        call avg22023
return