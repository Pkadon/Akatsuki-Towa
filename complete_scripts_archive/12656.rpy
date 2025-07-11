label avg12656:

play music "ED6300.ogg"
scene avg_bg_070
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
window show
with fade_in
c33 '[textdict[1166374]]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1166375]]'
hide p3
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1166376]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1166377]]'
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1166378]]'
hide p1
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 12', 'p4', [r(-5), r_shake, light], 5)
c43 '[textdict[1166379]]'
$ update_portrait('oc004_01 12', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1166380]]'
hide p4
$ update_portrait('oc002_01 15', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[textdict[1166381]]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[textdict[1166382]]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 5)
c33 '[textdict[1166383]]'
hide p2
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1166384]]'
hide p3
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 5)
c23 '[textdict[1166385]]'
return