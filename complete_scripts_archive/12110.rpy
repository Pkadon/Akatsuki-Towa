label avg12110:
stop music

play music "ed7116.ogg"
scene avg_bg_020
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
window show
with fade_in
play sfx2 "other_7020.ogg"
c11 '[textdict[1128090]]'
hide p1
$ update_portrait('oc001_01 18', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 5)
play sfx2 "fight_6024.ogg"
c2323 '[textdict[1128091]]'
hide p1
hide p232
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1128092]]'
hide p2
hide p232
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
c11 '[textdict[1128093]]'
hide p1
hide p232
c0 '[textdict[1128094]]'
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 5)
c2323 '[textdict[1128095]]'
hide p232
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1128096]]'
hide p232
hide p1
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 6)
c5383 '[textdict[1128097]]'
hide p1
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 5)
c2323 '[textdict[1128098]]'
hide p1
hide p232
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1128099]]'
hide p1
hide p232
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1128100]]'
hide p2
hide p232
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1128101]]'
hide p232
hide p3
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 6)
c5383 '[textdict[1128102]]' (what_size=(gui.text_size*1.2)) with shake
hide p3
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 5)
c2323 '[textdict[1128103]]'
hide p3
hide p232
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc003_01 14', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1128104]]'
scene avg_bg_070
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
with fade
play sfx2 "other_7020.ogg"
c33 '[textdict[1128105]]'
scene avg_bg_020
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
with fade
play sfxvoice "avg_vocal_ch11.ogg"
c21 '[textdict[1128106]]'
hide p2
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 14', 'p3', [r(-6), light], 5)
c33 '[textdict[1128107]]'
hide p3
hide p2
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 5)
c33 '[textdict[1128108]]'
hide p2
hide p3
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1128109]]'
return