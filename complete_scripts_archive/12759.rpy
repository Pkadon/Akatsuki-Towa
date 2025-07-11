label avg12759:

play music "ed6564.ogg"
scene avg_bg_004
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
window show
with fade_in
c31 '[textdict[1174464]]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1174465]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1174466]]'
hide p3
hide p1
c0 '[textdict[1174467]]'
return