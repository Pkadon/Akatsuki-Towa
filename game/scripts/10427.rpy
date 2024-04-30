label avg10427:
stop music

play music "ed7511.ogg"
scene placeholderbackground
with fade
c00 '[textdict[str(1141272)]]'
show oc001_01 13 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1141273)]]'
play sfxvoice "avg_vocal_na07.ogg"
hide c1portrait
show oc001_01 3 as c1portrait at rightside(-2), shakeleft, zorder 5
c13 '[textdict[str(1141274)]]'
hide c1portrait
show oc001_01 3 as c1portrait at darkright(-2), zorder 5
c11091 '[textdict[str(1141275)]]'
play sfxvoice "bcv_oc001_hurt_02.ogg"
hide c1portrait
show oc001_01 3 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1141276)]]'
hide c1portrait
show oc001_01 3 as c1portrait at darkright(-2), zorder 5
show oc002_01 9 as c2portrait at leftsideentrance(-3), zorder 5
c21 '[textdict[str(1141277)]]'
play sfxvoice "avg_vocal_li11.ogg"
hide c2portrait
hide c1portrait
show oc001_01 3 as c1portrait at darkright(-2), zorder 5
show oc004_01 12 as c4portrait at leftsideentrance(-5), zorder 5
c41 '[textdict[str(1141278)]]'
hide c1portrait
hide c4portrait
show oc004_01 12 as c4portrait at darkleft(-5), zorder 6
show oc001_01 9 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1141279)]]'
play sfxvoice "avg_vocal_ro09.ogg"
hide c4portrait
hide c1portrait
show oc001_01 9 as c1portrait at darkright(-2), zorder 5
show oc003_01 2 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1141280)]]'
hide c1portrait
hide c3portrait
show oc003_01 2 as c3portrait at darkleft(-6), zorder 6
show oc001_01 3 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1141281)]]'
play sfx2 "other_7007.ogg"
hide c3portrait
hide c1portrait
show oc001_01 3 as c1portrait at darkright(-2), zorder 5
c11091 '[textdict[str(1141282)]]' with Shake((0, 0, 0, 0), 0.5, dist=20)
return