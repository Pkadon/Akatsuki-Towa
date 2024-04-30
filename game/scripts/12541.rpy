label avg12541:
stop music

play music "ED6200.ogg"
scene avg_bg_010
with fade
c00 '[textdict[str(1152919)]]'
show oc003_01 4 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1152920)]]'
play sfxvoice "avg_vocal_ch19.ogg"
hide c3portrait
show oc003_01 4 as c3portrait at darkleft(-6), zorder 6
show oc002_01 10 as c2portrait at rightside(-3), zorder 5
c23 '[textdict[str(1152921)]]'
hide c3portrait
hide c2portrait
show oc002_01 10 as c2portrait at darkright(-3), zorder 5
show oc004_01 4 as c4portrait at leftside(-5), zorder 5
c41 '[textdict[str(1152922)]]'
return