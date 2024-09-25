label avg19120:
stop music

play music "ed7150.ogg"
scene avg_bg_071
with fade
show sc001_01 2 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218072]]' (what_size=18)
play sfxvoice "bcv_oc002_get_02.ogg"
hide c9portrait
show sc001_01 2 as c9portrait at darkleft(-11), zorder 6
show oc001_01 2 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1218073]]' (what_size=18)
hide c9portrait
hide c1portrait
show oc001_01 2 as c1portrait at darkright(-2), zorder 5
show sc001_01 1 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218074]]' (what_size=18)
play sfxvoice "bcv_oc002_get_02.ogg"
hide c1portrait
hide c9portrait
show sc001_01 1 as c9portrait at darkleft(-11), zorder 6
show oc001_01 2 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1218075]]' (what_size=18)
hide c9portrait
hide c1portrait
show oc001_01 2 as c1portrait at darkright(-2), zorder 5
show sc001_01 4 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218076]]' (what_size=18)
play sfxvoice "bcv_oc002_arts_02.ogg"
hide c1portrait
hide c9portrait
show sc001_01 4 as c9portrait at darkleft(-11), zorder 6
show oc001_01 18 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1218077]]' (what_size=18)
menu:
    "[textdict[1218078]]":
        call avg19121
    "[textdict[1218079]]":
        call avg19122
    "[textdict[1218080]]":
        call avg19123
return