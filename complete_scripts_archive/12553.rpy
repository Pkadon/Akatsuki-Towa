label avg12553:
stop music

play music "ED6523.ogg"
scene avg_bg_081
window show
with fade_in
c12411 '[textdict[1153036]]'
c12423 '[textdict[1153037]]'
c12431 '[textdict[1153038]]'
c12443 '[textdict[1153039]]'
c12451 '[textdict[1153040]]'
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1153041]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1153042]]'
hide p1
hide p3
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 5)
c43 '[textdict[1153043]]'
hide p4
hide p3
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1153044]]'
hide p3
hide p2
with fade
c12411 '[textdict[1153045]]'
return