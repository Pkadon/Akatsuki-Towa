label avg26003:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[textdict[1215512]]'
hide p2
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215513]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
c23 '[textdict[1215514]]'
hide p2
play sfx2 "other_7002.ogg"
c0 '[textdict[1215737]]'
c0 '[textdict[1215515]]'
c0 '[textdict[1215516]]'
c0 '[textdict[1215517]]'
return