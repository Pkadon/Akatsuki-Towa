label avg10851:
stop music

scene avg_bg_204
window show
with fade_in
c0 '[textdict[1189489]]'
c0 '[textdict[1189490]]'
c0 '[textdict[1189491]]'
c0 '[textdict[1189492]]'
play music "ed7304.ogg"
scene avg_bg_203
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 5)
with fade
c13043 '[textdict[1189493]]'
$ update_portrait('st061_01 4', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc004_01 18', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1189494]]'
hide p1304
$ update_portrait('oc004_01 18', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1189495]]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1189496]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1189497]]'
hide p2
hide p1
c0 '[textdict[1189498]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1189499]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1189500]]'
hide p1
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[textdict[1189501]]'
hide p1304
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1189502]]'
play music "ed7511.ogg"
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
play sfx2 "elc_5006.ogg"
c26221 '[textdict[1189503]]'
hide p3
play sfx2 "other_7034.ogg"
c0 '[textdict[1189504]]'
$ update_portrait('oc003_01 21', 'p3', [l(-6), l_shake, light, flip], 6)
c31 '[textdict[1189505]]'
$ update_portrait('oc003_01 21', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 5)
c13 '[textdict[1189506]]' with shake
return