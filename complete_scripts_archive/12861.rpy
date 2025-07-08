label avg12861:
stop music

play music "ed6323.ogg"
scene avg_bg_219
$ update_portrait('oc003_01 20', 'p3', [l(-6), light, flip], 6)
window show
with fade_in
c31 '[textdict[1188961]]'
hide p3
c0 '[textdict[1188962]]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
c13 '[textdict[1188963]]'
hide p1
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1188964]]'
hide p2
hide p1
c0 '[textdict[1188965]]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1188966]]'
hide p2
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 5)
c33 '[textdict[1188967]]'
scene avg_bg_070
with fade
c0 '[textdict[1188968]]'
c0 '[textdict[1188969]]'
c0 '[textdict[1188970]]'
return