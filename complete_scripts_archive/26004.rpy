label avg26004:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[textdict[1215518]]'
hide p2
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215519]]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215520]]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
c23 '[textdict[1215521]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215522]]'
hide p1
play sfx2 "other_7002.ogg"
c0 '[textdict[1215738]]'
c0 '[textdict[1215523]]'
c0 '[textdict[1215524]]'
return