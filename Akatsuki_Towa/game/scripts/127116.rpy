label avg127116:
stop music

play music "ED6202.ogg"
scene avg_bg_010
window show
with fade_in
$ update_portrait('st061_01 1', 'p1304', [l_entrance(-2), light, flip], 6)
c13041 '[textdict[1179474]]'
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1179475]]'
hide p1304
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1179476]]'
hide p1
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 5)
c23 '[textdict[1179477]]'
hide p1304
hide p2
c0 '[textdict[1179478]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1179479]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1179480]]'
hide p1
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1179481]]'
hide p1304
hide p2
play sfx2 "other_7079.ogg"
c0 '[textdict[1179482]]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 5)
c13 '[textdict[1179483]]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1179484]]'
return