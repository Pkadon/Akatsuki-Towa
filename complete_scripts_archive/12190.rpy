label avg12190:
stop music

play music "ed7110.ogg"
scene avg_bg_023
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
window show
with fade_in
play sfx2 "common_cancel.ogg"
c13 '[textdict[1120720]]'
hide p1
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('st009_01 2', 'p209', [l(-22), light, flip], 6)
c2091 '[textdict[1120721]]'
return