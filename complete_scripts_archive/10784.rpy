label avg10784:

play music "ed6323.ogg"
scene avg_bg_214
$ update_portrait('oc004_01 21', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
c41 '[textdict[1177363]]'
$ update_portrait('oc004_01 21', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1177364]]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1177365]]'
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1177366]]'
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('st061_01 3', 'p1304', [r(-2), light], 5)
c13043 '[textdict[1177367]]'
hide p3
$ update_portrait('st061_01 3', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc002_01 3', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1177368]]'
hide p1304
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
c13 '[textdict[1177369]]'
return