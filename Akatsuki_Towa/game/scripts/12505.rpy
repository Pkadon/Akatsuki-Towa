label avg12505:
stop music

play music "ed7150.ogg"
scene avg_bg_014
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
window show
with fade_in
play sfx2 "other_7071.ogg"
c13 '[textdict[1150847]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
play sfx2 "other_7072.ogg"
c5241 '[textdict[1150848]]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1150849]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
c5241 '[textdict[1150850]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1150851]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c5241 '[textdict[1150852]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c5241 '[textdict[1150853]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1150854]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c5241 '[textdict[1150855]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c5241 '[textdict[1150856]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1150857]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
play sfx2 "other_7073.ogg"
c21 '[textdict[1150858]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1150859]]'
return