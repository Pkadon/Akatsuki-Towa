label avg26017:
stop music

scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
window show
with fade_in
c23 '[textdict[1215615]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215616]]'
hide p1
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215617]]'
hide p1
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 5)
c23 '[textdict[1215618]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215619]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215620]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
c23 '[textdict[1215621]]'
hide p2
play sfx2 "other_7002.ogg"
c0 '[textdict[1215747]]'
c0 '[textdict[1215622]]'
c0 '[textdict[1215623]]'
return