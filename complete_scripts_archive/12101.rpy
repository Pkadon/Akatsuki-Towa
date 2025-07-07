label avg12101:
stop music

play music "ed7111.ogg"
scene avg_bg_047
show oc005_01 2 as p5 at r(-6), light, zorder 5
with fade
play sfxvoice "avg_vocal_ji04.ogg"
c53 '[textdict[1128006]]'
hide p5
show oc005_01 2 as p5 at r(-6), dark, zorder 5
show oc003_01 1 as p3 at l(-6), light, zorder 6
c31 '[textdict[1128011]]'
hide p5
hide p3
show oc003_01 1 as p3 at l(-6), dark, zorder 6
show oc005_01 5 as p5 at r(-6), light, zorder 5
play sfxvoice "avg_vocal_ji06.ogg"
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
hide p5
hide p3
show oc003_01 1 as p3 at l(-6), dark, zorder 6
show oc005_01 9 as p5 at r(-6), light, zorder 5
play sfxvoice "avg_vocal_ji16.ogg"
c53 '[textdict[1128015]]'
hide p5
hide p3
show oc003_01 1 as p3 at l(-6), dark, zorder 6
show oc005_01 4 as p5 at r(-6), light, zorder 5
play sfxvoice "avg_vocal_ji05.ogg"
c53 '[textdict[1128016]]'
menu:
    extend ""
    "[textdict[1100001]]":
        call avg12104
    "[textdict[1100002]]":
        call avg12103
return