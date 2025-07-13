label avg10064:

play music "ED6103.ogg"
scene avg_bg_038
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
play sfx2 "common_menu.ogg"
c11 '[textdict[1005000]]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 5)
c153 '[textdict[1005001]]'
hide p15
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1005002]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1005003]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 5)
c43 '[textdict[1005004]]'
hide p4
$ update_portrait('sc039_01 5', 'p46', [r(-13), light], 5)
c463 '[textdict[1005005]]'
$ update_portrait('sc039_01 5', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
c11 '[textdict[1005006]]'
hide p46
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[1005007]]'
return