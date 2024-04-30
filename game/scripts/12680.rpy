label avg12680:
stop music

play music "ed7203.ogg"
scene avg_bg_070
with fade
show oc003_01 4 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1166980)]]'
hide c3portrait
show oc003_01 4 as c3portrait at darkleft(-6), zorder 6
show oc004_01 4 as c4portrait at rightside(-5), zorder 5
c43 '[textdict[str(1166981)]]'
hide c3portrait
hide c4portrait
show oc004_01 4 as c4portrait at darkright(-5), zorder 5
show oc002_01 8 as c2portrait at leftside(-3), zorder 5
c21 '[textdict[str(1166982)]]'
hide c4portrait
hide c2portrait
show oc002_01 8 as c2portrait at darkleft(-3), zorder 6
show oc001_01 7 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1166983)]]'
hide c2portrait
hide c1portrait
show oc001_01 7 as c1portrait at darkright(-2), zorder 5
show oc004_01 8 as c4portrait at leftside(-5), zorder 5
c41 '[textdict[str(1166984)]]'
play sfx2 "other_7080.ogg"
hide c4portrait
hide c1portrait
show oc001_01 7 as c1portrait at darkright(-2), zorder 5
show oc003_01 4 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1166985)]]'
play sfx2 "fight_6024.ogg"
hide c1portrait
hide c3portrait
show oc003_01 4 as c3portrait at darkleft(-6), zorder 6
show oc001_01 4 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1166986)]]'
return