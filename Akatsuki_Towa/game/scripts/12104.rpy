label avg12104:
stop music

play music "ed7111.ogg"
scene avg_bg_047
show oc001_01 4 as p1 at l(-2), light, flip, zorder 6
window show
with fade_in
play sfx2 "common_select.ogg"
c11 '[textdict[1128019]]'
hide p1
show oc001_01 4 as p1 at l(-2), dark, flip, zorder 6
show oc005_01 5 as p5 at r(-6), light, zorder 5
play sfxvoice "avg_vocal_ji11.ogg"
c53 '[textdict[1128020]]'
hide p5
hide p1
show oc001_01 4 as p1 at l(-2), dark, flip, zorder 6
show oc005_01 4 as p5 at r(-6), light, zorder 5
c53 '[textdict[1128021]]'
hide p5
hide p1
show oc001_01 4 as p1 at l(-2), dark, flip, zorder 6
show oc005_01 10 as p5 at r(-6), light, zorder 5
c53 '[textdict[1128022]]'
hide p1
hide p5
show oc005_01 10 as p5 at r(-6), dark, zorder 5
show oc001_01 18 as p1 at l(-2), light, flip, zorder 6
c11 '[textdict[1128023]]'
hide p5
hide p1
show oc001_01 18 as p1 at l(-2), dark, flip, zorder 6
show oc005_01 1 as p5 at r(-6), light, zorder 5
play sfx2 "common_quest.ogg"
c53 '[textdict[1128024]]'
return