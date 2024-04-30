label avg12741:
stop music

play music "ed7105.ogg"
scene avg_bg_203
with fade
c00 '[textdict[str(1172905)]]'
c00 '[textdict[str(1172906)]]'
show oc001_01 4 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1172907)]]'
hide c1portrait
show oc001_01 4 as c1portrait at darkright(-2), zorder 5
show oc003_01 4 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1172908)]]'
hide c3portrait
hide c1portrait
show oc001_01 4 as c1portrait at darkright(-2), zorder 5
show oc003_01 17 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1172909)]]'
hide c1portrait
hide c3portrait
show oc003_01 17 as c3portrait at darkleft(-6), zorder 6
show oc001_01 2 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1172910)]]'
hide c3portrait
hide c1portrait
show oc001_01 2 as c1portrait at darkright(-2), zorder 5
show oc003_01 16 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1172911)]]'
hide c3portrait
hide c1portrait
show oc001_01 2 as c1portrait at darkright(-2), zorder 5
show oc003_01 1 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1172912)]]'
play sfx2 "fight_6024.ogg"
hide c1portrait
hide c3portrait
show oc003_01 1 as c3portrait at darkleft(-6), zorder 6
show oc001_01 4 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1172913)]]' with Shake((0, 0, 0, 0), 0.5, dist=20)
play sfx2 "fight_6025.ogg"
hide c3portrait
hide c1portrait
show oc001_01 4 as c1portrait at darkright(-2), zorder 5
show oc003_01 4 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1172914)]]'
return