label avg10852:

play music "ed7304.ogg"
scene avg_bg_203
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1189508]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1189509]]'
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
c33 '[textdict[1189510]]'
hide p4
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1189511]]'
hide p2
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1189512]]'
hide p3
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1189513]]'
return