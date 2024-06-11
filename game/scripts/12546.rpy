label avg12546:
stop music

play music "ED6105.ogg"
scene avg_bg_010
with fade
play sfxvoice "bcv_oc001_hurt_01.ogg"
show oc001_01 17 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1152959]]'
hide c1portrait
show oc001_01 17 as c1portrait at darkright(-2), zorder 5
show oc002_01 10 as c2portrait at leftside(-3), zorder 5
c21 '[textdict[1152960]]'
hide c2portrait
hide c1portrait
show oc001_01 17 as c1portrait at darkright(-2), zorder 5
show oc003_01 17 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[1152961]]'
hide c1portrait
hide c3portrait
show oc003_01 17 as c3portrait at darkleft(-6), zorder 6
show oc004_01 4 as c4portrait at rightside(-5), zorder 5
c43 '[textdict[1152962]]'
return