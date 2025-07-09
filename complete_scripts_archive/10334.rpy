label avg10334:
stop music

play music "ed7105.ogg"
scene avg_bg_003
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
window show
with fade_in
c41 '[textdict[1130999]]'
hide p4
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1131003]]'
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1131004]]'
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 5)
c13 '[textdict[1131005]]'
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1131006]]'
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1131007]]'
return