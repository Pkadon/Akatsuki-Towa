label avg19107:
stop music

play music "ed7150.ogg"
scene avg_bg_071
with fade
play sfxvoice "avg_vocal_na02.ogg"
show oc001_01 2 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1218031]]'
hide c1portrait
show oc001_01 2 as c1portrait at darkright(-2), zorder 5
show sc001_01 1 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218032]]'
play sfxvoice "avg_vocal_na21.ogg"
hide c1portrait
hide c9portrait
show sc001_01 1 as c9portrait at darkleft(-11), zorder 6
show oc001_01 12 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1218033]]'
hide c9portrait
hide c1portrait
show oc001_01 12 as c1portrait at darkright(-2), zorder 5
show sc001_01 1 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218034]]'
hide c9portrait
hide c1portrait
show oc001_01 12 as c1portrait at darkright(-2), zorder 5
show sc001_01 5 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218035]]'
play sfxvoice "avg_vocal_na02.ogg"
hide c1portrait
hide c9portrait
show sc001_01 5 as c9portrait at darkleft(-11), zorder 6
show oc001_01 2 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1218036]]'
menu:
    "[textdict[1218037]]":
        call avg19108
    "[textdict[1218038]]":
        call avg19109
    "[textdict[1218039]]":
        call avg19110
return