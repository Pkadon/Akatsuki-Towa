label avg12767:
stop music

play music "ed6564.ogg"
scene avg_bg_038
window show
with fade_in
c0 '[textdict[1174736]]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1174737]]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[textdict[1174738]]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1174739]]'
hide p3
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1174740]]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1174741]]'
hide p1
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 5)
c33 '[textdict[1174742]]'
hide p1304
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1174743]]'
hide p3
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
c33 '[textdict[1174744]]'
hide p3
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 5)
c33 '[textdict[1174745]]'
hide p1304
$ update_portrait('oc003_01 16', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1174746]]'
hide p1304
hide p3
c0 '[textdict[1174747]]'
play sfx2 "other_7012.ogg"
c0 '[textdict[1174748]]'
$ update_portrait('oc004_01 23', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1174749]]'
$ update_portrait('oc004_01 23', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1174750]]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1174751]]'
return