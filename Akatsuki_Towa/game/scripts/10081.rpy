label avg10081:

play music "ED6103.ogg"
scene avg_bg_023
$ update_narrator('c11')
window show
with fade_in
$ update_portrait('oc001_01 1', 'p1', [l_entrance(-2), light, flip], 6)
play sfx2 "other_7047.ogg"
c11 '[textdict[1005262]]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
c6993 '[textdict[1005263]]'
c6993 '[textdict[1005264]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1005265]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
c6993 '[textdict[1005266]]'
c6993 '[textdict[1005267]]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1005268]]'
hide p2
$ update_portrait('sc039_01 4', 'p46', [l(-13), light, flip], 6)
c461 '[textdict[1005269]]'
$ update_portrait('sc039_01 4', 'p46', [l(-13), dark, flip], 6)
c6993 '[textdict[1005273]]'
hide p46
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1005274]]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 6)
c6993 '[textdict[1005275]]'
c6993 '[textdict[1005276]]'
hide p1
$ update_portrait('sc040_01 4', 'p47', [l(-9), light, flip], 6)
c471 '[textdict[1005277]]'
$ update_portrait('sc040_01 4', 'p47', [l(-9), dark, flip], 6)
c6993 '[textdict[1005279]]'
c6993 '[textdict[1005280]]'
hide p47
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1005281]]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 6)
c6993 '[textdict[1005282]]'
c6993 '[textdict[1005283]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1005284]]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
c6993 '[textdict[1005285]]'
c6993 '[textdict[1005286]]'
return