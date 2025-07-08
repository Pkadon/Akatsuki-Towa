label avg10639:
stop music

play music "ED6105.ogg"
scene avg_bg_202
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 5)
window show
with fade_in
play sfx2 "other_7071.ogg"
c33 '[textdict[1164174]]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
play sfx2 "other_7072.ogg"
c7011 '[textdict[1164175]]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
c7011 '[textdict[1164176]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1164177]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1164178]]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c7011 '[textdict[1164179]]'
hide p1
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 5)
c33 '[textdict[1164180]]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
c7011 '[textdict[1164181]]'
hide p3
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 5)
c33 '[textdict[1164182]]'
hide p3
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 5)
c23 '[textdict[1164183]]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
c7011 '[textdict[1164184]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1164185]]'
return