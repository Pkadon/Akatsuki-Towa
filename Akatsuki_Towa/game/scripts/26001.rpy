label avg26001:

scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1215501]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
c23 '[textdict[1215502]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215503]]'
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215504]]'
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215505]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
c23 '[textdict[1215506]]'
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
c23 '[textdict[1215507]]'
hide p2
play sfx2 "other_7002.ogg"
c0 '[textdict[1215736]]'
c0 '[textdict[1215508]]'
c0 '[textdict[1215509]]'
return