label avg26030:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1215700]]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
c23 '[textdict[1215701]]'
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
c23 '[textdict[1215702]]'
hide p2
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215703]]'
hide p1
play sfx2 "other_7002.ogg"
c0 '[textdict[1215752]]'
c0 '[textdict[1215704]]'
c0 '[textdict[1215705]]'
c0 '[textdict[1215706]]'
c0 '[textdict[1215707]]'
return