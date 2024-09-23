label avg19124:
stop music

play music "ed7150.ogg"
scene avg_bg_071
with fade
show sc001_01 2 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218085]]'
play sfxvoice "bcv_oc002_win_02.ogg"
hide c9portrait
show sc001_01 2 as c9portrait at darkleft(-11), zorder 6
show oc001_01 1 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1218086]]'
hide c9portrait
hide c1portrait
show oc001_01 1 as c1portrait at darkright(-2), zorder 5
show sc001_01 1 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218087]]'
hide c9portrait
hide c1portrait
show oc001_01 1 as c1portrait at darkright(-2), zorder 5
show sc001_01 5 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218088]]'
play sfxvoice "bcv_oc002_win_02.ogg"
hide c1portrait
hide c9portrait
show sc001_01 5 as c9portrait at darkleft(-11), zorder 6
show oc001_01 1 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1218089]]'
menu:
    "[textdict[1218090]]":
        call avg19125
    "[textdict[1218091]]":
        call avg19126
    "[textdict[1218092]]":
        call avg19127
return