label avg12116:
stop music

play music "ed7111.ogg"
scene avg_bg_047
with fade
play sfxvoice "avg_vocal_ji02.ogg"
show oc005_01 1 as c5portrait at rightside(-6), zorder 5
c53 '[textdict[str(1128203)]]'
play sfx2 "other_7004.ogg"
hide c5portrait
show oc005_01 4 as c5portrait at rightside(-6), zorder 5
c53 '[textdict[str(1128204)]]'
hide c5portrait
show oc005_01 4 as c5portrait at darkright(-6), zorder 5
show oc003_01 7 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1128205)]]'
hide c3portrait
hide c5portrait
show oc005_01 4 as c5portrait at darkright(-6), zorder 5
show oc003_01 4 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1128206)]]'
play sfxvoice "avg_vocal_na03.ogg"
hide c5portrait
hide c3portrait
show oc003_01 4 as c3portrait at darkleft(-6), zorder 6
show oc001_01 18 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1128207)]]'
hide c1portrait
hide c3portrait
show oc003_01 4 as c3portrait at darkleft(-6), zorder 6
show oc001_01 4 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1128208)]]'
hide c3portrait
hide c1portrait
show oc001_01 4 as c1portrait at darkright(-2), zorder 5
show oc003_01 7 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1128209)]]'
play sfxvoice "bcv_oc002_c02_01.ogg"
hide c3portrait
hide c1portrait
show oc001_01 4 as c1portrait at darkright(-2), zorder 5
show oc002_01 9 as c2portrait at leftside(-3), zorder 5
c21 '[textdict[str(1128210)]]'
play sfxvoice "bcv_oc001_c04_01.ogg"
hide c1portrait
hide c2portrait
show oc002_01 9 as c2portrait at darkleft(-3), zorder 6
show oc001_01 7 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1128211)]]' with Shake((0, 0, 0, 0), 0.5, dist=20)
return