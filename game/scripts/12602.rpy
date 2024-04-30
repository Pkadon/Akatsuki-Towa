label avg12602:
stop music

play music "ED6200.ogg"
scene avg_bg_080
with fade
play sfxvoice "avg_vocal_ch19.ogg"
show oc002_01 17 as c2portrait at leftsideentrance(-3), zorder 5
c21 '[textdict[str(1161132)]]'
hide c2portrait
show oc002_01 17 as c2portrait at darkleft(-3), zorder 6
show oc001_01 1 as c1portrait at rightsideentrance(-2), zorder 5
c13 '[textdict[str(1161133)]]'
hide c2portrait
hide c1portrait
show oc001_01 1 as c1portrait at darkright(-2), zorder 5
show oc002_01 1 as c2portrait at leftside(-3), zorder 5
c21 '[textdict[str(1161134)]]'
hide c1portrait
hide c2portrait
show oc002_01 1 as c2portrait at darkleft(-3), zorder 6
show oc004_01 1 as c4portrait at rightside(-5), zorder 5
c43 '[textdict[str(1161135)]]'
hide c2portrait
hide c4portrait
show oc004_01 1 as c4portrait at darkright(-5), zorder 5
show oc002_01 23 as c2portrait at leftside(-3), zorder 5
c21 '[textdict[str(1161136)]]'
play sfxvoice "avg_vocal_ro12.ogg"
hide c2portrait
hide c4portrait
show oc004_01 1 as c4portrait at darkright(-5), zorder 5
show oc003_01 17 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1161137)]]'
hide c4portrait
hide c3portrait
show oc003_01 17 as c3portrait at darkleft(-6), zorder 6
show oc001_01 8 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1161138)]]'
hide c3portrait
hide c1portrait
show oc001_01 8 as c1portrait at darkright(-2), zorder 5
show oc002_01 12 as c2portrait at leftside(-3), zorder 5
c21 '[textdict[str(1161139)]]'
play sfx2 "fight_6025.ogg"
hide c2portrait
hide c1portrait
show oc001_01 8 as c1portrait at darkright(-2), zorder 5
show oc003_01 5 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1161140)]]'
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_com_01.ogg"
hide c1portrait
hide c3portrait
show oc003_01 5 as c3portrait at darkleft(-6), zorder 6
show oc001_01 4 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1161141)]]'
return