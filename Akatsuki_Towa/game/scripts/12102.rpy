label avg12102:
stop music

stop music
scene avg_bg_012
with fade
play sfx2 "other_7042.ogg"
show st051_01 6 as p709 at r(-9), light, zorder 5
c7093 '[textdict[1128007]]'
stop music
hide p709
show st051_01 6 as p709 at r(-9), dark, zorder 5
show oc001_01 6 as p1 at l(-2), light, zorder 6
c11 '[textdict[1128008]]'
stop music
hide p709
hide p1
show oc001_01 6 as p1 at l(-2), dark, zorder 6
show st051_01 2 as p709 at r(-9), light, zorder 5
c7093 '[textdict[1128009]]'
play music "ed7111.ogg"
scene avg_bg_047
with fade
play sfxvoice "avg_vocal_ji07.ogg"
show oc005_01 1 as p5 at r(-6), light, zorder 5
c53 '[textdict[1128010]]'
hide p5
show oc005_01 1 as p5 at r(-6), dark, zorder 5
show oc003_01 1 as p3 at l(-6), light, zorder 6
c31 '[textdict[1128011]]'
play sfxvoice "avg_vocal_ji06.ogg"
hide p5
hide p3
show oc003_01 1 as p3 at l(-6), dark, zorder 6
show oc005_01 5 as p5 at r(-6), light, zorder 5
c53 '[textdict[1128012]]'
hide p5
hide p3
show oc003_01 1 as p3 at l(-6), dark, zorder 6
show oc005_01 1 as p5 at r(-6), light, zorder 5
c53 '[textdict[1128013]]'
hide p5
hide p3
show oc003_01 1 as p3 at l(-6), dark, zorder 6
show oc005_01 4 as p5 at r(-6), light, zorder 5
c53 '[textdict[1128014]]'
play sfxvoice "avg_vocal_ji16.ogg"
hide p5
hide p3
show oc003_01 1 as p3 at l(-6), dark, zorder 6
show oc005_01 9 as p5 at r(-6), light, zorder 5
c53 '[textdict[1128015]]'
play sfxvoice "avg_vocal_ji05.ogg"
hide p5
hide p3
show oc003_01 1 as p3 at l(-6), dark, zorder 6
show oc005_01 4 as p5 at r(-6), light, zorder 5
c53 '[textdict[1128016]]'
menu:
    extend ""
    "[textdict[1100001]]":
        call avg12104
    "[textdict[1100002]]":
        call avg12103
return