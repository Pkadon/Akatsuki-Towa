label avg10308:
stop music

play music "ed7124.ogg"
scene avg_bg_059
with fade
play sfx2 "other_7021.ogg"
c10063 '[textdict[str(1130265)]]'
show oc001_01 1 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[str(1130266)]]'
hide c1portrait
show oc001_01 1 as c1portrait at darkleft(-2), zorder 6
c10063 '[textdict[str(1130267)]]'
hide c1portrait
show oc001_01 1 as c1portrait at darkleft(-2), zorder 6
c10063 '[textdict[str(1130268)]]'
hide c1portrait
show oc001_01 1 as c1portrait at darkleft(-2), zorder 6
c10063 '[textdict[str(1130269)]]'
hide c1portrait
show oc004_01 1 as c4portrait at leftside(-5), zorder 5
c41 '[textdict[str(1130270)]]'
hide c4portrait
show oc004_01 1 as c4portrait at darkleft(-5), zorder 6
c10063 '[textdict[str(1130271)]]'
hide c4portrait
show oc004_01 2 as c4portrait at leftside(-5), zorder 5
c41 '[textdict[str(1130272)]]'
hide c4portrait
show oc004_01 2 as c4portrait at darkleft(-5), zorder 6
c10063 '[textdict[str(1130273)]]'
hide c4portrait
show oc004_01 2 as c4portrait at darkleft(-5), zorder 6
c10063 '[textdict[str(1130274)]]'
hide c4portrait
show oc004_01 12 as c4portrait at leftside(-5), shakeleft, zorder 5
c41 '[textdict[str(1130275)]]'
hide c4portrait
show oc004_01 12 as c4portrait at darkleft(-5), zorder 6
show oc001_01 2 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1130276)]]'
hide c1portrait
hide c4portrait
show oc004_01 12 as c4portrait at darkleft(-5), zorder 6
show oc002_01 2 as c2portrait at rightside(-3), zorder 5
c23 '[textdict[str(1130277)]]'
play sfxvoice "avg_vocal_ro08.ogg"
hide c2portrait
hide c4portrait
show oc004_01 12 as c4portrait at darkleft(-5), zorder 6
show oc003_01 5 as c3portrait at rightside(-6), zorder 5
c33 '[textdict[str(1130278)]]'
hide c4portrait
hide c3portrait
show oc003_01 5 as c3portrait at darkright(-6), zorder 5
show oc004_01 7 as c4portrait at leftside(-5), shakeleft, zorder 5
c41 '[textdict[str(1130279)]]'
hide c3portrait
hide c4portrait
show oc004_01 7 as c4portrait at darkleft(-5), zorder 6
c10063 '[textdict[str(1130280)]]'
play sfxvoice "avg_vocal_li30.ogg"
hide c4portrait
show oc004_01 5 as c4portrait at leftside(-5), zorder 5
c41 '[textdict[str(1130281)]]'
hide c4portrait
show oc004_01 5 as c4portrait at darkleft(-5), zorder 6
show oc001_01 8 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1130282)]]'
menu:
    "[textdict[str(1130283)]]":
        call avg10309
    "[textdict[str(1130284)]]":
        call avg10310
return