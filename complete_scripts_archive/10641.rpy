label avg10641:
stop music

play music "ed7513.ogg"
scene avg_bg_070
window show
with fade_in
c0 '[textdict[1164401]]'
c0 '[textdict[1164402]]'
c0 '[textdict[1164403]]'
c0 '[textdict[1164404]]'
c0 '[textdict[1164405]]'
c0 '[textdict[1164406]]'
c0 '[textdict[1164407]]'
c0 '[textdict[1164408]]'
c0 '[textdict[1164409]]'
c0 '[textdict[1164410]]'
c0 '[textdict[1164411]]'
play music "ed9999.ogg"
scene avg_bg_202
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
with fade
c43 '[textdict[1164412]]'
hide p4
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 5)
c43 '[textdict[1164413]]'
hide p4
$ update_portrait('oc004_01 10', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[textdict[1164414]]'
hide p4
hide p2
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 5)
c33 '[textdict[1164415]]'
hide p2
hide p3
$ update_portrait('oc003_01 16', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1164416]]'
hide p3
hide p2
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1164417]]'
hide p2
hide p1
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1164418]]'
hide p2
hide p1
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 13', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1164419]]'
hide p1
hide p2
$ update_portrait('oc002_01 13', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 5)
c13043 '[textdict[1164420]]'
hide p2
hide p1304
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1164421]]'
hide p1304
hide p2
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st061_01 2', 'p1304', [r(-2), light], 5)
c13043 '[textdict[1164422]]'
hide p2
hide p1304
$ update_portrait('st061_01 2', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1164423]]'
return