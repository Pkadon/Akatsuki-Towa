label avg12820:
stop music

play music "ED6202.ogg"
scene avg_bg_201
window show
with fade_in
c0 '[textdict[1183812]]'
c25521 '[textdict[1183813]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1183814]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 23', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1183815]]'
hide p1
$ update_portrait('oc002_01 23', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 5)
c13043 '[textdict[1183816]]'
hide p2
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1183817]]'
hide p3
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
c25521 '[textdict[1183818]]'
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 5)
c13043 '[textdict[1183819]]'
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
c25521 '[textdict[1183820]]'
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 5)
c13043 '[textdict[1183821]]'
$ update_portrait('st061_01 5', 'p1304', [r(-2), dark], 5)
c25521 '[textdict[1183822]]'
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 5)
c13043 '[textdict[1183823]]'
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
c25531 '[textdict[1183824]]'
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc002_01 22', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1183825]]'
$ update_portrait('oc002_01 22', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 5)
c13043 '[textdict[1183826]]'
hide p2
hide p1304
play sfx2 "other_7013.ogg"
c0 '[textdict[1183827]]'
return