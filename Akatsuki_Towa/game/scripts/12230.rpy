label avg12230:
stop music

play music "ed7105.ogg"
scene avg_bg_023
with fade
c6891 '[textdict[1121103]]'
play sfxvoice "avg_vocal_na15.ogg"
show oc001_01 1 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1121104]]'
hide c1portrait
show oc001_01 1 as c1portrait at darkright(-2), zorder 5
c6891 '[textdict[1121105]]'
hide c1portrait
show oc001_01 1 as c1portrait at darkright(-2), zorder 5
show sc030_01 4 as c38portrait at leftside(-12), zorder 5
c381 '[textdict[1121106]]'
hide c38portrait
hide c1portrait
show oc001_01 1 as c1portrait at darkright(-2), zorder 5
show sc031_01 2 as c39portrait at leftside(-14), zorder 5
c391 '[textdict[1121107]]'
hide c39portrait
hide c1portrait
show oc001_01 1 as c1portrait at darkright(-2), zorder 5
show sc032_01 5 as c40portrait at leftside(-17), zorder 5
c401 '[textdict[1121108]]'
hide c1portrait
hide c40portrait
show sc032_01 5 as c40portrait at darkleft(-17), zorder 6
show oc002_01 2 as c2portrait at rightside(-3), zorder 5
c23 '[textdict[1121109]]'
hide c40portrait
hide c2portrait
show oc002_01 2 as c2portrait at darkright(-3), zorder 5
c6891 '[textdict[1121110]]'
hide c2portrait
show oc001_01 18 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1121111]]'
hide c1portrait
show oc001_01 18 as c1portrait at darkright(-2), zorder 5
show sc030_01 2 as c38portrait at leftside(-12), zorder 5
c381 '[textdict[1121112]]'
menu:
    "[textdict[1121113]]":
        call avg12231
    "[textdict[1121114]]":
        call avg12232
return