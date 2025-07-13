label avg10333:

play music "ed7105.ogg"
scene avg_bg_003
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
c41 '[textdict[1130999]]'
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc005_01 12', 'p5', [r(-6), light], 5)
c53 '[textdict[1131000]]'
hide p4
$ update_portrait('oc005_01 12', 'p5', [r(-6), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1131001]]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1131002]]'
return