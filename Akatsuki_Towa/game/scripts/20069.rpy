label avg20069:
stop music

play music "ed7150.ogg"
scene avg_bg_015
show oc001_01 4 as p1 at l(-2), light, zorder 6
window show
with fade_out
c11 '[textdict[1003881]]'
hide p1
show oc001_01 4 as p1 at l(-2), dark, zorder 6
show oc002_01 4 as p2 at r(-3), light, zorder 5
c23 '[textdict[1003882]]'
hide p2
hide p1
show oc001_01 4 as p1 at l(-2), dark, zorder 6
show oc003_01 4 as p3 at r(-6), light, zorder 5
c33 '[textdict[1003883]]'
hide p1
hide p3
show oc003_01 4 as p3 at r(-6), dark, zorder 5
show oc001_01 18 as p1 at l(-2), light, zorder 6
play sfxvoice "avg_vocal_na06.ogg"
c11 '[textdict[1003884]]'
hide p1
hide p3
show oc003_01 4 as p3 at r(-6), dark, zorder 5
show oc001_01 1 as p1 at l(-2), light, zorder 6
c11 '[textdict[1003885]]'
return