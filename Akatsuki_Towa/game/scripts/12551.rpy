label avg12551:
stop music

play music "ED6103.ogg"
scene avg_bg_023
with fade
c00 '[textdict[1153001]]'
c00 '[textdict[1153002]]'
show oc002_01 2 as c2portrait at leftside(-3), zorder 5
c21 '[textdict[1153003]]'
hide c2portrait
show oc002_01 2 as c2portrait at darkleft(-3), zorder 6
show oc001_01 10 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1153004]]'
hide c2portrait
hide c1portrait
show oc001_01 10 as c1portrait at darkright(-2), zorder 5
show oc002_01 8 as c2portrait at leftside(-3), zorder 5
c21 '[textdict[1153005]]'
play sfxvoice "avg_vocal_ro05.ogg"
hide c2portrait
hide c1portrait
show oc001_01 10 as c1portrait at darkright(-2), zorder 5
show oc003_01 5 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[1153006]]'
hide c1portrait
hide c3portrait
show oc003_01 5 as c3portrait at darkleft(-6), zorder 6
show oc004_01 4 as c4portrait at rightside(-5), zorder 5
c43 '[textdict[1153007]]'
hide c4portrait
hide c3portrait
show oc003_01 5 as c3portrait at darkleft(-6), zorder 6
show oc004_01 4 as c4portrait at rightside(-5), zorder 5
c43 '[textdict[1153008]]'
hide c3portrait
hide c4portrait
c00 '[textdict[1153009]]'
return