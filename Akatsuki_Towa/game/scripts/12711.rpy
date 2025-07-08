label avg12711:
stop music

play music "ed7516.ogg"
scene avg_bg_070
window show
with fade_in
c0 '[textdict[1170719]]'
c0 '[textdict[1170720]]'
scene avg_bg_050
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
with fade
c13 '[textdict[1170721]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1170722]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1170723]]'
hide p1
hide p1304
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1170724]]'
hide p1304
hide p1
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1170725]]'
hide p1304
hide p1
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1170726]]'
hide p1304
hide p1
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1170727]]'
hide p1
hide p1304
$ update_portrait('st061_01 5', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1170728]]'
hide p1304
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1170729]]'
return