label avg12603:
stop music

play music "ED6200.ogg"
scene avg_bg_080
with fade
show oc001_01 4 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1161143)]]'
hide c1portrait
show oc001_01 4 as c1portrait at darkright(-2), zorder 5
show oc003_01 4 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1161144)]]'
hide c1portrait
hide c3portrait
show oc003_01 4 as c3portrait at darkleft(-6), zorder 6
show oc002_01 4 as c2portrait at rightside(-3), shakeright, zorder 5
c23 '[textdict[str(1161145)]]'
hide c3portrait
hide c2portrait
show oc002_01 4 as c2portrait at darkright(-3), zorder 5
show oc003_01 1 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1161146)]]'
hide c2portrait
hide c3portrait
show oc003_01 1 as c3portrait at darkleft(-6), zorder 6
show oc004_01 1 as c4portrait at rightside(-5), zorder 5
c43 '[textdict[str(1161147)]]'
return