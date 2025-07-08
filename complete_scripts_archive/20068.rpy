label avg20068:
stop music

play music "ed7150.ogg"
scene avg_bg_043
show oc001_01 4 as p1 at l(-2), light, flip, zorder 6
window show
with fade_out
play sfx2 "other_7043.ogg"
c11 '[textdict[1003875]]'
hide p1
show oc001_01 2 as p1 at l(-2), light, flip, zorder 6
c11 '[textdict[1003876]]'
hide p1
show oc001_01 4 as p1 at l(-2), light, flip, zorder 6
c11 '[textdict[1003877]]'
hide p1
show oc001_01 4 as p1 at l(-2), dark, flip, zorder 6
show oc002_01 2 as p2 at r_entrance(-3), light, zorder 5
c23 '[textdict[1001582]]'
hide p1
hide p2
show oc002_01 2 as p2 at r(-3), dark, zorder 5
show oc001_01 10 as p1 at l(-2), light, flip, zorder 6
play sfxvoice "avg_vocal_na20.ogg"
c11 '[textdict[1003879]]'
hide p1
hide p2
show oc002_01 2 as p2 at r(-3), dark, zorder 5
show oc001_01 4 as p1 at l(-2), light, flip, zorder 6
c11 '[textdict[1003880]]'
return