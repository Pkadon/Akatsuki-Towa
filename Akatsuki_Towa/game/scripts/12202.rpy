label avg12202:
stop music

play music "ed7104.ogg"
scene avg_bg_039
window show
with fade_in
$ update_portrait('st026_01 1', 'p225', [r_entrance(-14), light], 5)
play sfx2 "other_7047.ogg"
c2253 '[textdict[1128668]]'
hide p225
$ update_portrait('oc001_01 21', 'p1', [r(-2), light], 5)
c13 '[textdict[1128669]]'
hide p1
$ update_portrait('st026_01 2', 'p225', [r(-14), light], 5)
c2253 '[textdict[1128670]]'
$ update_portrait('st026_01 2', 'p225', [r(-14), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1128671]]'
hide p225
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1128672]]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st026_01 4', 'p225', [r(-14), light], 5)
c2253 '[textdict[1128673]]'
hide p2
$ update_portrait('st026_01 4', 'p225', [r(-14), dark], 5)
$ update_portrait('sc039_01 2', 'p46', [l(-13), light, flip], 6)
c461 '[textdict[1128674]]'
hide p225
$ update_portrait('sc039_01 2', 'p46', [l(-13), dark, flip], 6)
$ update_portrait('st026_01 4', 'p225', [r(-14), light], 5)
c2253 '[textdict[1128675]]'
hide p46
$ update_portrait('st026_01 4', 'p225', [r(-14), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na16.ogg"
c11 '[textdict[1128676]]'
hide p225
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('st026_01 1', 'p225', [r(-14), light], 5)
c2253 '[textdict[1128677]]'
hide p225
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('st026_01 1', 'p225', [r(-14), light], 5)
c2253 '[textdict[1128678]]'
hide p1
hide p225
c0 '[textdict[1128679]]'
return