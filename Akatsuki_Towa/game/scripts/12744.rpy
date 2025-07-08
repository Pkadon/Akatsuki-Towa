label avg12744:
stop music

play music "ed6564.ogg"
scene avg_bg_004
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
window show
with fade_in
c31 '[textdict[1172947]]'
hide p3
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1172948]]'
hide p1
hide p3
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1172949]]'
hide p3
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1172950]]'
hide p1
hide p3
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1172951]]'
return