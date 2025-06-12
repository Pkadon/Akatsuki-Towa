label avg100108:
stop music

stop music
scene placeholderbackground
with fade
play sfxvoice "avg_vocal_na02.ogg"
show oc001_01 2 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1218033]]'
stop music
hide c1portrait
show oc001_01 2 as c1portrait at darkright(-2), zorder 5
show sc001_01 1 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218034]]'
stop music
play sfxvoice "avg_vocal_na21.ogg"
hide c1portrait
hide c9portrait
show sc001_01 1 as c9portrait at darkleft(-11), zorder 6
show oc001_01 12 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1218035]]'
stop music
hide c9portrait
hide c1portrait
show oc001_01 12 as c1portrait at darkright(-2), zorder 5
show sc001_01 1 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218036]]'
stop music
hide c9portrait
hide c1portrait
show oc001_01 12 as c1portrait at darkright(-2), zorder 5
show sc001_01 5 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218037]]'
stop music
play sfxvoice "avg_vocal_na02.ogg"
hide c1portrait
hide c9portrait
show sc001_01 5 as c9portrait at darkleft(-11), zorder 6
show oc001_01 2 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1218038]]'
menu:
    extend ""
    "[textdict[1218039]]":
        call avg100109
    "[textdict[1218040]]":
        call avg100110
    "[textdict[1218041]]":
        call avg100111
return