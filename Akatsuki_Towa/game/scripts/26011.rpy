label avg26011:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 15', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1215566]]'
hide p1
$ update_portrait('oc002_01 19', 'p2', [mid(-3), light], 5)
c23 '[textdict[1215567]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215568]]'
hide p1
play sfx2 "other_7002.ogg"
c0 '[textdict[1215755]]'
c0 '[textdict[1215569]]'
c0 '[textdict[1215570]]'
c0 '[textdict[1215571]]'
return