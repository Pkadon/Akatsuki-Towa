label avg26010:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1215560]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
c23 '[textdict[1215561]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215562]]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215563]]'
hide p1
play sfx2 "other_7002.ogg"
c0 '[textdict[1215742]]'
c0 '[textdict[1215564]]'
c0 '[textdict[1215565]]'
return