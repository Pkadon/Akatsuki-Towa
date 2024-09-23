label avg10312:
stop music

play music "ed7105.ogg"
scene avg_bg_022
with fade
show st053_01 1 as c1007portrait at rightside(-12), zorder 5
c10073 '[textdict[1130302]]'
hide c1007portrait
show st053_01 1 as c1007portrait at darkright(-12), zorder 5
show oc001_01 1 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[1130303]]'
hide c1007portrait
hide c1portrait
show oc001_01 1 as c1portrait at darkleft(-2), zorder 6
show oc002_01 5 as c2portrait at rightside(-3), zorder 5
c23 '[textdict[1130304]]'
hide c1portrait
hide c2portrait
show oc002_01 5 as c2portrait at darkright(-3), zorder 5
show oc003_01 1 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[1130305]]'
hide c2portrait
hide c3portrait
show oc003_01 1 as c3portrait at darkleft(-6), zorder 6
show st053_01 2 as c1007portrait at rightside(-12), zorder 5
c10073 '[textdict[1130306]]'
hide c3portrait
hide c1007portrait
show st053_01 2 as c1007portrait at darkright(-12), zorder 5
show oc004_01 1 as c4portrait at leftside(-5), zorder 5
c41 '[textdict[1130307]]'
hide c1007portrait
hide c4portrait
show oc004_01 1 as c4portrait at darkleft(-5), zorder 6
show st053_01 4 as c1007portrait at rightside(-12), zorder 5
c10073 '[textdict[1130308]]'
hide c1007portrait
hide c4portrait
show oc004_01 1 as c4portrait at darkleft(-5), zorder 6
show st053_01 1 as c1007portrait at rightside(-12), zorder 5
c10073 '[textdict[1130309]]'
hide c1007portrait
hide c4portrait
show oc004_01 1 as c4portrait at darkleft(-5), zorder 6
show st053_01 1 as c1007portrait at rightside(-12), zorder 5
c10073 '[textdict[1130310]]'
hide c4portrait
hide c1007portrait
show st053_01 1 as c1007portrait at darkright(-12), zorder 5
show oc001_01 2 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[1130311]]'
play sfxvoice "avg_vocal_ro05.ogg"
hide c1007portrait
hide c1portrait
show oc001_01 2 as c1portrait at darkleft(-2), zorder 6
show oc003_01 5 as c3portrait at rightside(-6), zorder 5
c33 '[textdict[1130312]]'
play sfxvoice "avg_vocal_li21.ogg"
hide c1portrait
hide c3portrait
show oc003_01 5 as c3portrait at darkright(-6), zorder 5
show oc004_01 7 as c4portrait at leftside(-5), shakeleft, zorder 5
c41 '[textdict[1130313]]'
hide c3portrait
hide c4portrait
show oc004_01 7 as c4portrait at darkleft(-5), zorder 6
show st053_01 4 as c1007portrait at rightside(-12), zorder 5
c10073 '[textdict[1130314]]'
menu:
    "[textdict[1130315]]":
        call avg10313
    "[textdict[1130316]]":
        call avg10314
return