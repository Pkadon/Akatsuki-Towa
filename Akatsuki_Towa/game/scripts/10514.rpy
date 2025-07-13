label avg10514:

play music "ED6200.ogg"
scene avg_bg_010
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1150601]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1150602]]'
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1150603]]'
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1150604]]'
hide p4
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1150605]]'
return