label avg12607:

play music "ed7151.ogg"
scene avg_bg_036
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 16', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1161283]]'
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1161284]]'
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[textdict[1161285]]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1161286]]'
return