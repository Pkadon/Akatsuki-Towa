label avg12513:
stop music

play music "ed7150.ogg"
scene avg_bg_014
window show
with fade_in
play sfx2 "other_7071.ogg"
c5241 '[textdict[1151034]]'
c5241 '[textdict[1151035]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1151036]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c5241 '[textdict[1151037]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1151038]]'
hide p2
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c5241 '[textdict[1151039]]'
hide p2
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1151040]]'
hide p2
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1151041]]'
hide p2
hide p3
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1151042]]'
hide p3
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c5241 '[textdict[1151043]]'
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 12', 'p3', [l(-6), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ro09.ogg"
c31 '[textdict[1151044]]'
hide p1
hide p3
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1151045]]'
hide p3
hide p1
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
c5241 '[textdict[1151046]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1151047]]'
hide p2
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c5241 '[textdict[1151048]]'
hide p2
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
c13 '[textdict[1151049]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
play sfx2 "other_7073.ogg"
c13 '[textdict[1151050]]'
return