label avg14024:

play music "ed7300.ogg"
scene avg_bg_071
window show
with fade_in
c0 '[textdict[1202493]]'
$ update_portrait('oc002_01 8', 'p2', [l_entrance(-3), light, flip], 6)
play sfx2 "fight_6019.ogg"
c21 '[textdict[1202494]]'
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 5', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1202495]]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1202496]]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1202497]]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1202498]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1202499]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1202500]]'
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 5)
c13 '[textdict[1202501]]'
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
c13 '[textdict[1202502]]'
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1202503]]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1202504]]'
scene avg_bg_070
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
with fade
c11 '[textdict[1202506]]'
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1202507]]'
return