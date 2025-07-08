label avg12353:
stop music

play music "ed7104.ogg"
scene avg_bg_050
show oc001_01 6 as p1 at r(-2), light, zorder 5
window show
with fade_out
play sfx2 "other_7021.ogg"
c13 '[textdict[1133603]]'
hide p1
show oc001_01 6 as p1 at r(-2), dark, zorder 5
show oc004_01 2 as p4 at l(-5), light, flip, zorder 6
c41 '[textdict[1133604]]'
play music "ed7110.ogg"
scene avg_bg_001
show oc005_01 2 as p5 at r(-6), light, zorder 5
with fade
play sfxvoice "avg_vocal_ji02.ogg"
c53 '[textdict[1133645]]'
hide p5
show oc005_01 2 as p5 at r(-6), dark, zorder 5
show oc004_01 9 as p4 at l(-5), light, flip, zorder 6
c41 '[textdict[1133646]]'
hide p5
hide p4
show oc004_01 9 as p4 at l(-5), dark, flip, zorder 6
show oc005_01 4 as p5 at r(-6), light, zorder 5
c53 '[textdict[1133647]]'
hide p4
hide p5
show oc005_01 4 as p5 at r(-6), dark, zorder 5
show oc002_01 11 as p2 at l(-3), light, flip, zorder 6
c21 '[textdict[1133648]]'
hide p5
hide p2
show oc002_01 11 as p2 at l(-3), dark, flip, zorder 6
show oc001_01 6 as p1 at r(-2), light, zorder 5
play sfx2 "other_7018.ogg"
c13 '[textdict[1133649]]'
return