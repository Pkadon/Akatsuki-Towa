label avg26024:
stop music

scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
window show
with fade_in
c23 '[textdict[1215656]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
c23 '[textdict[1215657]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215658]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
c23 '[textdict[1215659]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215660]]'
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215661]]'
hide p1
play sfx2 "other_7002.ogg"
c0 '[textdict[1215749]]'
c0 '[textdict[1215662]]'
c0 '[textdict[1215663]]'
c0 '[textdict[1215664]]'
return