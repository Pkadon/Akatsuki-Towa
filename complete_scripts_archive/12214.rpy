label avg12214:

play music "ed7123.ogg"
scene avg_bg_046
window show
with fade_in
$ update_portrait('oc001_01 8', 'p1', [l_entrance(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
c11 '[textdict[1120875]]'
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 5)
c33 '[textdict[1120876]]'
hide p1
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1120877]]'
hide p3
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 5)
c43 '[textdict[1120878]]'
hide p2
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1120879]]'
hide p1
hide p4
c0 '[textdict[1120880]]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1120881]]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1120882]]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 18', 'p4', [r(-5), light], 5)
c43 '[textdict[1120883]]'
$ update_portrait('oc004_01 18', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1120884]]'
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1120885]]'
return