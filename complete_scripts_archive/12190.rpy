label avg12190:
stop music

play music "ed7110.ogg"
scene avg_bg_023
show oc001_01 18 as p1 at r(-2), light, zorder 5
window show
with fade_out
play sfx2 "common_cancel.ogg"
c13 '[textdict[1120720]]'
hide p1
show oc001_01 18 as p1 at r(-2), dark, zorder 5
show st009_01 2 as p209 at l(-22), light, zorder 6
c2091 '[textdict[1120721]]'
return