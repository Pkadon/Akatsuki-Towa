label avg12850:
stop music

play music "ed7151.ogg"
scene avg_bg_221
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1187781]]'
hide p1
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 5)
c13 '[textdict[1187782]]'
hide p1
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1187783]]'
hide p3
hide p1
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1187784]]'
hide p1
hide p3
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
c13 '[textdict[1187785]]'
return