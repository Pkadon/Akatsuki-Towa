label avg127118:
stop music

play music "ED6202.ogg"
scene avg_bg_010
window show
with fade_in
c0 '[textdict[1179502]]'
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 5)
c23 '[textdict[1179503]]'
hide p2
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1179504]]'
hide p2
hide p1304
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1179505]]'
hide p1
hide p1304
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1179506]]'
hide p1304
hide p1
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1179507]]'
return