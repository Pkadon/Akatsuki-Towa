label avg10531:
stop music

play music "ED6103.ogg"
scene avg_bg_023
$ update_portrait('uc001_01 1', 'p1255', [l(-2), light, flip], 6)
window show
with fade_in
c12551 '[textdict[1152336]]'
$ update_portrait('uc001_01 1', 'p1255', [l(-2), light, flip], 6)
c12551 '[textdict[1152337]]'
$ update_portrait('uc001_01 1', 'p1255', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1152338]]'
hide p1255
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1152339]]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1152340]]'
hide p3
hide p4
with fade
$ update_portrait('oc002_01 2', 'p2', [l_entrance(-3), light, flip], 6)
c21 '[textdict[1152341]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1152342]]'
hide p2
hide p1
play sfx2 "other_7004.ogg"
c0 '[textdict[1152343]]'
play sfx2 "other_7004.ogg"
c0 '[textdict[1152344]]'
play sfx2 "other_7004.ogg"
c0 '[textdict[1152345]]'
play sfx2 "other_7004.ogg"
c0 '[textdict[1152346]]'
play sfx2 "other_7004.ogg"
c0 '[textdict[1152347]]'
play sfx2 "other_7004.ogg"
c0 '[textdict[1152348]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1152349]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1152350]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('uc001_01 1', 'p1255', [l(-2), light, flip], 6)
c12551 '[textdict[1152351]]'
return