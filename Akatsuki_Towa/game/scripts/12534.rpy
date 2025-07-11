label avg12534:

play music "ED6301.ogg"
scene placeholderbackground
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
window show
with fade_in
c31 '[textdict[1151733]]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1151734]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1151735]]'
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 24', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li11.ogg"
c41 '[textdict[1151736]]'
hide p4
hide p1
c0 '[textdict[1151737]]'
$ update_portrait('oc004_01 15', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li27.ogg"
c41 '[textdict[1151738]]' with shake
$ update_portrait('oc004_01 15', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 5)
c23 '[textdict[1151739]]'
hide p4
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1151740]]'
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1151741]]'
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1151742]]'
hide p3
hide p2
with fade
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1151743]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 12', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1151744]]'
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1151745]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1151746]]'
return