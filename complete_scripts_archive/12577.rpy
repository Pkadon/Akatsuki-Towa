label avg12577:
stop music

play music "ED6523.ogg"
scene avg_bg_080
window show
with fade_in
c12611 '[textdict[1155350]]'
c12611 '[textdict[1155351]]'
$ update_portrait('uc004_02 1', 'p570', [r(-9), light], 5)
c5703 '[textdict[1155352]]'
hide p570
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
with fade
c31 '[textdict[1155353]]'
hide p3
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1155354]]'
hide p3
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1155355]]'
hide p1
hide p4
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 9', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1155356]]'
hide p4
hide p2
with fade
c12611 '[textdict[1155357]]'
return