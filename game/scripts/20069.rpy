label avg20069:
stop music

play music "ed7150.ogg"
scene avg_bg_015
with fade
show oc001_01 4 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[str(1003881)]]'
hide c1portrait
show oc001_01 4 as c1portrait at darkleft(-2), zorder 6
show oc002_01 4 as c2portrait at rightside(-3), zorder 5
c23 '[textdict[str(1003882)]]'
hide c2portrait
hide c1portrait
show oc001_01 4 as c1portrait at darkleft(-2), zorder 6
show oc003_01 4 as c3portrait at rightside(-6), zorder 5
c33 '[textdict[str(1003883)]]'
play sfxvoice "avg_vocal_na06.ogg"
hide c1portrait
hide c3portrait
show oc003_01 4 as c3portrait at darkright(-6), zorder 5
show oc001_01 18 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[str(1003884)]]'
hide c1portrait
hide c3portrait
show oc003_01 4 as c3portrait at darkright(-6), zorder 5
show oc001_01 1 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[str(1003885)]]'
return