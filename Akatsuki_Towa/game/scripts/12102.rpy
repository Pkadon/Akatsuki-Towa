label avg12102:
stop music

stop music
scene avg_bg_012
with fade
play sfx2 "other_7042.ogg"
show st051_01 6 as c709portrait at rightside(-9), zorder 5
c7093 '[textdict[1128007]]'
stop music
hide c709portrait
show st051_01 6 as c709portrait at darkright(-9), zorder 5
show oc001_01 6 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[1128008]]'
stop music
hide c709portrait
hide c1portrait
show oc001_01 6 as c1portrait at darkleft(-2), zorder 6
show st051_01 2 as c709portrait at rightside(-9), zorder 5
c7093 '[textdict[1128009]]'
play music "ed7111.ogg"
scene avg_bg_047
with fade
play sfxvoice "avg_vocal_ji07.ogg"
show oc005_01 1 as c5portrait at rightside(-6), zorder 5
c53 '[textdict[1128010]]'
hide c5portrait
show oc005_01 1 as c5portrait at darkright(-6), zorder 5
show oc003_01 1 as c3portrait at leftside(-6), zorder 5
c31 '[textdict[1128011]]'
play sfxvoice "avg_vocal_ji06.ogg"
hide c5portrait
hide c3portrait
show oc003_01 1 as c3portrait at darkleft(-6), zorder 6
show oc005_01 5 as c5portrait at rightside(-6), zorder 5
c53 '[textdict[1128012]]'
hide c5portrait
hide c3portrait
show oc003_01 1 as c3portrait at darkleft(-6), zorder 6
show oc005_01 1 as c5portrait at rightside(-6), zorder 5
c53 '[textdict[1128013]]'
hide c5portrait
hide c3portrait
show oc003_01 1 as c3portrait at darkleft(-6), zorder 6
show oc005_01 4 as c5portrait at rightside(-6), zorder 5
c53 '[textdict[1128014]]'
play sfxvoice "avg_vocal_ji16.ogg"
hide c5portrait
hide c3portrait
show oc003_01 1 as c3portrait at darkleft(-6), zorder 6
show oc005_01 9 as c5portrait at rightside(-6), zorder 5
c53 '[textdict[1128015]]'
play sfxvoice "avg_vocal_ji05.ogg"
hide c5portrait
hide c3portrait
show oc003_01 1 as c3portrait at darkleft(-6), zorder 6
show oc005_01 4 as c5portrait at rightside(-6), zorder 5
c53 '[textdict[1128016]]'
menu:
    "[textdict[1100001]]":
        call avg12104
    "[textdict[1100002]]":
        call avg12103
return