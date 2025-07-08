label avg10515:
stop music

play music "ED6200.ogg"
scene avg_bg_010
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
window show
with fade_in
c31 '[textdict[1150607]]'
hide p3
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[1150608]]'
hide p3
hide p2
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1150609]]'
hide p2
hide p4
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1150610]]'
return