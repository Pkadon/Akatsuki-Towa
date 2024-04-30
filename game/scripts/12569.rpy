label avg12569:
stop music

play music "ED6200.ogg"
scene avg_bg_010
with fade
play sfxvoice "avg_vocal_li07.ogg"
show oc004_01 5 as c4portrait at leftside(-5), shakeleft, zorder 5
c41 '[textdict[str(1155140)]]'
hide c4portrait
show oc004_01 5 as c4portrait at darkleft(-5), zorder 6
show oc002_01 16 as c2portrait at rightside(-3), zorder 5
c23 '[textdict[str(1155141)]]'
play sfxvoice "avg_vocal_ch09.ogg"
hide c2portrait
hide c4portrait
show oc004_01 5 as c4portrait at darkleft(-5), zorder 6
show oc002_01 14 as c2portrait at rightside(-3), shakeright, zorder 5
c23 '[textdict[str(1155142)]]'
hide c4portrait
hide c2portrait
show oc002_01 14 as c2portrait at darkright(-3), zorder 5
show oc003_01 17 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[str(1155143)]]'
play sfxvoice "avg_vocal_na20.ogg"
hide c2portrait
hide c3portrait
show oc003_01 17 as c3portrait at darkleft(-6), zorder 6
show oc001_01 10 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1155144)]]'
return