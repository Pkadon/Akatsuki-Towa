label avg10102:
stop music

play music "ED6103.ogg"
scene avg_bg_037
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
window show
with fade_in
play sfx2 "other_7071.ogg"
c11 '[textdict[1005660]]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1005661]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1005662]]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1005663]]'
hide p2
$ update_portrait('oc001_01 5', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 5)
c23 '[textdict[1005664]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
c11 '[textdict[1005665]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1005666]]'
hide p2
$ update_portrait('oc001_01 5', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1004401]]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc040_01 1', 'p47', [l(-9), light, flip], 6)
c471 '[textdict[1005668]]'
hide p2
$ update_portrait('sc040_01 1', 'p47', [l(-9), dark, flip], 6)
$ update_portrait('sc039_01 2', 'p46', [r(-13), light], 5)
c463 '[textdict[1005669]]'
hide p47
$ update_portrait('sc039_01 2', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7072.ogg"
c11 '[textdict[1005670]]'
hide p46
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
c7013 '[textdict[1005671]]'
hide p1
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1005672]]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 6)
c7013 '[textdict[1005673]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1005674]]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
c7013 '[textdict[1005675]]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
c7013 '[textdict[1005676]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7073.ogg"
c11 '[textdict[1005677]]'
hide p1
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1005678]]'
hide p1
c0 '[textdict[1005679]]'
return