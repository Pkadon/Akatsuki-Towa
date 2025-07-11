label avg12354:

play music "ed7123.ogg"
scene avg_bg_046
window show
with fade_in
play sfx2 "other_7048.ogg"
c10951 '[textdict[1133650]]'
c10951 '[textdict[1133651]]'
c10951 '[textdict[1133652]]'
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 5)
play sfx2 "other_7004.ogg"
c13 '[textdict[1133653]]'
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 5)
c13 '[textdict[1133654]]'
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
c10951 '[textdict[1133655]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1133657]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1133658]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch10.ogg"
c21 '[textdict[1133656]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 5)
c33 '[textdict[1133659]]'
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1133660]]'
hide p3
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 5)
c13 '[textdict[1133661]]'
return