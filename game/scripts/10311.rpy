label avg10311:
stop music

play music "ed7105.ogg"
scene avg_bg_022
with fade
play sfx2 "other_7020.ogg"
show oc002_01 2 as c2portrait at leftside(-3), zorder 5
c21 '[textdict[str(1130295)]]'
hide c2portrait
show oc002_01 2 as c2portrait at darkleft(-3), zorder 6
show st053_01 1 as c1007portrait at rightside(-12), zorder 5
c10073 '[textdict[str(1130296)]]'
hide c2portrait
hide c1007portrait
show st053_01 1 as c1007portrait at darkright(-12), zorder 5
show oc001_01 6 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[str(1130297)]]'
hide c1007portrait
hide c1portrait
show oc001_01 6 as c1portrait at darkleft(-2), zorder 6
show st053_01 2 as c1007portrait at rightside(-12), zorder 5
c10073 '[textdict[str(1130298)]]'
hide c1portrait
hide c1007portrait
show st053_01 2 as c1007portrait at darkright(-12), zorder 5
show oc002_01 8 as c2portrait at leftside(-3), zorder 5
c21 '[textdict[str(1130299)]]'
hide c2portrait
hide c1007portrait
show st053_01 2 as c1007portrait at darkright(-12), zorder 5
show oc001_01 1 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[str(1130300)]]'
hide c1007portrait
hide c1portrait
show oc001_01 1 as c1portrait at darkleft(-2), zorder 6
show st053_01 5 as c1007portrait at rightside(-12), zorder 5
c10073 '[textdict[str(1130301)]]'
hide c1007portrait
hide c1portrait
show oc001_01 1 as c1portrait at darkleft(-2), zorder 6
show st053_01 1 as c1007portrait at rightside(-12), zorder 5
c10073 '[textdict[str(1130309)]]'
hide c1007portrait
hide c1portrait
show oc001_01 1 as c1portrait at darkleft(-2), zorder 6
show st053_01 1 as c1007portrait at rightside(-12), zorder 5
c10073 '[textdict[str(1130310)]]'
hide c1portrait
hide c1007portrait
show st053_01 1 as c1007portrait at darkright(-12), zorder 5
show oc001_01 2 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[str(1130311)]]'
play sfxvoice "avg_vocal_ro05.ogg"
hide c1007portrait
hide c1portrait
show oc001_01 2 as c1portrait at darkleft(-2), zorder 6
show oc003_01 5 as c3portrait at rightside(-6), zorder 5
c33 '[textdict[str(1130312)]]'
play sfxvoice "avg_vocal_li21.ogg"
hide c1portrait
hide c3portrait
show oc003_01 5 as c3portrait at darkright(-6), zorder 5
show oc004_01 7 as c4portrait at leftside(-5), shakeleft, zorder 5
c41 '[textdict[str(1130313)]]'
hide c3portrait
hide c4portrait
show oc004_01 7 as c4portrait at darkleft(-5), zorder 6
show st053_01 4 as c1007portrait at rightside(-12), zorder 5
c10073 '[textdict[str(1130314)]]'
menu:
    "[textdict[str(1130315)]]":
        call avg10313
    "[textdict[str(1130316)]]":
        call avg10314
return